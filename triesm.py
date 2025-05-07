names = ['Collins', 'Marina', 'Getrude', 'Bob', 'Jane']
ages = [21, 25, 16, 11, 30]

age_threshold = 18

for name, age in zip(names, ages):
    if age >= age_threshold:
        print(f'{name} is eligible')
    else:
        print(f'{name} is not eligible')