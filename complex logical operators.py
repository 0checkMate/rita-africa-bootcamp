#job eligibility script

age = int(input('What is your age: '))
has_degree = bool(input('Do you have a degree? True/False: '))
years_experience = int(input('How many years of experience do you have? '))

#checking for eligibility
if age >= 18:
    if has_degree == True:
        if years_experience >= 2:
            print('Congratulations, you are eligible for professional role!')
        elif years_experience < 2:
            print('Congratulations, you are eligible for entry level role!')
    elif has_degree == False:
        if years_experience >= 5:
            print('Congratulations, you are eligible for a skilled role!')
elif age < 18:
    print('Not eligible for any role')
else:
    print('Not eligible for any role')