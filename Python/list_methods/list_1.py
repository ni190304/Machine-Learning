basket = [1,2,3,4,5]

print(len(basket))

#adding
new_list = basket.append(100)
print(basket)
print(new_list)

#insert
ins_list = basket.insert(3,10)
print(basket)
print(ins_list)

#extend
ext_list = basket.extend([5,7,9,14])
print(basket)
print(ext_list)

#removing
basket.pop()
print(basket)
basket.remove(3)
print(basket)
new_list = basket.pop(5)
print(new_list)
print(basket)
