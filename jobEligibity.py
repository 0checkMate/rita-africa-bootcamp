#job eligibility script

age = int(input('What is your age: '))
has_degree = bool(input('Do you have a degree? True/False '))
years_experience = int(input('How many years of experience do you have? '))

if age >= 18 and has_degree == True and years_experience >= 2:
    print('Congratulations, you are eligible for professional role!')
elif age >= 18 and has_degree == True and years_experience < 2:
    print('Congratulations, you are eligible for entry level role!')
elif age >= 18 and has_degree == False and years_experience >= 5:
    print('Congratulations, you are eligible for a skilled role!')
elif age < 18:
    print('Not eligible for any role')
else:
    print('Not eligible for any role')