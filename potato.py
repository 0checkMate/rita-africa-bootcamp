toe = [1,2,3]
cow = {1, 1.11, 'potato', 2, 2, 3, 4,5}
if 2 in cow:
    cow.add(1.55)
    cow.update([True, 19])
    cow.remove(1.11)
    #print(cow)

#dictionary 1
our_dict = {'boy': 'girl', 'tom': 'harry', 'goat': 'matata'}
#dictionary 2
my_dict = {
    'name':'collins',
    ('cook', 'book'): ['tom', 'bob', 'charlie'],
    'cash': 20,
    'is_available' : True,
    'job': {'qa':'bidco'}
}
my_dict.pop('job')
my_dict['name'] = 'rotich'
# print(my_dict['name'])
# print(my_dict.items())
# cash = my_dict.get('cash')
# print(cash)
# for key, value in my_dict.items():
#     print(key, value)
print(len(my_dict))