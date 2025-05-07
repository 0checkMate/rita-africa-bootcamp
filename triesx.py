# Defining the lists
names = ['Collins', 'Marina', 'Getrude', 'Bob', 'Jane']
ages = [21, 25, 16, 11, 30]

# age threshold
age_threshold = 18

#looping through the lists
for i in range(len(names)):
    if ages[i] >= age_threshold:
        print(f'{names[i]} is eligible')
    else:
        print(f'{names[i]} is not eligible')

