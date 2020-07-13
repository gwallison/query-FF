# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:42:18 2020

@author: Gary
"""
import pandas as pd
import inspect
import defaults
from modules.show_user import *


def keep_only_columns(df,cols=defaults.output_cols):
    exec_banner(inspect.currentframe().f_code.co_name)
    if cols=='all':
        print('No columns removed')
    else: df = df.filter(cols)
    simple_df_summary(df)
    return df

def drop_columns(df,cols=[]):
    exec_banner(inspect.currentframe().f_code.co_name)
    df  = df.drop(cols,axis=1)
    simple_df_summary(df)
    return df

def filter_by_state(df,keep_states=defaults.states_to_keep):
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgStateName.isin(keep_states)]
    simple_df_summary(df)
    return df

def filter_by_county(df,keep_counties=[]):
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgCountyName.isin(keep_counties)]
    simple_df_summary(df)
    return df

def filter_by_operator(df,keep_operators=defaults.operators_to_keep):
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgOperatorName.isin(keep_operators)]
    simple_df_summary(df)
    return df

def filter_by_year_range(df,minyr=defaults.min_year_to_keep,
                         maxyr=defaults.max_year_to_keep):
    exec_banner(inspect.currentframe().f_code.co_name)
    rng = list(range(minyr,maxyr+1))
    df['year'] = df.date.dt.year
    df = df[df.year.isin(rng)]
    simple_df_summary(df)
    return df

def filter_by_bgCAS(df,casnums=defaults.cas_nums_to_keep):
    exec_banner(inspect.currentframe().f_code.co_name)
    df = df[df.bgCAS.isin(casnums)]
    simple_df_summary(df)
    return df