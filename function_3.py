def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :p
        return
    
    print('Hi there, ', name)
optional_greeter('Xander')
