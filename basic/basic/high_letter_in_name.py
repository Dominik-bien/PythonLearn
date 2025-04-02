#program to learn simple string operations in Python 
name = "rowman atkinson" 
little_name = name.lower()
upper_name = name.upper()
title_name = name.capitalize()
print(f"Hello , {name}! Do you want to learn Python?")
print(title_name)
print(upper_name)
print(little_name)
print('George R.R Martin Says: "The greatest fools are ofttimes more clever than the men who laugh at them."')
famous_person = '\tGeorge R.R Martin\n\t'
message = '"The greatest fools are ofttimes more clever than the men who laugh at them."'
print(f'{famous_person} says: {message}')

print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
