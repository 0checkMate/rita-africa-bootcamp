#contacts dictionary
contacts_dict = {
    'Bob' : 123,
    'Cal' : 234,
    'Billy' : 456
}

#adding a new contact
contacts_dict['Grace'] = 111
print(contacts_dict)

#updting an existing contact
contacts_dict['Bob'] = 444
print(contacts_dict)

#remocing a contact
contacts_dict.pop('Cal')
print(contacts_dict)