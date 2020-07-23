- [Introduction](#introduction)
- [How to use these examples in your own scripts](#how-to-use-these-examples-in-your-own-scripts)
- [Simple filtering](#simple-filtering)
  * [By state](#by-state)
  * [By operator](#by-operator)
  * [By chemical](#by-chemical)
  * [By date](#by-date)
  * [Keep only proprietary records](#keep-only-proprietary-records)
  * [Reducing the number of columns saved](#reducing-the-number-of-columns-saved)
  * [Using a list of items to keep](#using-a-list-of-items-to-keep)
  * [Combining filters](#combining-filters)
- [Simple exploration](#simple-exploration)
  * [Show list of all field names](#show-list-of-all-field-names)
  * [Save lists of companies](#save-lists-of-companies)
  * [Show summary of a specific field](#show-summary-of-a-specific-field)
  * [Using the unfiltered set](#using-the-unfiltered-set)
- [Debugging your scripts](#debugging-your-scripts)
- [Defaults](#defaults)
- [Using python and pandas coding directly](#using-python-and-pandas-coding-directly)
  * [Quick diagnostics](#quick-diagnostics)
  * [Using conditionals to filter a data frame](#using-conditionals-to-filter-a-data-frame)
    + [for boolean fields](#for-boolean-fields)
  * [Using `groupby` to summarize by groups](#using--groupby--to-summarize-by-groups)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction
This file contains several simple query-FF scripts that can be used to build
a customized data set and to do exploratory analysis. 

# How to use these examples in your own scripts
To run these example scripts:
1. Copy the code from an example and paste it
into a template file.  The template file has a specific location where the 
pasted code goes.  The template file also has a set of preamble code that is 
necessary for all query-FF scripts.  You should not need to modify the preamble code.

2. After copying the example code into template, modify that code to suit your needs.

3. Save that file as `working_script.py` in the `code` directory of the CodeOcean
project.  `working_script.py` is the file that is executed when you click the 
"Reproducible-run" button.

4. When you click that run button, watch the "Run" window (lower part of the middle of the
screen). This shows the progression of the run and any errors that occur.

5. When the run is completed, any files created will be in the results section.

6. If necessary, modify the code and run again.  

Simple query-FF scripts run in less that 60 seconds of computation time, so an iterative
development of code is feasible.  

Note that the results of *every* run are kept by default in your account, and are counted
toward your overall free storage.  Because the FracFocus data sets can be quite
large, you may wish to occasionally delete runs that are not being used. (In the
list of runs in the right panel, next to the execution time of each completed run
is a 'down-arrow'.  Click on that to see the options, including the delete option.)

# Simple filtering
To get simple subsets, such as all the records for a specific state, company,
or chemical, very little code is needed.
## By state 
Here we keep all records for the state of Ohio
```python
df = get_base_df()
df = filter_by_state(df,['ohio'])  
save_as_csv(df,fn='AllOhio')
```
With this code, the output will be saved in a csv file named `AllOhio.csv`.  If
you leave out the `fn='AllOhio'` part, the default is `output.csv`.

## By operator
Keep all records where the Operator is Chesapeake.
```python
df = get_base_df()
df = filter_by_operator(df,['chesapeake'])  
save_as_csv(df)
```
This function uses the field `bgOperatorName` which is a curated version of
`OperatorName`.  There are many misspellings in the raw OperatorName that are
grouped together under a single lower-case `bgOperatorName` value.

## By chemical
Keep all records of 2-butoxy-ethanol or CAS registration number 111-76-2 
```python
df = get_base_df()
df = filter_by_bgCAS(df,casnums=['111-76-2'])  
save_as_csv(df)
```
Note that single or double quotes must be around the CAS# to indicate that it
is a string, not a number.

## By date
Keep all records in years 2016-2018
```python
df = get_base_df()
df = filter_by_year_range(df,minyr=2016,maxyr=2018)  
save_as_csv(df)
```

## Keep only proprietary records
```python
df = get_base_df()
df = keep_only_proprietary(df)  
save_as_csv(df)
```

## Reducing the number of columns saved
Maybe you only want a handful of columns in the final set. Use `keep_only_columns()':
```python
df = get_base_df()
df = keep_only_proprietary(df)  
df = keep_only_columns(df,['bgStateName','bgOperatorName','date'])
save_as_csv(df)
```

------
## Using a list of items to keep
Many of this fitering functions allow you to input a list of item to keep.  For
example, to keep Texas, Oklahoma and New Mexico, use:
```python
df = get_base_df()
df = filter_by_state(df,['texas','oklahoma','new mexico'])  
save_as_csv(df)
```
## Combining filters
To filter more than one thing, just add more filtering lines.  The following
makes a data set for 2-butoxy-ethanol for fracking events in Ohio for 
the years 2016-18.
```python
df = get_base_df()
df = filter_by_year_range(df,minyr=2016,maxyr=2018)  
df = filter_by_bgCAS(df,casnums=['111-76-2'])  
df = filter_by_state(df,['ohio'])  
save_as_csv(df)
```

# Simple exploration
Here are a few simple tools to examine fields:

## Show list of all field names
```python
df = get_base_df()
show_columns(df)
```
## Save lists of companies
To create lists of the company names in a data frame and report
the number of disclosures (for OperatingName) and records (for Supplier) use
the following commands.  For each name, the associated 'best guess' (or 'bg') name
is given.  The results are saved into csv files.
```python
df = get_base_df()
show_company_lists(df)
```
This script snippet uses the whole set, but you could filter first, say by
state or year.

## Show summary of a specific field
```python
df = get_base_df()
show_column_summary(df,columnname='TradeName') 
```
When the column contains strings (instead of numbers), the results of this function
will be saved into the results as a csv file, unless you include the parameter `save=False`.
**Under construction**

## Using the unfiltered set
The examples above use the data that was filtered by the `open-FF` project to remove
error-laden and ambiguous data.  That is the default operation.  If you want to
explore all records, use 
```python
df = get_base_df(version="full")
```
instead of 
```python
df = get_base_df()
```

# Debugging your scripts
** Under construction **
Because this project is currently under development, please feel free to contact
the authors with any questions or problems.  Your feedback will help us improve
`query-FF`

# Defaults
This file, `code/defaults.py` 
is used to set up the defaults used throughout
any given run.  Typically, you will make your code changes just in ```working_script.py```
but you may want to look at the defaults to understand the code's operation.

# Using python and pandas coding directly
The CodeOcean environment for `query-FF` allows anyone direct access to the 
FracFocus data using any python/pandas coding.  This provides a huge amount
of flexibility for those that have some coding skills.  This section provides
some ideas for developing your own scripts. You will probably benefit from having
the python and pandas documentation nearby. (Usually doing a google search is
sufficient. For example, search for "pandas groupby" to learn about the set of
parameters you can use.)  

## Quick diagnostics
Use `print(df.head())` or `print(df.tail())` to see a sample of the current data frame.
The default is five lines, but you can change that: `print(df.head(20))` 

Using `print(df.info())` will give you information about each field in a data frame,
and its overall shape.

## Using conditionals to filter a data frame
One very direct way to return a specific slice of a data frame is to use conditionals.
The following generates a data frame where the mass of a chemical is at least
1,000 pounds (the `MassIngredient` and `bgMass` fields are in pounds), and
the water volume used is greater than 7,000,000 gallons (`TotalBaseWaterVolume` is
in gallons)

```python
df = get_base_df()
df = df[df.bgMass>1000]
df = df[df.TotalBaseWaterVolume>7000000]
print(df.head())
```

You can combine conditionals with operators such as "or" ('|'):
```python
df = get_base_df()
df = df[(df.bgOperatorName=='anadarko petroleum')|(df.bgOperatorName=='chesapeake')]
print(df.bgOperatorName.unique())
```

### for boolean fields
If a field is a boolean (that is True or False), it is even easier.
```python
df = get_base_df()
df = df[df.is_on_TEDX]
print(df.head())
```
This returns all records where is_on_TEDX is `True`.  Using the negation symbol "~"
will return the opposite set of records:
```python
df = get_base_df()
df = df[~df.is_on_TEDX]
print(df.head())
```


## Using `groupby` to summarize by groups
The pandas method `groupby` gives you the ability to summarize by groups, either
single fields or multiple fields.

The following code tells you how many records there are for each bgCAS number.
```python
df = get_base_df()
gb = df.groupby('bgCAS',as_index=False)[['UploadKey']].count()
print(gb.head())
```

This code gives you a data frame with the total amount (in pounds) used across
a data frame for each chemical.
```python
df = get_base_df()
gb = df.groupby('bgCAS',as_index=False)[['bgMass']].sum()
print(gb.head())
```

If you want to sum up the `PercentHFJob` values for each disclosure (`UploadKey` is the
unique identifier for each disclosure) you could do something like this:
```python
df = get_base_df()
gb = df.groupby('UploadKey',as_index=False)[['PercentHFJob']].sum()
print(gb.head(20))
```

You can group by more than one field. The following returns a data frame
with the total number of records from each county/state combination.
```python
df = get_base_df()
gb = df.groupby(['bgStateName','bgCountyName'],as_index=False)[['bgCAS']].count()
print(gb.head(20))
```

