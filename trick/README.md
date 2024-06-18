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
header = f"{'NAME':<15} | {'SIZE (CM)':<15} | {'WEIGHT (G)':<15} | {'LIFESPAN':<15}"
divider = "-" * len(header)

# Print header
print(divider)
print(header)
print(divider)

# Print each bird's details
for i in range(len(birds_list[0])):
    print(f"{birds_list[0][i]:<15} | {birds_list[1][i]:<15} | {birds_list[2][i]:<15} | {birds_list[3][i]:<15}")

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