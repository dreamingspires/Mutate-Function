# Welcome to the mutate function repo!

[![PyPI version](https://badge.fury.io/py/mutate-function.svg)](https://badge.fury.io/py/mutate-function)

Mutate function was made as a tool to aid with other modules, such as FastAPI, which inspect function signatures. It allows you to replace one or more arguments in a function, and replace them with multiple arguments. This changes both the function interface and the function signature.

# Using replace arg
```py
from mutate_function import replace_arg

@replace_arg(
    'gentoo', 
    new1 = {'annotation' : str}, 
    new2 = {'annotation' : int}
)
def test_func(gentoo):
    return gentoo


test_func('test', new2 = 1)
# {'new1': 'test', 'new2': 1}
```

# Using replace args

Note: all replaced arguments are listed in the order they are defined, and additional arguments are placed at the start.

```py
from mutate_function import replace_args

@replace_args(
    new1 = {
        'replaces': 'gentoo',
        'annotation': str
    },
    new2 = {'replaces': 'gentoo'},
    new3 = {'replaces': 'adelie'}
)
def test_func(gentoo, rockhopper, adelie):
    return [gentoo, rockhopper, adelie]

test_func('test',1,2,3)

# [{'new1': 1, 'new2': 2}, 'test', {'new3': 3}]
```

# Using replace arg simple

```py
from mutate_function import replace_arg_simple

@replace_arg_simple('test', 'new')
def test_func(new):
    return new

test_func(test='test_phrase')

# 'test_phrase'
```
