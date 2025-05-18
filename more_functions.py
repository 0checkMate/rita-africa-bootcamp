#defining the functions
def add_numbers(a,b):
    return(a+b)

def substract_numbers(a,b):
    return(a-b)

def multiply_numbers(a,b):
    return(a*b)

def divide_numbers(a,b):
    if b==0:
        return None #handles divisions by zero
    return a/b

#defining a numbers list
num_list = [2, 3, 0]

#defining a contant 
num1 = 2

#calling operation functions
for num in num_list:
    print(f'For number: {num}\n')
    print(f'Addition: {add_numbers(num1,num)}')
    print(f'Subtraction: {substract_numbers(num1,num)}')
    print(f'Multiplication: {multiply_numbers(num1,num)}')
    print(f'Division: {divide_numbers(num1,num)}\n')
