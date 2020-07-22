- [User's Guide to query-FF](#user-s-guide-to-query-ff)
  * [Quick Start](#quick-start)
  * [What CAN you do with the query-FF example scripts?](#what-can-you-do-with-the-query-ff-example-scripts-)
    + [Filtering](#filtering)
    + [Saving products of your scripts](#saving-products-of-your-scripts)
    + [Other functions to be added in the future](#other-functions-to-be-added-in-the-future)
      - [Displaying the data throughout the process](#displaying-the-data-throughout-the-process)
      - [Basic analysis](#basic-analysis)
      - [Summarizing the data](#summarizing-the-data)
    + [General structure of custom scripts](#general-structure-of-custom-scripts)
  * [Starting with the open-FF data set that works best for you](#starting-with-the-open-ff-data-set-that-works-best-for-you)
  * [Using the power of python/pandas yourself](#using-the-power-of-python-pandas-yourself)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# User's Guide to query-FF

The **query-FF** project is a set of functions designed to facilitate the extraction
and analysis of data from the **open-FF** project to give users access to FracFocus data
that has been organized and cleaned.  See the 
[description of the open-FF project](https://frackingchemicaldisclosure.wordpress.com/).  

With the current version of `query-FF` (v2), users can filter the massive data set by
several different parameters (chemical type, state, company, year, etc.)
to a more managable size.  Future additions to query-FF will facilitate more 
filtering, exploration and analysis without the need of programming 
skills.  

Because the CodeOcean provides a complete environment to run code, `query-FF`
 also allows users **with** python/pandas knowledge to write their own
scripts to explore the entire data set directly.  We plan to include examples
of these more sophisticated scripts in later versions.

## Quick Start
- **Signup at CodeOcean for an account.**  Currently, all users are given at least 
one hour
of free computation time each month. If you signup with an academic email 
address ('.edu'), you will get 10 hours of free time each month.  In this project,
each run is currently taking less than one minute, so this free time is probably
sufficient for most people to create the data they need.

- **Find the Query-FF project at CodeOcean.**  Go to "Explore" and search for 
FracFocus or query-FF, and open the project (CodeOcean calls them capsules.)

- **Run the default published code.**  To do this, just click on the `Re-Run` button.
You may have to answer a question or two to get it started, but then it will re-run 
the project as it was published. Once it is finished, examine the results files (right-hand
panel of the webpage). You now have a new personal and private copy of 
the project that you
can edit however you see fit.  You can come back to it any time through your 
CodeOcean "dashboard."

- **Edit the default script.** Get to your private copy of query-FF, and edit
the file "working_script.py."  Run it.  You are on your way to creating your own scripts! 
If you feel you have made a mess of the code and can't figure out how to make 
it work, you 
can always create a new private copy from the published version. Go to the
[examples document](https://github.com/gwallison/query-FF/blob/master/examples.md) to
get some ideas of what to do.

## What CAN you do with the query-FF example scripts?
The example scripts help novice or non-programmers explore the open-FF data with
minimal coding.  We are trying to build a set of example scripts that cover common
uses of the data.  If you don't find an sample script to do what you need,
please contact us so we can make a this example set comprehensive enough to be 
useful.

### Filtering 
The complete open-FF data set has all years (2011-present), all states, all chemicals,
and all companies.  That's a lot of records which can make handling it pretty hard. (Without filtering,
there are over 6 million records.  That will choke most spreadsheet and graphinc programs.)

However, most of the time, users just want a subset of that data.  The query-FF 
functions can handle common filtering functions.  For example, you can remove
all but one state, or one chemical, or one operating company.  You can retrieve
only those records that are "proprietary" claims.  You can fetch just the records
in 2018.  Further, by using multiple functions, you can combine these filters
to extract very specific data sets.

### Saving products of your scripts
Once you create the data frame that you want, you can perform one last function
to create a file of your results.  You can then download that file from the 
results panel in CodeOcean to your local machine where you can do more detailed 
analysis and graphing.

Currently, we have one function to save dataframes: ```save_as_csv()``` which 
will store your data frame as a csv-formatted file. This is a common text-based
format.  Let us know if there
are other formats that would be useful to you.

### Other functions to be added in the future

#### Displaying the data throughout the process
** under construction **

#### Basic analysis
** under construction **

#### Summarizing the data
** under construction **

### General structure of custom scripts 

To extract the data you want, you write a simple script and then execute it
directly in CodeOcean.  But don't worry! These scripts do not require you to
be a programmer or to know any programming language.  Often it will be as easy as
changing a parameter or two in the supplied Sample Scripts and clicking "Run." 
Mostly you need to know is
what you want your output to look like and to think a little about what steps
will get you there.

Here's an example.  Say you want all the records in the data set for fracking events
that happened in Karnes County, Texas.  The following script will do that for you:

``` python
df = get_base_df()                        # line 1
df = filter_by_state(df,['texas'])        # line 2
df = filter_by_county(df,['karnes'])      # line 3
save_as_csv(df)                           # line 4
```
**Line 1** creates a data frame called `df` that has the entire default open-FF data set.
Something like this will be in every script. 

Just a note about script lines of this structure:  `xxx = yyy()` : What's on the 
right side of the equal sign is the function performed with the parentheses 
showing what is passed into the function.  What's on the left side
is the output from that function.  So in the case of line 1, the function 
`get_df_base`
is called, with nothing passed in.  The result of that function is
stored with the label `df`.

**Line 2** removes all records from `df` except where the `bgStateName` is 'texas'.  
We use the contents of `df` from line 1 as the input to line 2's function and
line 2's output is stored again in `df`.

**Line 3** removes all records from `df` except where the `bgCountyName` is 'carnes'.
Again, we store the output in `df`.

**Line 4** saves that resulting data frame (stored in `df`) into a file in the csv format.  This script
line does not return a dataframe.  Instead, it writes a file to disk for your later use. 
You can download it into a spreadsheet program and make cool charts, 
send it to your friends, or post it on your Instagram. 

## Starting with the open-FF data set that works best for you
**This function is under construction!** 
[[[Currently, there are two forms of the open-FF data that you can start with:
- the 'full' data set, including records that have been detected with errors
- the 'filtered' data set, that has the error-ladened and ambiguous 
records removed.  This set 
is the default set. Unless you specify the full set, you will be working with the 
filtered set.  We expect that most people will want this filtered set.

If you want to work with the full set, perhaps to investigate the nature of some
of the errors, you can use the `record_flags` field to target specific types of 
records.  (see Example...)  ]]]


## Using the power of python/pandas yourself
Although we have tried to construct Query-FF so that users don't need to know
how to program to get usable results, **if you know some programming**, you can 
access the full power of python/pandas and other
modules directly in your scripts.  Even though the samples use mostly just 
the functions that we
have defined in this project, you are not limited to them.  

Here is a silly example.  Suppose you want to have a data set for only the
operators whose name begins with the letter 'r'.  With a little python code, it is 
not too complicated:

```python
df = get_base_df()                        

companylst = list(df.bgOperatorName.unique()) # get list of all operators
r_lst = []                                    # start empty list
for company in companylst:                    # loop through company list
    if company[0]=='r':                       # if the first letter of the name is 'r'
        r_lst.append(company)                 #    append it to r_lst

df = filter_by_operator(df,keep_operators=r_lst)  # use r_lst to filter

save_as_csv(df)
```
There are more sophisticated ways of doing the same thing, but you get the
point.  You are not limited to the small set of functions *we* have defined.
