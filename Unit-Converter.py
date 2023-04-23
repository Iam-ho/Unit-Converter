unit = input("Select the unit please (length, weight, temperature, digital-storage, data-transfer):\n")
if unit == "length":
    x_type = input("Enter the first unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
    if x_type == "cm":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = amount * 1
            print(formula + " cm")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 10
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) / 2.54
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) / 30.48
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 100000
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 160900
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) / 91.44
            print(str(formula) + " yd")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) / 100
            print(str(formula) + " m")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 9.461e+17
            print(str(formula) + " ly")
    if x_type == "mm":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = amount * 1
            print(formula + " mm")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) / 10
            print(str(formula) + " cm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) / 25.4
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) / 304.8
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1e-6
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1.609e+6
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) / 914.4
            print(str(formula) + " yd")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1000
            print(str(formula) + " m")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 9.461e+18
            print(str(formula) + " ly")