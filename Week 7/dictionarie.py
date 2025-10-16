# Written by Ousman

# Question 4
'''
def get_name(my_dict):
    names = []
    for key in my_dict:
        name = my_dict[key]
        names.append(name)
    return names
    names_dict = {'11': 'Ousman Kandeh', '2006': 'Student ', '224': 'Ozil'}
    print(get_name(names_dict))
'''

# Question 5
def find_oldest(persons):
    oldest_name = ""
    max_age = -1


    for key in persons:
        age = persons [name]
        if age > max_age:
            max_age = age
            oldest_name = name
    return oldest_name