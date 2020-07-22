# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 06:59:19 2020

@author: Gary

various funtions to display progress and results to user
"""
import pandas as pd
import defaults
import inspect

def banner(text):
    """Print banner during execution of script"""
    print()
    print('*'*50)
    space = ' '*int((50 - len(text))/2)
    print(space,text,space)
    print('*'*50)

def exec_banner(name):
    """Print banner with the name of executing function"""
    text = f'executing: {name}'
    banner(text)
    
def simple_df_summary(df):
    """Show simple summary of dataframe if default.feeback_text is set to "verbose" """
    if defaults.feedback_text == 'verbose':
        print(f'  -- Num columns: {len(df.columns)}, num records: {len(df)}')
    
def show_column_summary(df,columnname='bgCAS',save=True):
    """ Display a summary of any column of a dataframe.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    columnname -- name of column to summarize
    save -- if True and the type of the column is 'string', save the resulting summary
            to disk.
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    print(f'   ** Summary for column: {columnname} **')
    if df[columnname].dtype=='bool':
        print(f'Num True: {len(df[df[columnname]==True])}, Num False: {len(df[df[columnname]==False])}')
    elif df[columnname].dtype=='O':
        print('       - number of non-empty cells in other columns')
        gb = df.groupby(columnname).count()
        print(gb)
        if save==True:
            fn = defaults.out_dir+columnname+'_summary.csv'
            gb.to_csv(fn)
            print(f'Summary saved to {fn}')
    else:
        print(df[columnname].describe())
            
def show_columns(df):
    """ Display column names of dataframe.
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    print('\n     **  Column names ** ')
    print(list(df.columns))
    
def show_company_lists(df):
    """ Save lists of raw company names with counts and associated best guess names
    
    Keyword arguments:
    df -- dataframe used as input (no default)
    """
    exec_banner(inspect.currentframe().f_code.co_name)
    gb1 = df.groupby(['OperatorName','UploadKey'],as_index=False)['APINumber'].count()
    gb1 = gb1.groupby('OperatorName',as_index=False)['UploadKey'].count()
    gb2 = df.groupby(['OperatorName'],as_index=False)['bgOperatorName'].first()
    mg = pd.merge(gb1,gb2,on='OperatorName',how='left')
    mg = mg.rename({'UploadKey':'disclosure_counts'},axis=1)
    mg.to_csv(defaults.out_dir+'OperatorName_list.csv',index=False)
    print(f'  >> OperatorName list saved.  Unique names = {len(mg)}')
    
    gb1 = df.groupby(['Supplier'],as_index=False)['UploadKey'].count()
    gb2 = df.groupby(['Supplier'],as_index=False)['bgSupplier'].first()
    mg = pd.merge(gb1,gb2,on='Supplier',how='left')
    mg = mg.rename({'UploadKey':'record_counts'},axis=1)
    mg.to_csv(defaults.out_dir+'Supplier_list.csv',index=False)
    print(f'  >> Supplier list saved.  Unique names = {len(mg)}')