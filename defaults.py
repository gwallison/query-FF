# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:36:39 2020

@author: Gary
"""

location = "local"
#location = "code-ocean"

if location=='local':
    sources = './sources/'
    out_dir = './out/'

if location=='code-ocean':
    sources = '../data/'
    out_dir = '../results/'

feedback_text = 'verbose' # if 'quiet', messages are silenced
                          # if 'verbose', lots of messages are displayed
                          
df_keep_records = 'M|A|3'
df_remove_records = 'R|1|2|4|5'

output_cols = ['UploadKey','date','bgCAS','bgMass','bgStateName','bgCountyName',
                'bgOperatorName','TotalBaseWaterVolume']
output_fn = 'output'

states_to_keep = ['ohio']
operators_to_keep = ['anadarko']
min_year_to_keep = 2011
max_year_to_keep = 2020
cas_nums_to_keep = ['7732-18-5']  #water

