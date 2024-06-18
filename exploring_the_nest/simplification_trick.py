"""
This method leverages Python's string formatting capabilities to align text in columns easily.
By using the format specifier `:<15`, we ensure that each value is left-aligned within a field
of 15 characters. This approach automatically handles spacing, making the code cleaner and
more readable compared to manually adding spaces based on the length of each word.
Note: If the word exceeds 15 characters, the field will expand to accommodate the word.
"""

birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle",
     "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
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