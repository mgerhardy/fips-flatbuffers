"""
Compiles the fbs files into *.h files
"""
Version = None

import os
import platform
import genutil
import subprocess
from mod import log

#-------------------------------------------------------------------------------
def get_flatc_path() :
    """find flatc compiler, fail if not exists"""
    proj_path = os.path.dirname(os.path.abspath(__file__))
    flatc_path = '{}/../flatbuffers/flatc'.format(proj_path)
    flatc_path = os.path.normpath(flatc_path)
    if not os.path.isfile(flatc_path) :
        log.error("flatc executable not found")
    return flatc_path

#-------------------------------------------------------------------------------
def run_flatc(input_file, out_hdr) :
    cmd = [
        get_flatc_path(),
        '-c',
        '--gen-includes',
        '-o', out_tmp,
        input_file
    ]
    print(cmd)
    subprocess.call(cmd)

#-------------------------------------------------------------------------------
def generate(input_file, out_src, out_hdr) :
    """
    :param input_file:  flatbuffers fbs file
    :param out_src:     must be None
    :param out_hdr:     path for output header files
    """
    flatc_path = get_flatc_path()
    run_flatc(input_file, out_hdr)

