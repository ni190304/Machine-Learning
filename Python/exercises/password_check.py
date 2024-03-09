username = input('Your username ? ')

password = input('Your password: ')

pass_len = len(password)

hashed_password = '*'*pass_len 

print(f'{username}, your password {hashed_password} is {pass_len} letters long')

