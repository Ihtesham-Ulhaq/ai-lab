def namestart_with_A():
    names = []
    for i in range(5):
        name = input("Enter name: ")
        if name.startswith('A') or name.startswith('a'):
            names.append(name)
    print("Names starting with 'A':", names)


namestart_with_A()
