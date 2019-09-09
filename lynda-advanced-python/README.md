## Notes

### Strings vs. bytes

**String:** sequence of unicode characters.  

**Bytes:** sequece of raw 8bit values.

### Template strings (String formatting)

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

Use `__doc__` to print the documentation for a given function or module. E.g. `print(map.__doc__)`.

For documenting, use literal string at the top of a function, class, module with triple quotation marks.

- First line should contain the name of the function with its parameters and a brief description.
- Then, with a line left blak, a description of the parameters (one per line).
- Modules: list important classes, funcs, exceptions.
- Classes: list important methods and members.
- Functions: if there's a return value, explain it. Mention exceptions.

### Variable argument lists (functions)





