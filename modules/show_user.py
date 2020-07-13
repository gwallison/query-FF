# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 06:59:19 2020

@author: Gary

various funtions to display progress and results to user
"""
import defaults

def banner(text):
    print()
    print('*'*50)
    space = ' '*int((50 - len(text))/2)
    print(space,text,space)
    print('*'*50)

def exec_banner(name):
    text = f'executing: {name}'
    banner(text)
    
def simple_df_summary(df):
    if defaults.feedback_text == 'verbose':
        print(f'  -- Num columns: {len(df.columns)}, num records: {len(df)}')
    

