# Dictionary    immutable keys

dictionary = {
    'a' : [1,2,3],
    'b': 'hello',
    'x': True,
    # [100] : True,
    'a' : [2,4,7]
    
}

my_list = [
    
    {
    'a' : [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'a' : [4,5,6],
    'b': 'nihaal',
    'x': False
    
},{
    'a' : [13,21,35],
    'b': 'hello',
    'x': True
    
}
    
]

print(dictionary['a'][1])
# print(dictionary[[100]])
print(my_list[1]['a'])

print(dictionary['b'])

user = {
    'basket' : [1,2,3],
    'greet': 'hello',
    'age' : 20
}

print(user.get('age',55))
print('basket' in user)
print('age' in user.keys())
print('hello' in user.values())

print(user.items())

# user.clear()
# print(user)
user3 = user.copy()
print(user3)
print(user)

# print(user.pop('age'))
# print(user)

# print(user.popitem())
# print(user)

print(user.update({'age':55}))
print(user)
print(user.update({'ages':45}))
print(user)

user2 = dict(name='Nihaal')
print(user2)