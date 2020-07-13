# User's Guide to query-FF


The **query-FF** project is a set of functions designed to facilitate the extraction
and analysis of data from the **open-FF** project: data organized and cleaned from
FracFocus.  

## Quick Start
- **Signup at CodeOcean for an account.**  Currently, all users are given at least one hour
of free computation time each month. If you signup with an academic email 
address ('.edu'), you will get 10 hours of free time each month.  In this project,
each run is currently taking less than one minute, so this free time is probably
sufficient for most people to create the data they need.

- **Find the Query-FF project at CodeOcean.**  Go to "Explore" and search for 
FracFocus or query-FF, and open the project (CodeOcean calls them capsules.)

- **Run the default published code.**  To do this, just click on the "Re-Run" button.
You may have to answer a question or two to get it started, but then it will re-run 
project as it was published. Once it is finished, examine the results files (right-hand
panel of the webpage).

- **Edit the default script.** Click on "Edit Capsule" in the upper right corner.
This causes CodeOcean to create a new private copy of the project for you.  


## General structure of custom scripts 


To extract the data you want, you write a simple script and then execute it
directly in CodeOcean.  But don't worry! These scripts do not require you to
be a programmer or to know any programming language.  Often it will be as easy as
changing a parameter or two in the supplied Sample Scripts and clicking "Run." 
Mostly you need to know is
what you want your output to look like and to think a little about what steps
will get you there.

Here's an example.  Say you want all the records in the data set for fracking events
that happened in Carnes County, Texas.  The following script will do that for you:

``` python
df = get_df_base()                        # line 1
df = filter_by_state(df,['texas'])        # line 2
df = filter_by_county(df,['carnes'])      # line 3
save_to_csv(df)                           # line 4
```
Line 1 creates a data frame called **df** that has the entire default open-FF data set.
Something like this will be in every script. 

Just a note about script lines of this structure:  xxx = yyy() : What's on the 
right side of the equal sign is the function performed with the parentheses 
showing what is passed into the function.  What's on the left side
is the output from that function.  So in the case of line 1, the function 
**get_df_base**
is called, with nothing passed in.  The result of that function is
stored with the label **df**.

Line 2 removes all records from **df** except where the bgStateName is 'texas'.  
We use the contents of **df** from line 1 as the input to line 2's function and
line 2's output is stored again in **df**.

Line 3 removes all records from **df** except where the bgCountyName is 'carnes'

Line 4 save that resulting data frame into a file in the csv format.  This script
line does not return a dataframe.  Instead, it writes a file to disk for your use
later.

## Starting with the open-FF data set that works best for you
Currently, there are two forms of the open-FF data that you can start with:
- the 'full' data set, including records that have been detected with errors
- the 'filtered' data set, that has the error-ladened records removed.  This set 
is the default set. Unless you specify the full set, you will be working with the 
filtered set.  We expect that most people will want this filtered set.

If you want to work with the full set, perhaps to investigate the nature of some
of the errors, you can use the "record_flags" field to target specific types of 
records.  (see Example...)  

## Filtering to the set you want


## Displaying the data throughout the process


## Basic analysis


## Summarizing the data


## Saving the data



