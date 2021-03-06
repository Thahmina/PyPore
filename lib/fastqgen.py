#! /usr/bin/env python

import argparse
import atexit
import os
import shutil
import sys
import ntpath
import tempfile
from logging_module import log

####################
## Define classes ##
####################

                
class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values
        if not os.path.isdir(prospective_dir):
            log.error("readable_dir:{0} is not a directory".format(prospective_dir))
            sys.exit(1)
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            log.error("readable_dir:{0} is not a directory".format(prospective_dir))
            sys.exit(1)


def ArgsReader(args):
    global work_dir
    global file_folder
    global prefix
    global th
    global ver
    global out_dir
    work_dir = os.getcwd()
    file_folder = args.input_directory
    prefix = args.label
    th = args.threads
    ver = args.verbose
    f_flag = args.fail_reads
    if args.output_dir is not None:
        out_dir = str(args.output_dir[0])
    else:
        out_dir = 'PyPore_results'
    num_consumers = th
    ags=[work_dir, file_folder, prefix, out_dir, str(ver), str(th), str(f_flag)]
    import lib.fastqmpi as sq
    sq.run(ags)

######################
## Argument Parsing ##
######################

def run(argsin):
    ldir = tempfile.mkdtemp()
    atexit.register(lambda dir=ldir: shutil.rmtree(ldir))
    parser = argparse.ArgumentParser(add_help=False,
                                     prog='fastqgen',
                                     usage='''\r      \n
                                  ________________
                                 |                |
                                 |    #####       |
                                 |    ##  ##      |
                                 |    #####       |
                                 |    ## #####    |
                                 |    ## ##  ##   |
                                 |       #####    |
                                 |       ##       |
                                 |       ##       |
                                 |________________|

                                       PyPore    
                                      FastQGen                                 
                                                
usage: %(prog)s [-i <input_directory>] [-l <my_label>] [options]''',
                                     epilog='''
                                     
PyPore. Written by Roberto Semeraro, Department of Clinical and Sperimental Medicine,
University of Florence. For bug report or suggestion write to robe.semeraro@gmail.com''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     )
    g = parser.add_argument_group(title='mandatory arguments',
                                  description='''-i, --input_directory                                       path to the file folder
-l, --label                                                    label for fastq file
    ''')
    g.add_argument('-i', '--input_directory', action=readable_dir, default=ldir,
                   help=argparse.SUPPRESS)
    g.add_argument('-l', '--label', action='store', metavar='',
                   help=argparse.SUPPRESS)
    f = parser.add_argument_group(title='options',
                                  description='''-f, --fail_reads                                  avoid skipping of fail reads [no]
-o, --output_dir                                    if omitted, generates a results 
                                                  directory in the current position
-n, --threads_number                               number of processing threads [1]
-v, --verbose                      increase verbosity: 0 = warnings only, 1 = info, 
                                    2 = debug, 3 = debug on terminal. Default is no
                                                    verbosity. No number means info
-h, --help                                          show this help message and exit
    ''')
    f.add_argument('-f', '--fail_reads', action="store", nargs='*', default=['n'], metavar='',
                   help=argparse.SUPPRESS, choices=['y', 'n', 'yes', 'no'])
    f.add_argument('-o', '--output_dir', action="store", nargs=1, metavar='',
                   help=argparse.SUPPRESS)
    f.add_argument('-n', '--threads_number', action="store", type=int, default=1, metavar='',
                   help=argparse.SUPPRESS)
    f.add_argument('-h', '--help', action="help",
                   help=argparse.SUPPRESS)
    f.add_argument('-v', '--verbose', const=1, default=1, type=int, nargs="?",
                   help=argparse.SUPPRESS, choices=range(0, 4))

    try:
        args = parser.parse_args(argsin)
        if not args.input_directory or not args.label:
            parser.print_help()
            log.error('Missing mandatory arguments!')
            sys.exit(1)
        else:
            ArgsReader(args)
    except IOError as msg:
        parser.error(str(msg))