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

df = get_base_df()                        # line 1
df = filter_by_state(df,['texas'])        # line 2
df = filter_by_county(df,['karnes'])      # line 3
save_as_csv(df)        