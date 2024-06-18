# List of lists of birds
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle",
     "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [210, 900, 5, 136000, 26000, 112000, 5200, 28600, 4180, 2900],
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]

# List of bird dictionaries
birds_dictionaries = [
    {
        "name": "Magpie",
        "size (cm)": 60,
        "weight (g)": 210,
        "lifespan": 3.5
    },
    {
        "name": "Cockatoo",
        "size (cm)": 70,
        "weight (g)": 900,
        "lifespan": 45
    },
    {
        "name": "Hummingbird",
        "size (cm)": 10,
        "weight (g)": 5,
        "lifespan": 5
    },
    {
        "name": "Ostrich",
        "size (cm)": 270,
        "weight (g)": 136000,
        "lifespan": 40
    },
    {
        "name": "Bald Eagle",
        "size (cm)": 100,
        "weight (g)": 26000,
        "lifespan": 30
    },
    {
        "name": "Emperor Penguin",
        "size (cm)": 129,
        "weight (g)": 112000,
        "lifespan": 20
    },
    {
        "name": "Lyrebird",
        "size (cm)": 90,
        "weight (g)": 5200,
        "lifespan": 30
    },
    {
        "name": "Peacock",
        "size (cm)": 105,
        "weight (g)": 28600,
        "lifespan": 15
    },
    {
        "name": "Toucan",
        "size (cm)": 60,
        "weight (g)": 4180,
        "lifespan": 20
    },
    {
        "name": "Helmeted Hornbill",
        "size (cm)": 120,
        "weight (g)": 2900,
        "lifespan": 30
    }
]

# Print out data about the 4th bird in the list
data = [
    "name",
    "size (cm)",
    "weight (g)",
    "lifespan",
]

i = 0
print(" ")
for row in birds_list:
    print(f"{data[i].title()}: {row[3]}")
    i +=1

# Now lets try to create a menu to store data about bird 4 in.

menu_dash = "-"*70
line = ['', '|']
print(f"\n{menu_dash}")
a = 0
for n in range(4):
    print(f"{line[a]}{data[n].upper()}{' '*(15-len(data[n]))}", end = " ")
    a = 1
print(f"\n{menu_dash}")
a = 0
for row in birds_list:
    print(f'{line[a]}{row[3]}{" "*(15-len(str(row[3])))}', end = " ")
    a = 1
print("\n")


# Calculate the total weight (kg) of all of the birds in the list

# Loop through the birds dictionary list
# Print the names of the birds and their lifespans
# Calculate and print out the size to weight ratio


# Highest size to weight ratio:
# Lowest size to weight ratio: