import os
import sys
sys.path.append(".")#/scripts")

import fulltext
import logging
import multiprocessing

log = logging.getLogger('fulltext')


if __name__ == '__main__':
    processes = multiprocessing.cpu_count() if len(sys.argv) <= 1 else int(sys.argv[1])

    PATH = '/pdfs'
    log.info("Convert pdfs in path '{}'".format(PATH))
    converts = fulltext.convert_directory_parallel(PATH, processes=processes)
