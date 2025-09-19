#cell 6-3
def greetings(name = ""):
    if name == "" : 
        print(f"Hello, noble stranger")
    elif isinstance(name,str):
        print(f'Hello, {name}')
    else:
        print("Error! It was not a name")
    

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)     



