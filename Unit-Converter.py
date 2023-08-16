unit = input("Select the unit please (length, weight, temperature, digital-storage, data-transfer-Second): ")
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
    if x_type == "m":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " m")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 100
            print(str(formula) + " cm")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1000
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 39.37
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 3.281
            print(str(formula) + " in")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1000
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1609
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1094
            print(str(formula) + " yd")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 9,461e+15
            print(str(formula) + " ly")
    if x_type == "in":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " in")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 2.54
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) / 39.37
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 25.4
            print(str(formula) + " mm")
        if y_type == "ft":
            amount =input("Enter the amount: ")
            formula = float(amount) / 12
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 39370
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount ")
            formula = float(amount) / 2.54e+7
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount ")
            formula = float(amount) / 36
            print(str(formula) + " yd")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula =float(amount) / 3.725e+17
            print(str(formula) + " ly")
    if x_type == "ft":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " ft")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 30.48
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) / 3.281
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 304.8
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 12
            print(str(formula) + " in")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 3281
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 5280
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) / 3
            print(str(formula) + " yd")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 3.104e+16
            print(str(formula) + " ly")
    if x_type == "km":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " km")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 100000
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1000
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1e+6
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 39370
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 3281
            print(str(formula) + " ft")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1.609
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1904
            print(str(formula) + " yd")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 9.461e+12
            print(str(formula) + " ly")
    if x_type == "mi":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " mi")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 160900
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1609
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1.609e+6
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 63360
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 5280
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1.609
            print(str(formula) + " km")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1760
            print(str(formula) + " yd")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 5.879e+12
            print(str(formula) + " ly")
    if x_type == "yd":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " yd")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 91.44
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1.094
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 914.4
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 36
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 3
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1094
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1760
            print(str(formula) + " mi")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1.035e+16
            print(str(formula) + " ly")
    if x_type == "ly":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "ly":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " ly")
        if y_type == "cm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 9.461e+17
            print(str(formula) + " cm")
        if y_type == "m":
            amount = input("Enter the amount: ")
            formula = float(amount) * 9.461e+15
            print(str(formula) + " m")
        if y_type == "mm":
            amount = input("Enter the amount: ")
            formula = float(amount) * 9.461e+18
            print(str(formula) + " mm")
        if y_type == "in":
            amount = input("Enter the amount: ")
            formula = float(amount) * 3.725e+17
            print(str(formula) + " in")
        if y_type == "ft":
            amount = input("Enter the amount: ")
            formula = float(amount) * 3.104e+16
            print(str(formula) + " ft")
        if y_type == "km":
            amount = input("Enter the amount: ")
            formula = float(amount) * 9.461e+12
            print(str(formula) + " km")
        if y_type == "mi":
            amount = input("Enter the amount: ")
            formula = float(amount) * 5.879e+12
            print(str(formula) + " mi")
        if y_type == "yd":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1.035e+16
            print(str(formula) + " yd")
if unit == "weight":
    x_type = input("Enter the first unit type (ton, kg, lb, g): ")
    if x_type == "ton":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "ton":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " ton")
        if y_type == "kg":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1000
            print(str(formula) + " kg")
        if y_type == "lb":
            amount = input("Enter the amount: ")
            formula = float(amount) * 2205
            print(str(formula) + " lb")
        if y_type == "g":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1e+6
            print(str(formula) + " g")
    if x_type == "kg":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "kg":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " kg")
        if y_type == "ton":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1000
            print(str(formula) + " ton")
        if y_type == "lb":
            amount = input("Enter the amount: ")
            formula = float(amount) * 2.205
            print(str(formula) + " lb")
        if y_type == "g":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1000
            print(str(formula) + " g")
    if x_type == "lb":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "lb":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " lb")
        if y_type == "ton":
            amount = input("Enter the amount: ")
            formula = float(amount) / 2205
            print(str(formula) + " ton")
        if y_type == "kg":
            amount = input("Enter the amount: ")
            formula = float(amount) / 2.205
            print(str(amount) + " kg")
        if y_type == "g":
            amount = input("Enter the amount: ")
            formula = float(amount) * 453.6
            print(str(formula) + " g")
    if x_type == "g":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "g":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " g")
        if y_type == "ton":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1e+6
            print(str(formula) + " ton")
        if y_type == "kg":
            amount = input("Enter the amount: ")
            formula = float(amount) / 1000
            print(str(formula) + " kg")
        if y_type == "lb":
            amount = input("Enter the amount: ")
            formula = float(amount) / 453.6
      if unit == "temperature":
    x_type = input("Enter the first unit type(c, f): ")
    if x_type == "c":
        y_type = input("Enter the second unit type (c, f): ")
        if y_type == "c":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " c")
        if y_type == "f":
            amount = input("Enter the amount: ")
            formula = (float(amount) * 9/5) + 32
            print(str(formula) + " f")
    if x_type == "f":
        y_type = input("Enter the second unit type(c, f): ")
        if y_type == "f":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " f")
        if y_type == "c":
            amount = input("Enter the amount: ")
            formula = (float(amount) - 32) * 5/9
            print(str(formula) + " c")      print(str(formula) + " lb")
if unit == "temperature":
    x_type = input("Enter the first unit type(c, f): ")
    if x_type == "c":
        y_type = input("Enter the second unit type (c, f): ")
        if y_type == "c":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " c")
        if y_type == "f":
            amount = input("Enter the amount: ")
            formula = (float(amount) * 9/5) + 32
            print(str(formula) + " f")
    if x_type == "f":
        y_type = input("Enter the second unit type(c, f): ")
        if y_type == "f":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " f")
        if y_type == "c":
            amount = input("Enter the amount: ")
            formula = (float(amount) - 32) * 5/9
            print(str(formula) + " c")
if unit == "digital-storage":
    x_type = input("Enter the first unit type(Bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
    if x_type == "Bit":
        y_type = input("Enter the second unit type(Bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
        if y_type == "Bit":
            amount = input("Enter the amount: ")
            formula = float(amount) * 1
            print(str(formula) + " Bit")
