# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 06:59:19 2020

@author: Gary

various funtions to display progress and results to user
"""
import defaults

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
        print('       - number of non-empty cells')
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
