# Tuple  (immutable lists)

my_tuple = (1,2,3,4,5,5)

print(5 in my_tuple)
print(my_tuple[2])
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

user = {
    (1,2) : [1,2,3],
    'greet' : 'hello',
    'age' : 23
}

print(user[(1,2)])

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z , *other = (1,2,3,4,5)

print(x)
print(other)

