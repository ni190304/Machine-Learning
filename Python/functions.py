#Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    for row in picture:
        for pixel in row: 
            if(pixel):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print('')
        
show_tree()
show_tree()

#Default parametrs

def say_hello(name='Nayak', emoji='😅'):
    print(f'helllllooo {name} {emoji}')


say_hello('Nihaal', '😅')

# keyword arguments

say_hello(emoji='😅', name='Nii')

say_hello()

# return

def sum(num1 , num2):
    def another_fn(num1, num2):
        return num1 + num2
    return another_fn(num1, num2)

total = sum(10,5)

print(total)

print(sum(10,sum(10,5)))