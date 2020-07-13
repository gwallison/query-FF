# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:08:31 2020

@author: Gary
"""

import pandas as pd
import inspect
import defaults
from modules.show_user import *

def save_as_csv(df,fn=defaults.output_fn):
    exec_banner(inspect.currentframe().f_code.co_name)
    outname = defaults.out_dir+fn+'.csv'
    df.to_csv(outname,index=False)
    print(f'  >> output file saved as: {outname}')
    simple_df_summary(df)

