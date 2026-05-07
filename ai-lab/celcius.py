def cel_to_fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    if fahrenheit > 100:
        print("hye گرمی")
    elif fahrenheit < 32:
        print("سردی ho gai a")
    else:
        print("موسم bot changa a aj")


cel_to_fah(38)
