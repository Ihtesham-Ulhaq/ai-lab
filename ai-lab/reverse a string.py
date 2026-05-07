def reverse_string(s):
    rev = ""
    for char in s[::-1]:
        rev += char
    return rev


print(reverse_string("Ihtesham"))
