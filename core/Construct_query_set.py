# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:34:50 2019

@author: GAllison

This is a stripped down version of open-FF/core/Construct_set.py that is used
to simple unpickle a data set for the query-FF project.

Change the file handles at the top of this code to appropriate directories.
    
"""
#### -----------   File handles  -------------- ####

####### uncomment below for local runs
outdir = './out/'
sources = './sources/'
tempfolder = './tmp/'

### uncomment below for running on CodeOcean
#outdir = '../results/'
#sources = '../data/'
#tempfolder = '../'


####### zip input files
zfilename = 'currentData'
stfilename = 'sky_truth_final'


#### ----------    end File Handles ----------  ####

import shutil
import os
import core.Table_manager as c_tab


class Construct_set():
    def __init__(self, sources=sources,outdir=outdir):

        self.outdir = outdir
        self.sources = sources
        self.picklefolder = self.sources+'currentData_pickles/'
        
    def get_full_set(self):
        tab_const = c_tab.Construct_tables(pkldir=self.picklefolder)
        print('loading tables from pickles...')
        tab_const.loadAllPickles()
        tab_const.listTables()
        return tab_const

