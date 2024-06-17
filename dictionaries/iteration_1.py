info = {
    'name': {
        'first': 'mason',
        'middle': 'loring',
        'last': 'galusha',
    },
    'age': 20,
    'hobbies': ['learning', 'riding motorcycles', 'engineering', 'snowboarding', 'exploring'],
    'wake-up': {
        'sunday': 10,
        'modnay': 8,
        'tuesday': 8,
        'wednesday': 8,
        'thursday': 8,
        'firday': 8,
        'saturday': 10,
    },
}

print(f"\n{info}\n")

print(f"My name is {info['name']['first'].title()} {info['name']['last'].title()}. I am {info['age']} years old.\n")

print(f"My first hobby is {info['hobbies'][0]}.\n")


# Testing working with keys and values in a list I wanted to print key and value in same sentence
iterations = 0
for key, value in info['wake-up'].items():
    iterations += 1
    if iterations == 7:
        print(f"\nTEST\nOn {key.title()} I wake up at {value} A.M.")
    else:
        pass

list = (list(info['wake-up'].items())[6])
print(f"On {list[0].title()} I wake up at {list[1]}\nTEST\n")

print(f"On Saturday I wake up at {info['wake-up']['saturday']}")

menu_dashes = '-'*60

print(menu_dashes)
print(f"Keys{' '*19}|Values{' '*20}")
print(f"{'-'*23}|{'-'*36}")
for key, value in info.items():
    num_item_spaces = 22 - len(key)
    item_spaces = ' '* num_item_spaces
    print(f"{key}{item_spaces} | {value}")
print(f"{menu_dashes}\n")

for day in info['wake-up'].keys():
    print(day.title())

print(" ")

for time in info['wake-up'].values():
    print(f"Time: {time}.00 A.M.")

print(" ")

dash_tw = '-'*30
print(dash_tw)
print(f"Day{' '*10} | Time")
print(dash_tw)

for day, time in info['wake-up'].items():
    dasher = 13 - len(day)
    dash_space = ' '*dasher
    print(f"{day.title()}{dash_space} | {time}.00 A.M.")
print(f"{dash_tw}\n")