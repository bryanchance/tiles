# Tiles

*Tiles* is a simple Python module meant to help with **code generation**.
It provides a way to deal with **rectangular areas of text** as atomic units.
This is particularly important if proper **indentation** of generated code is
desired.

Tile is a standard Python string. However, one should keep in mind that
conceptually it's just the ractangular area of text that counts. All the
surrounding whitespace has no significance.

![](tile.png)

The module provides a single function that can be used to combine smaller
tiles to create larger tiles:

```python
from tiles import tile

colors = """
         White
         Black
         Ultramarine
         Red
         Green
         Blue
         """

shapes = """
         Triangle
         Circle
         """

output = tile("""
              Colors: @{colors}     Shapes: @{shapes}

              That's all, folks!
              """)

print output
```

The output looks like this (expanded tiles marked in red):

![](output.png)

### Worked example

Imagine we want to generate code that prints out some greetings.

```python
def greet(name):
    return "print 'Hello, " + name + "!'\nprint 'Welcome!'" 
```

Although there is no particular need for manipulating rectangular areas of text
here tiling can be employed to make the code more readable.

```python
def greet(name):
    return tile("""
                print 'Hello, @{name}!'
                print 'Welcome!'
                """)
```

Given that whitespace surrounding the tile is ignored anyway we can neatly
align the generated code with the generator code instead of writing an
abomination like this:

```python
def greet(name):
    return tile("""print 'Hello, @{name}!'
print 'Welcome!'""")
```

