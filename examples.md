

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

# Defaults
Under construction



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
df = filter_by_operator(df,operators=['chesapeake'])  
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

## Show summary of a specific field
```python
df = get_base_df()
show_column_summary(df,colname='TradeName') 
```
When the column contains strings (instead of numbers), the results of this function
will be saved into the results as a csv file, unless you include the parameter `save=False`.
**Under construction**

# Debugging your scripts
** Under construction **