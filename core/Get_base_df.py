# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:32:40 2020

@author: Gary

This routine returns a base data frame that was created by the open-FF project.
The files pulled in are pickles of either the filtered data set (the default)
is the quick way to get data, and can be used when just filtered data is 
the target
"""

import pandas as pd
import defaults
from modules.show_user import *
import inspect


default_name = 'filtered_pickle.pkl'
full_name = 'full_pickle.pkl'

def get_base_df(sources=defaults.sources,
                version='default'):
    exec_banner(inspect.currentframe().f_code.co_name)
    print(f'  >> Loading pickle of {version} data frame')
    if version=='default':
        df = pd.read_pickle(sources+default_name)
    else:
        df = pd.read_pickle(sources+full_name)
    simple_df_summary(df)
    return df