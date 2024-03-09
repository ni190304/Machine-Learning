# Sets

my_sets = {1,2,3,4,5,5}
my_list = [1,2,3,4,5,5]

print(my_sets)
print(set(my_list))
print(list(my_sets))

print(1 in my_sets)

new_set = my_sets.copy()
my_sets.clear()
print(new_set)
print(my_sets)

# Methods

my_sets = {4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_sets.difference(your_set))

# print(my_sets.discard(5))
# print(my_sets)

# print(my_sets.difference_update(your_set))
# print(my_sets)

# print(my_sets.intersection(your_set))
# print(my_sets)

# print(my_sets.isdisjoint(your_set))

# print(my_sets.union(your_set)) 
# or
# print(my_sets | your_set)

print(my_sets.issubset(your_set))

print(your_set.issuperset(my_sets))



