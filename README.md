# pypack_test_repo

###EasyLabel:

#Description:
EasyLabel is a configurable label encoder categorical data processing.

#Requirements:
EasyLabel requires the pandas package.

Data is passed in as a simple python list or a pandas Series object and is 
returned as a pandas Series

#Functionality
The main feature of this encoder is its ability to easily create custom labels.

It is set up similarly to Scikit Learn's category-encoders, you start by creating an
instance of EasyLabel(), run a fit on your data, and transform return your data in a
pandas Series object.

The extra functionality comes in the form of `get_params()`, `return_params()` and 
`select_labels()`. `get_params()` prints the number of categories, the number of times 
each appears, a normalized list of the value counts, and the current labels. 
`return_labels()` will return category names, current labels, and value counts for
passing to other functions.

EasyLabel will by default encode categories using the number of times they appear, and
`get_params` will return a normalized list of value counts for easy use as labels.

`select_labels()` takes a list of labels. It will check the length of the list and
produce an error if the list is not the same length as the number of categories. The 
list should be ordered from most to least frequent categories as printed by `get_params()`
