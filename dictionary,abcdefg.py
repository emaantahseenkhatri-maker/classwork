my_dict ={}
my_dict = {1: 'apple' , 2 : 'ball' }
my_dict =  { 'name ': 'Aali' , 1: [2,3,5]}
my_dict = {'name': 'Aali',  'age': 4}

print(my_dict ['name'])
print(my_dict.get ('age'))

my_dict['age'] = 4
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print( "address: " , my_dict.get('address'))

my_dict.clear()
print(my_dict)
