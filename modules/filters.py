# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:42:18 2020

@author: Gary

These functions are used to filter out some portion of the passed in dataframe.
"""
import pandas as pd
import inspect
import defaults
from modules.show_user import *


def keep_only_columns(df,cols=defaults.output_cols):
    """ Return a dataframe with all columns removed except those in "cols" list.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    cols -- list of column names to keep in returned dataframe.  
       (Default = defaults.output_cols)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    if cols=='all':
        print('No columns removed')
    else: df = df.filter(cols)
    simple_df_summary(df)
    return df

def filter_by_state(df,keep_states=defaults.states_to_keep):
    """ Return dataframe with only rows where bgStateName is in "keep_states" list.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    keep_states -- list of state names (should conform to bgStateName constraints)  
       (Default = defaults.states_to_keep)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgStateName.isin(keep_states)]
    simple_df_summary(df)
    return df

def filter_by_county(df,keep_counties=[]):
    """ Return dataframe with only rows where bgCountyName is in "keep_counties" list.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    keep_counties -- list of county names (should conform to bgCountyName constraints)  
       (Default = defaults.counties_to_keep)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgCountyName.isin(keep_counties)]
    simple_df_summary(df)
    return df

def filter_by_operator(df,keep_operators=defaults.operators_to_keep):
    """ Return dataframe with only rows where bgOperatorName is in "keep_operators" list.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    keep_operators -- list of operator names (should conform to bgOperatorName constraints)  
       (Default = defaults.operators_to_keep)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgOperatorName.isin(keep_operators)]
    simple_df_summary(df)
    return df

def filter_by_year_range(df,minyr=defaults.min_year_to_keep,
                         maxyr=defaults.max_year_to_keep):
    """ Return dataframe with only rows where date is within minyr to maxyr.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    minyr -- earliest year to keep (integer) (Default = defaults.min_year_to_keep)
    maxyr -- latest year to keep (integer) (Default = defaults.max_year_to_keep)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    rng = list(range(minyr,maxyr+1))
    df['year'] = df.date.dt.year
    df = df[df.year.isin(rng)]
    simple_df_summary(df)
    return df

def filter_by_bgCAS(df,casnums=defaults.cas_nums_to_keep):
    """ Return dataframe with only rows where bgCAS is in "casnums" list.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    casnums -- list of CAS numbers (should conform to bgCAS constraints)  
       (Default = defaults.cas_nums_to_keep)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgCAS.isin(casnums)]
    simple_df_summary(df)
    return df

def keep_only_proprietary(df):
    """ Return dataframe with only rows identified as "proprietary" claim.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.proprietary]
    simple_df_summary(df)
    return df
    