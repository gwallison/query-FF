# -*- coding: utf-8 -*-
"""
@author: GAllison

This file is used as the main script within query-FF to run analysis and 
create output files.  Users edit this file and then run the project.
    
"""
##########################################################################
#  Preamble.  Do not edit the following block of code.                   #
##########################################################################

import defaults
from modules.get_base_df import *
from modules.filters import *
from modules.save_out import *
from modules.show_user import *

##########################################################################
#   User section.  Make changes here to customize the process            #
##########################################################################

df = get_base_df()
df = filter_by_state(df,['texas'])  # can filter by more a list
#print(df.columns)
#df = filter_by_bgCAS(df,['50-00-0'])  #
#df = keep_only_columns(df,cols=['StateName','bgCountyName','bgCAS','bgMass'])
#show_column_summary(df,columnname='TradeName')
show_columns(df)
#save_as_csv(df)
