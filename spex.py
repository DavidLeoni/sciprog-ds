#!/usr/bin/python3

# This script allows initialization and management of exams.


__author__ = "David Leoni"
__status__ = "Development"

import conf
import sys
import os
import shutil
import datetime
import glob
import fnmatch
import re
from zipfile import ZipFile
import arghandler
from arghandler import ArgumentHandler
from arghandler import subcmd

import jupman_tools as jmt

from jupman_tools import info
from jupman_tools import fatal
from jupman_tools import warn
import jupman

jm = conf.jm

import logging
logging.getLogger().setLevel(logging.INFO)

def get_target_student(ld):
    return '_private/%s/student-zip/%s/'  % (ld, jm.get_exam_student_folder(ld))

def get_exam_text_filename(ld, extension):
    return 'exam-%s.%s' % (ld, extension)
    
cur_dir_names = os.listdir('.')    

if 'exam.py' not in cur_dir_names:
    fatal('You must execute exam.py from within the directory it is contained!')

# mmm should have tried th inlude !!
@subcmd(help='Set up shipped exams. Usage example:  ./spex.py fixship 2021-01-14     --exclude "*.pdf,*.js,*.png,*.css,*.pyc,*.json,*_test.py,sciprog.py,jupman.py,*-checkpoint.ipynb,ipynb_checkpoints/*,__pycache__/*,_static/*"')
def fixship(parser,context,args):
    
    parser.add_argument('date', help="date in format 'yyyy-mm-dd'" )
    parser.add_argument('--dry-run', action='store_true',)
    parser.add_argument('--include',nargs='?')
    parser.add_argument('--exclude',nargs='?')
    parsed = vars(parser.parse_args(args))
    ld = jmt.parse_date_str(parsed['date'])
    dry_run = parsed['dry_run']
    include = parsed['include']
    if include:
        include = include.split(',')
    else:
        include = []
    exclude = parsed['exclude']
    if exclude:
        exclude = exclude.split(',')
    else:
        exclude = []
        
    
    if dry_run:
        warn("DRY RUN, NOT CHANGING ANYTHING !")
    
    eld_admin = "_private/%s" % ld
    shipped_raw = "%s/shipped-raw" % eld_admin
    shipped = "%s/shipped" % eld_admin
    graded = "%s/graded" % eld_admin

    if not os.path.exists(shipped_raw):
        fatal("Couldn't find directory: " + shipped_raw)

    try:
        dir_names = next(os.walk(shipped_raw))[1]
    except Exception as e:        
        info("\n\n    ERROR! %s\n\n" % repr(e))
        exit(1)
    if len(dir_names) == 0:
        fatal("NOTHING TO FIX IN %s" % shipped_raw)
        
    for dn in dir_names:
        source = "%s/%s" % (shipped_raw, dn)
        info('source=%s' % source)
                        
        
        #shutil.copytree('%s/shipped/%s' % (eld_admin, dn) , '%s/graded' % target)
        try:
            zip_names = next(os.walk(source))[2]            
        except Exception as e:        
            info("\n\n    ERROR! %s\n\n" % repr(e))
            exit(1)
        if len(zip_names) == 0:
            fatal("NOTHING TO UNZIP IN %s/%s" % (shipped_raw, dn))
        elif len(zip_names) != 1:
            fatal("MORE THAN ONE FILE TO UNZIP IN %s/%s" % (shipped_raw, dn))

        source_zip = "%s/%s/%s" % (shipped_raw, dn, zip_names[0])

        with ZipFile(source_zip, 'r') as zip_obj:
            # Get a list of all archived file names from the zip
            fnames = zip_obj.namelist()
            # Iterate over the file names
            
            created_dir = False
            for fn in fnames:
                if 'FIRSTNAME' in fn or 'LASTNAME' in fn:
                    fatal("FOUND NON-RENAMED DIRECTORY: %s" % fn)

                if fn.startswith(f'{conf.jm.filename}-') or fn.startswith('sciprog-qcb-'):
                    if not created_dir:                          
                        folder = os.path.normpath(fn).split(os.sep)[0]
                        target_dir = "%s/%s" % (shipped, folder)
                        if (os.path.exists(target_dir)):
                            fatal("TARGET DIRECTORY ALREADY EXISTS: %s\n\n" % target_dir)
                        info("Creating target_dir %s" % target_dir)
                        if not dry_run:
                            os.makedirs(target_dir)
                        created_dir = True

                    target_path = "%s/%s" % (shipped, fn)
                    user_filepath = os.path.normpath(fn).split(os.path.sep)
                    user_filepath = "/".join(user_filepath[1:])
                    
                    if (not include or (include and any([fnmatch.fnmatch(user_filepath, ext) for ext in include])))\
                       and not any([fnmatch.fnmatch(user_filepath, ext) for ext in exclude]):
                        
                        info('extracting %s' % target_path)
                        if not dry_run:
                            zip_obj.extract(fn, shipped)
                    else:
                        info('  skipped %s' % fn)
                else:
                    fatal(f"FOUND FILE NOT IN {conf.jm.filename}-* DIRECTORY !: %s\n\n" % fn)
            # Extract all the contents of zip file in different directory
            
            #zipObj.extractall('target')
    
    print("")
    if dry_run:
        warn("END OF DRY RUN")
    else:        
        info("DONE.\n")
    print()

@subcmd(help='replaces strings in built exam version')
def build_exam(parser,context,args):

    parser.add_argument('date', help="date in format 'yyyy-mm-dd'" )
    parsed = vars(parser.parse_args(args))
    ld = jmt.parse_date_str(parsed['date'])
    server_path = f'./_private/{ld}/server'
    if not os.path.isdir(server_path):
        raise ValueError(f"ERROR! Path not existing {server_path}")
    
    exts = ['html', 'js','css', 'py', 'ipynb', 'md']
    filepaths = []
    for ext in exts: 
        filepaths.extend(glob.iglob(f'{server_path}/**/*.%s' % ext, recursive=True))
    filepaths.sort()
    for filepath in filepaths:
        print('fixing', filepath)
        if os.path.isfile(filepath):
            with open(filepath) as file:
                s = file.read()
                s = s.replace('sciprog.davidleoni.it', 'spex.altervista.org/server/ds') \
                     .replace('en.softpython.org', 'spex.altervista.org/server/softpython-en') \
                     .replace('lucamarchetti79.github.io/teaching/qcbSciProLab', 'spex.altervista.org/server/qcb') \
                     .replace('github.com/DavidLeoni/sciprog-ds', '')                                      \
                     .replace('github.com/DavidLeoni/softpython-en', '')                                      \
                     .replace('github.com/lucamarchetti79/teaching/qcbSciProLab', '')                        # better to avoid it   
                with open(filepath, "w") as file:
                    file.write(s)
                    
                    


handler = ArgumentHandler(description='Manages ' + jm.filename + ' exams.',
                         use_subcommand_help=True)
handler.run()




