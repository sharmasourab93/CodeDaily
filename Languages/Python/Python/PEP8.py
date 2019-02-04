"""Function 	function, my_function
Variable	 			x,var,my_var
Class								Model,MyClass
Method							class_method,method
Constant					CONSTANT,MY_CONSTANT
Module							module.py,my_module.py
Package						package,mypackage


Surround top-level functions and classes with two blank lines
Surround method definitions inside classes with a single blank line.
Use blank lines sparingly inside functions to show clear steps

PEP 8 suggests lines should be limited to 79 characters.
If it is impossible to use implied continuation, then you can use backslashes to break lines instead
If line breaking needs to occur around binary operators, like + and *, it should occur before the operator.
The key indentation rules laid out by PEP 8 are the following:
    Use 4 consecutive spaces to indicate indentation.
Prefer spaces over tabs.

To improve readability, you should indent a continued line to show that it is a continued line.
There are two ways of doing this.
	1. Align the indented block with the opening delimiter
	2. Use a hanging indent

Where to Put the Closing Brace

Here are some key points to remember when adding comments to your code:

	1.Limit the line length of comments and docstrings to 72 characters.
	2.Use complete sentences, starting with a capital letter.
	3.Make sure to update comments if you change your code.

Use block comments to document a small section of code.

The most important rules applying to docstrings are the following:

Surround docstrings with three double quotes on either side, as in """"""This is a docstring.""""""
Write them for all public modules, functions, classes, and methods.
Put the """"""that ends a multiline docstring on a line by itself
For one-line docstrings, keep the """""" on the same line

Surround the following binary operators with a single space on either side:

Assignment operators (=, +=, -=, and so forth)

Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)

Booleans (and, not, or)
When = is used to assign a default value to a function argument, do not surround it with spaces.
The most important place to avoid adding whitespace is at the end of a line.

The following list outlines some cases where you should avoid adding whitespace:
Immediately inside parentheses, brackets, or braces
Before a comma, semicolon, or colon
Before the open parenthesis that starts the argument list of a function call
Before the open bracket that starts an index or slice
Between a trailing comma and a closing parenthesis
To align assignment operators:


Don’t compare boolean values to True or False using the equivalence operator
Use the fact that empty sequences are falsy in if statements
Don’t use if x: when you mean if x is not None
Use .startswith() and .endswith() instead of slicing


However, some guidelines in PEP 8 are inconvenient in the following instances:

If complying with PEP 8 would break compatibility with existing software
If code surrounding what you’re working on is inconsistent with PEP 8
If code needs to remain compatible with older versions of Python
"""
x = 5
if x > 3 and x < 10:
    print(x)

#Recommended
var = function(
    arg_one, arg_two,
    arg_three, arg_four)

#Not Recommended

var=function(arg_one, arg_two,
    arg_three, arg_four)

#Recommeded Function

def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one

#Not Recommeded
def function_one(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one

#Close the Brace
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]

#Block Comments
for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')
    
x = 5  # This is an inline comment

#Not Recommended
empty_list = []  # Initialize empty list

x = 5
x = x * 5  # Multiply x by 5
#Whitespace
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)

list[3:4]

# Treat the colon as the operator with lowest priority
list[x+1 : x+2]

# In an extended slice, both colons must be
# surrounded by the same amount of whitespace
list[3:4:5]
list[x+1 : x+2 : x+3]

# The space is omitted if a slice parameter is omitted
list[x+1 : x+2 :]

# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')
    
# Recommended
my_list = []
if not my_list:
    print('List is empty!')
