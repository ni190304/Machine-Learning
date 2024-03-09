li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

# Data Structure

amazon_cart = ['notebook', 'sunglasses','toys','grapes','apples']

# print(amazon_cart[0])

# List Slicing

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]  # very important
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# print(amazon_cart[0:3])

