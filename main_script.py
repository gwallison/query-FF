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

version = 'default'  # 'default' or 'full'

df = get_base_df(version=version)
df = filter_by_state(df,['texas','ohio'])  # can filter by more a list
df = filter_by_bgCAS(df,['50-00-0'])  #
df = keep_only_columns(df,cols=['bgCountyName','bgCAS','bgMass'])
save_as_csv(df)
