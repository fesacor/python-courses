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