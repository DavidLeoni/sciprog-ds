
# Changelog

Jupman Jupyter Manager  http://jupman.readthedocs.com


## v0.8, August 12th, 2018

- Fixes #11: replaced index with proper homepage. 
  
  - from now on you need home.ipynb file, because replacing index.rst is a nightmare! 
  - new index.rst is just a placeholder which simply redirects to home.html. Do not modify it.
  - put the toctree in toc.rst
  
  NOTE: All alternatives I tried failed miserably:

    - Markdown: index as markdown is not supported, and I dont' want to use .rst
    - Jupyter notebook : if you try to include toc in a jupyter notebook, Sphinx doesn't put index page paragraphs in the left sidebar
    - Select other theme: if you change from RTD theme, you don't get sidebar links on every page 

- Closes #12: exercises ipynb can now stay in exercises/ folder; when exercises are zipped,
  jupman automatically adds to the zip the required site files. The downside is that now we have to write      
  `sys.path.append('../../')`   at the beginning of all the notebooks :-/

- disabled toc by default in html files. To enable it, in python use jupman.init(toc=True)
- renamed past-exams directory from 'past-exams' to 'exams'
- created `info`, `error`, `warn`, `fatal` functions to `conf.py`
- introduced new variable `exercise_common_files` in `conf.py` for common files to be zipped
- added pages `exam-project` , `markdown` , `project-ideas`, 
- added `cc-by.png`
- renamed `changelog.txt` to `changelog.md`
- now using templates with curly brackets in in templating, like `_JM_{some_property}`
- jupman.js : now when manually saving html in Jupyter, resulting html correctly hides cells
- Fixes #2 : now toc is present in local build for pdfs 

## V0.7 , August 3rd, 2018

- added jupman.py pytut() for displaying Python tutor in the cells
- added  jupman.py toc=False option to jupman.py init to disable toc
- removed  jupman.pyuseless networkx import from 

- fixed usage indentation
- added changelog.txt

