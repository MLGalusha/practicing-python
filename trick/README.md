# Using String Formatting to Align Text in Columns

This method leverages Python's string formatting capabilities to align text in columns easily.
By using the format specifier `:<15`, we ensure that each value is left-aligned within a field
of 15 characters. This approach automatically handles spacing, making the code cleaner and
more readable compared to manually adding spaces based on the length of each word.
Note: If the word exceeds 15 characters, the field will expand to accommodate the word.

## Example Code

```python
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle", "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [210, 900, 5, 136000, 26000, 112000, 5200, 28600, 4180, 2900],
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]

# Header
header = f"{'NAME':<18} | {'SIZE (CM)':<10} | {'WEIGHT (G)':<10} | {'LIFESPAN':<10}"
divider = "-" * len(header)

# Print header
print(divider)
print(header)
print(divider)

# Print each bird's details
for i in range(len(birds_list[0])):
    print(f"{birds_list[0][i]:<18} | {birds_list[1][i]:<10} | {birds_list[2][i]:<10} | {birds_list[3][i]:<10}")

# Print footer
print(divider)
```

## Output

```markdown
---------------------------------------------------------
NAME               | SIZE (CM)  | WEIGHT (G) | LIFESPAN
---------------------------------------------------------
Magpie             | 60         | 210        | 3.5
Cockatoo           | 70         | 900        | 45
Hummingbird        | 10         | 5          | 5
Ostrich            | 270        | 136000     | 40
Bald Eagle         | 100        | 26000      | 30
Emperor Penguin    | 129        | 112000     | 20
Lyrebird           | 90         | 5200       | 30
Peacock            | 105        | 28600      | 15
Toucan             | 60         | 4180       | 20
Helmeted Hornbill  | 120        | 2900       | 30
---------------------------------------------------------
```

## Revised Dynamic Version

```python
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle", "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [210, 900, 5, 136000, 26000, 112000, 5200, 28600, 4180, 2900],
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]


# First we want to make a preset for the headers so we can get the length of each
# seperatly
headers = ["NAME", "SIZE (CM)", "WEIGHT (G)", "LIFESPAN"]


# Combine headers and data for max length calculation
# This is so that it takes into account the max length of both the headers and
# the corresponding data under the headers in order for things to always line up.
combined = [
    [headers[0]] + birds_list[0],
    [headers[1]] + birds_list[1],
    [headers[2]] + birds_list[2],
    [headers[3]] + birds_list[3],
]

# Calculate the maximum width for each column
# Sorry for the complexity this is essentially a list comprehension within a list comprehension
# I am basically going into each column which is column in combined then we want to get the item
# with the maximum length so I need to convert each item to a string so I can record the length
# for each item. Once each item has a recorded length I then can use max to record the maximum
# length of the entire column
max_lengths = [max(len(str(item)) for item in column) for column in combined]

# Now we have the max length for each colum so we create a variable to store it to use for later
format_str = f"{{:<{max_lengths[0]}}} | {{:<{max_lengths[1]}}} | {{:<{max_lengths[2]}}} | {{:<{max_lengths[3]}}}"

# Now we just create the header using the format_str and add each individual header from the headers list.
header = format_str.format(headers[0], headers[1], headers[2], headers[3])
divider = "-" * len(header)

# Print header
print(divider)
print(header)
print(divider)

# Now we have the max length for each column stored in format_str so we will simply use that
for i in range(len(birds_list[0])):
    print(format_str.format(birds_list[0][i], birds_list[1][i], birds_list[2][i], birds_list[3][i]))

# Print footer
print(divider)

```

```markdown
-----------------------------------------------------
NAME              | SIZE (CM) | WEIGHT (G) | LIFESPAN
-----------------------------------------------------
Magpie            | 60        | 210        | 3.5
Cockatoo          | 70        | 900        | 45
Hummingbird       | 10        | 5          | 5
Ostrich           | 270       | 136000     | 40
Bald Eagle        | 100       | 26000      | 30
Emperor Penguin   | 129       | 112000     | 20
Lyrebird          | 90        | 5200       | 30
Peacock           | 105       | 28600      | 15
Toucan            | 60        | 4180       | 20
Helmeted Hornbill | 120       | 2900       | 30
-----------------------------------------------------
```
