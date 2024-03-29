## Notes

### Strings vs. bytes

**String:** sequence of unicode characters.  

**Bytes:** sequece of raw 8bit values.

### Template strings (string formatting)

**String doc:** [for python3](https://docs.python.org/3/library/string.html) 

[Template class](https://docs.python.org/3/library/string.html#template-strings) from string can be used for string formatting.

For simple variable substitution this is easier to use and more readable.

Templates could be supplied from a source that I can't control or I don't fully trust.

### Built-in fnctions

Find more info about built-in functions [here](https://docs.python.org/3/library/functions.html).

Use built-in functions as often as possible. This leverage the optimized existing code in Python.

### Iterators

Built-in methods to help out with sequence looping.

Use `iter()` to iterate through a file (in conjunction with `readline`).
In this case a seccond argument will be passed to `iter()`, which is called
the sentinel and and denotes when to stop iterating.

Use `enumerate()` when there's a need for indexed iteration. This also makes code easier to read.

### Transforms

Built-in functions for transforming sequences of data. Such as `filer()` and `map()`.

Use `filter()` to filter out entries from a sequence based on a criteria that is given
by a function which returns boolean.

Use `map()` to apply a given function to each entry in a sequence.

### Itertools (this is very helpful)

Find more info [here](https://docs.python.org/3/library/itertools.html).

Useful for creating iterators that generate sequences.

**Important**: the `next()` method allows to iterate through iterators.

### Function documentation strings

Use `__doc__` to print the documentation for a given function or module. E.g.: `print(map.__doc__)`.

For documenting, use literal string at the top of a function, class, module with triple quotation marks.

- First line should contain the name of the function with its parameters and a brief description.
- Then, with a line left blak, a description of the parameters (one per line).
- Modules: list important classes, funcs, exceptions.
- Classes: list important methods and members.
- Functions: if there's a return value, explain it. Mention exceptions.

### Variable argument lists (functions)

Use an asterisk to denote a function argument that takes a variable number of parameters.
These have to be defined after any positional arguments.

The convention is to name this parameter `args`.

A list can be passed as the `args` argument. It has to be passed to the function call with a leading asterisk.

### Lambda functions

When there is no need to define a whole separate funcion because of the added complexity. Improve code readability.

Defined as `lambda <parameters>: expression(parameters)`

### Keyword-only arguments

Used to define arguments that must be passed as keywords to a function.

Example: `def my_fcn(arg0, arg1, *, kw_only_arg=True)`

These are the ones defined after the `*,`.

### Advanced collections overview

- **`namedtuple`**
- **`OrderedDict`, `defaultdict`**
- **`Counter`**
- **`deque`**

### Using `namedtuple`

Create tuples which have a general name, and each entry has its own "tag".

Use `_replace()` to replace the value for a given "tag" in the tuple.

### `defaultdict`

Have a default value for each dictionay entry.

> If I try to access a key that doesn't exist, the key is created with the default value.

A `type` must be passed as an argument. It specifyes the type of the default values. This can be replaced by a `lambda` which sets the default value.

### Counters

Creates a dictionary with a count for each key.

Use `update()` to add new entries to an existing counter.

Use `most_common()` to get the most common entries and their respective counts. 

Use `subtract()` to remove entries from an existing counter.

Use `&` to get the intersection between two counters.

### OrderedDict

Regular dictionaries in Python don't keep order.

Won't keep things sorted. If changes are made, it will be necessary to re-sort it.

Equality between two ODs is true if both have the same order. 
Equality between a OD and a regular dict will be true if both have the same contents.

### Deque (Double Ended Queue)

Memory efficient when accessed through either end.

Add data: `appendleft()` or `append()`.

Remove data: `popleft()` or `pop()`.

`rotate()`: basically shift deque elements right (positive) or left (negative).

### Advanced classes overview

Use special functions and features that are part of every object in Python.

### Defining enumerations

Increase readability of code: assign easy-to-read names to constant values.

Use as hash values and iterate through them.

Not valid to have a duplicate name. 

It is valid to have duplicate values.

To prevent duplicate values, use the `unique` decorator (this is applied to the class declaraion).

Use the `auto()` function to automatically assign values.

### Class string values

Human-readable string that the object returns. This is `object.__str__(self)` and is called when the following functions are used: `str(object)`, `print(object)` and `'{}'.format(object)`. 

Python expresion to recreate an object with the same value: `object.__repr__(self)` called when `repr()` is used. This is commonly used for debugging, and it's also used when `object.__str__(self)` is not declared.

There is also the following:

- `format(object, format_spec)` --> `object.__format__(self, format_spec)`.
- `bytes(object)` --> `object.__bytes__(self)`.

### Computed attributes

Control how attributes are accessed in an object.

Retrive attribute value (called when `object.attr`): `object.__getattribute__(self, attr)` (called unconditionally, everytime) and `object.__getattr__(self, attr)` (when requested attribute can't be found in object).

When setting an attribute (`object.attr = val`), `object.__setattr__(self, attr, val)` is called.

When deleting an attribute (`del object.attr`), `object.__delattr__(self)` is called.

Discover the attributes that an object supports: `dir(object)` --> `object.__dir__(self)`.