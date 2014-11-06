#!/usr/bin/python
"""
Sub-sample the preprocessed training set into subsets based on click/non-click
per hour.

Input
------
ptrain.csv: the preprocessed training set.
num: the number of subsets. Default is 10.

Output
-------
train_1 ~ num.csv: num subsets of the training set.
"""

# data file directory
FILE_DIR = './data'

import os
import copy
import csv
import random

def random_partition(lines, num):
    '''Get random partition of a list of records'''
    random.shuffle(lines)
    division = len(lines)/float(num)
    return [lines[int(round(division*i)):int(round(division*(i + 1)))]
            for i in xrange(num)]

def append_files(lines, num, is_header=False):
    '''Append subsets to files. If is_header=True, create files.'''
    if is_header:
        for i in range(num):
            with open(
                os.path.join(FILE_DIR, 'train_' + str(i) +'.csv'), "w+"
            )as f_subset:
                c = csv.writer(f_subset, delimiter=',')
                c.writerows([lines])
    else:
        subsets = random_partition(lines, num)
        # append to existing files
        for i in range(num):
            with open(
                os.path.join(FILE_DIR, 'train_' + str(i) +'.csv'), "a"
            )as f_subset:
                c = csv.writer(f_subset, delimiter=',')
                c.writerows(subsets[i])

def sub_sample(filename, num=10):
    '''Get subsamples from .csv file. Default number of subsets is 10.'''
    with open(os.path.join(FILE_DIR, filename)) as f:
        is_header = 1
        lines = [] # container
        for line in f:
            # if not header
            if not is_header:
                if lines != []: # check if not empty
                    line_split = line.split(',')
                    # check if in same hour
                    if line_last == line_split[2]:
                        lines.append(line_split)
                    else:
                        append_files(lines, num=num)
                        lines = []
                else:
                    line_split = line.split(',')
                    lines.append(line_split)
                    line_last = line_split[2] # hour indicator
            else:
                # header of the file
                file_header = line.split(',')
                append_files(file_header, num=num, is_header=is_header)
                is_header = 0
        print "subsampling SUCCEED!!"

if __name__ == "__main__":
    random.seed(3)
    sub_sample('ptrain.csv', num=10)
