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
#   User section.  Make changes below to customize the process            #
##########################################################################

#df = get_base_df()
#tab = fetch_table_from_file()
#gb = df.groupby('bgCAS',as_index=False)[['bgMass']].median()
#print(gb.head(30))
df = get_base_df()
# =============================================================================
# df = filter_by_year_range(df,minyr=2017,maxyr=2019)
# df = filter_by_state(df,['pennsylvania'])
# df = filter_by_county(df,['washington'])
# lst = make_list_of_unique(df,'bgCAS')
# analyze_cas_list(df,lst,minCount=50)
# 
# =============================================================================
