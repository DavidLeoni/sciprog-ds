
# David Leoni Aug 2018


# Library to be included in Jupyter notebooks with commands like (note the '-i')
#
#    %run -i ../../jupman
#
# followed by
#
#    jupman_init()
#
# For reasons behind, see  discussion here: https://github.com/DavidLeoni/jupman/issues/12

import sys
import unittest
import inspect
import os
import conf
import argparse


    
jupman_root=None
jupman_toc=False

def jupman_main():
    global jupman_root
    global jupman_toc
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--root', type=str, default=None, help='a relative path to the root')
    parser.add_argument('--toc', default=False, action='store_true', help='Includes toc')

    args = parser.parse_args()

    jupman_toc = args.toc

    if args.root == None:
        chopped_path=sys.argv[0]
        prefix = ''
        while chopped_path.startswith('../'):
            chopped_path = chopped_path[len('../'):]
            prefix += '../'

        jupman_root = prefix
    else:
        jupman_root = args.root 

def jupman_init():
    """ To be called at the beginning of Jupyter sheets (must be last call in cell), right after the %run
    """
    global jupman_toc
    global jupman_root
    
    from IPython.core.display import HTML

    on_rtd = os.environ.get('READTHEDOCS') == 'True'

    if on_rtd:
        # on RTD we don't inject anything, files are set in sphinx conf.py
        print("")
    else:
        # Hacky stuff, because Jupyter only allows to set a per user custom js, we want per project js

        css = open(jupman_root + "overlay/_static/css/jupman.css", "r").read()
        tocjs = open(jupman_root + "overlay/_static/js/toc.js", "r").read()
        js = open(jupman_root + "overlay/_static/js/jupman.js", "r").read()

        ret = "<style>\n" 
        ret += css
        ret += "\n </style>\n"

        ret +="\n"

        ret += "<script>\n"
        ret += "var JUPMAN_IN_JUPYTER = true;"  
        ret += "\n"
        if jupman_toc:
            ret += tocjs
            ret += "\n"    
        ret += js
        ret += "\n</script>\n"

    return  HTML(ret)



def jupman_get_class(meth):
    """
        Taken from here: https://stackoverflow.com/a/25959545
    """

    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if cls.__dict__.get(meth.__name__) is meth:
                 return cls
        meth = meth.__func__  # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        cls = getattr(inspect.getmodule(meth),
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)  # handle special descriptor objects

def jupman_run(classOrMethodOrModule):    
    """ Runs test class or method or Module. Doesn't show code nor output in html.

        todo look at test order here: http://stackoverflow.com/a/18499093        
    """ 

    if  inspect.isclass(classOrMethodOrModule) and issubclass(classOrMethodOrModule, unittest.TestCase):        
        testcase = classOrMethodOrModule
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    elif inspect.isfunction(classOrMethodOrModule):
        meth = classOrMethodOrModule
        suite = unittest.TestSuite()
        testcase = get_class(meth)
        suite.addTest(testcase(meth.__name__))
    elif inspect.ismodule(classOrMethodOrModule):
        module = classOrMethodOrModule
        suite = unittest.TestLoader().loadTestsFromModule(module)
    else:
        raise Exception("Accepted parameters are either a TestCase class, a TestCase method or a test module. Found instead: " + str(classOrMethodOrModule))

    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )

def jupman_show_run(classOrMethod):    
    """ Runs test class or method. Code is not shown, but output is

        @since 0.19
        @deprecated Just use run()
    """    
    run(classOrMethod)


def jupman_pytut():
    """ Embeds a Python tutor in the output of the current cell, with code *current* cell stripped from the call to 
        pytut() itself. 

        - The GUI will be shown on the built Sphinx website.
        - Requires internet connection. Without, it will show standard browser message telling there is no connectivity        
    """
    #Hacky way to get variables from stack, but if we use %run -i we don't need it.
    #import inspect
    #notebook_globals = inspect.stack()[1][0].f_globals
    #code = notebook_globals["In"][-1]

    code =  In[-1]

    i = code.find('jupman_pytut()')

    if i != -1:  # check 
        extra = code[i + len('jupman_pytut()'):]
        if len(extra.strip()) > 0:
            print("ERROR: the call to jupman_pytut() must be the last in the cell, found instead this code afterwards: \n%s" % extra)
            return

    new_code =  code.replace('jupman_pytut()', '').replace('pytut()', '')

    if len(new_code.strip()) == 0:
        print("""Nothing to show ! You have to put the code in the same cell as pytut(), right before its call. For example: 

                      x = 5
                      y = x + 3
                      jupman_pytut()
               """)
        return
    else:            
        import urllib
        from IPython.display import IFrame

        params = {'code':new_code,
                  'cumulative': 'false',
                  'py':3,
                  'curInstr':0} 

        # BEWARE YOU NEED HTTP _S_ !    
        src = "https://pythontutor.com/iframe-embed.html#" + urllib.parse.urlencode(params)
        base = 200
        return IFrame(src, 900,max(base,(new_code.count('\n')*25) + base))

        
    
# being %run from notebook        
if __name__ == '__main__':
    jupman_main()
    
    