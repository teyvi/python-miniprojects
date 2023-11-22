def say_hi(name):
    print('Hi, ' + name)

print("Let's greet the entire world")
say_hi('world')


import sys
if len(sys.argv) == 1:
    name = sys.argv[1]
else:
    name = 'stranger'
print(f'Hi there, {name}')