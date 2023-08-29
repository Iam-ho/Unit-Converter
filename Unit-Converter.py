unit = input("Select the unit please (length, weight, temperature, digital-storage, data-transfer-Second): ")
if unit == "length":
    x_type = input("Enter the first unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
    amount = input("Enter the amount: ")
    if x_type == "cm":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "cm":
            formula = amount * 1
            print(formula + " cm")
        if y_type == "mm":
            formula = float(amount) * 10
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) / 2.54
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) / 30.48
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) / 100000
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 160900
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) / 91.44
            print(formula, " yd")
        if y_type == "m":
            formula = float(amount) / 100
            print(formula, " m")
        if y_type == "ly":
            formula = float(amount) / 9.461e+17
            print(formula, " ly")
    if x_type == "mm":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "mm":
            formula = amount * 1
            print(formula + " mm")
        if y_type == "cm":
            formula = float(amount) / 10
            print(formula, " cm")
        if y_type == "in":
            formula = float(amount) / 25.4
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) / 304.8
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) / 1e-6
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 1.609e+6
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) / 914.4
            print(formula, " yd")
        if y_type == "m":
            formula = float(amount) / 1000
            print(formula, " m")
        if y_type == "ly":
            formula = float(amount) / 9.461e+18
            print(formula, " ly")
    if x_type == "m":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "m":
            formula = float(amount) * 1
            print(formula, " m")
        if y_type == "cm":
            formula = float(amount) * 100
            print(formula, " cm")
        if y_type == "mm":
            formula = float(amount) * 1000
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 39.37
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) * 3.281
            print(formula, " in")
        if y_type == "km":
            formula = float(amount) / 1000
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 1609
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) * 1094
            print(formula, " yd")
        if y_type == "ly":
            formula = float(amount) / 9,461e+15
            print(formula, " ly")
    if x_type == "in":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "in":
            formula = float(amount) * 1
            print(formula, " in")
        if y_type == "cm":
            formula = float(amount) * 2.54
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) / 39.37
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 25.4
            print(formula, " mm")
        if y_type == "ft":
            formula = float(amount) / 12
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) / 39370
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 2.54e+7
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) / 36
            print(formula, " yd")
        if y_type == "ly":
            formula = float(amount) / 3.725e+17
            print(formula, " ly")
    if x_type == "ft":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "ft":
            formula = float(amount) * 1
            print(formula, " ft")
        if y_type == "cm":
            formula = float(amount) * 30.48
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) / 3.281
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 304.8
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 12
            print(formula, " in")
        if y_type == "km":
            formula = float(amount) / 3281
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 5280
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) / 3
            print(formula, " yd")
        if y_type == "ly":
            formula = float(amount) / 3.104e+16
            print(formula, " ly")
    if x_type == "km":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "km":
            formula = float(amount) * 1
            print(formula, " km")
        if y_type == "cm":
            formula = float(amount) * 100000
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) * 1000
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 1e+6
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 39370
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) * 3281
            print(formula, " ft")
        if y_type == "mi":
            formula = float(amount) / 1.609
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) * 1904
            print(formula, " yd")
        if y_type == "ly":
            formula = float(amount) / 9.461e+12
            print(formula, " ly")
    if x_type == "mi":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "mi":
            formula = float(amount) * 1
            print(formula, " mi")
        if y_type == "cm":
            formula = float(amount) * 160900
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) * 1609
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 1.609e+6
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 63360
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) * 5280
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) * 1.609
            print(formula, " km")
        if y_type == "yd":
            formula = float(amount) * 1760
            print(formula, " yd")
        if y_type == "ly":
            formula = float(amount) / 5.879e+12
            print(formula, " ly")
    if x_type == "yd":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "yd":
            formula = float(amount) * 1
            print(formula, " yd")
        if y_type == "cm":
            formula = float(amount) * 91.44
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) / 1.094
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 914.4
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 36
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) * 3
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) / 1094
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) / 1760
            print(formula, " mi")
        if y_type == "ly":
            formula = float(amount) / 1.035e+16
            print(formula, " ly")
    if x_type == "ly":
        y_type = input("Enter the second unit type (cm, m, mm, in, ft, km, mi, yd, ly): ")
        if y_type == "ly":
            formula = float(amount) * 1
            print(formula, " ly")
        if y_type == "cm":
            formula = float(amount) * 9.461e+17
            print(formula, " cm")
        if y_type == "m":
            formula = float(amount) * 9.461e+15
            print(formula, " m")
        if y_type == "mm":
            formula = float(amount) * 9.461e+18
            print(formula, " mm")
        if y_type == "in":
            formula = float(amount) * 3.725e+17
            print(formula, " in")
        if y_type == "ft":
            formula = float(amount) * 3.104e+16
            print(formula, " ft")
        if y_type == "km":
            formula = float(amount) * 9.461e+12
            print(formula, " km")
        if y_type == "mi":
            formula = float(amount) * 5.879e+12
            print(formula, " mi")
        if y_type == "yd":
            formula = float(amount) * 1.035e+16
            print(formula, " yd")
if unit == "weight":
    x_type = input("Enter the first unit type (ton, kg, lb, g): ")
    amount = input("Enter the amount: ")
    if x_type == "ton":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "ton":
            formula = float(amount) * 1
            print(formula, " ton")
        if y_type == "kg":
            formula = float(amount) * 1000
            print(formula, " kg")
        if y_type == "lb":
            formula = float(amount) * 2205
            print(formula, " lb")
        if y_type == "g":
            formula = float(amount) * 1e+6
            print(formula, " g")
    if x_type == "kg":
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "kg":
            formula = float(amount) * 1
            print(formula, " kg")
        if y_type == "ton":
            formula = float(amount) / 1000
            print(formula, " ton")
        if y_type == "lb":
            formula = float(amount) * 2.205
            print(formula, " lb")
        if y_type == "g":
            formula = float(amount) * 1000
            print(formula, " g")
    if x_type == "lb":
        amount = input("Enter the amount: ")
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "lb":
            formula = float(amount) * 1
            print(formula, " lb")
        if y_type == "ton":
            formula = float(amount) / 2205
            print(formula, " ton")
        if y_type == "kg":
            formula = float(amount) / 2.205
            print(str(amount) + " kg")
        if y_type == "g":
            formula = float(amount) * 453.6
            print(formula, " g")
    if x_type == "g":
        amount = input("Enter the amount: ")
        y_type = input("Enter the second unit type (ton, kg, lb, g): ")
        if y_type == "g":
            formula = float(amount) * 1
            print(formula, " g")
        if y_type == "ton":
            formula = float(amount) / 1e+6
            print(formula, " ton")
        if y_type == "kg":
            formula = float(amount) / 1000
            print(formula, " kg")
        if y_type == "lb":
            formula = float(amount) / 453.6
if unit == "temperature":
    x_type = input("Enter the first unit type(c, f): ")
    amount = input("Enter the amount: ")
    if x_type == "c":
        y_type = input("Enter the second unit type (c, f): ")
        if y_type == "c":
            formula = float(amount) * 1
            print(formula, " c")
        if y_type == "f":
            formula = (float(amount) * 9/5) + 32
            print(formula, " f")
    if x_type == "f":
        y_type = input("Enter the second unit type(c, f): ")
        if y_type == "f":
            formula = float(amount) * 1
            print(formula, " f")
        if y_type == "c":
            formula = (float(amount) - 32) * 5/9
            print(formula, " c")
if unit == "digital-storage":
    x_type = input("Enter the first unit type(bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
    amount = input("Enter the amount: ")
    if x_type == "bit":
        y_type = input("Enter the second unit type(bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
        if y_type == "bit":
            formula = float(amount) * 1
            print(formula, " bit")
        if y_type == "kb":
            formula = float(amount) * 10**-3
            print(formula, " kb")
        if y_type == "Mb":
            formula = float(amount) * 10**-6
            print(formula, " Mb")
        if y_type == "Gb":
            formula = float(amount) * 10**-9
            print(formula, " Gb")
        if y_type == "Tb":
            formula = float(amount) * 10**-12
            print(formula, " Tb")
        if y_type == "Pb":
            formula = float(amount) * 10**-15
            print(formula, " Pb")
        if y_type == "Byte":
            formula = float(amount) * 0.125
            print(formula, " Byte")
        if y_type == "kB":
            formula = float(amount) * 125*10**-6
            print(formula, " kB")
        if y_type == "MB":
            formula = float(amount) * 125*10**-9
            print(formula, " MB")
        if y_type == "GB":
            formula = float(amount) * 125*10**-12
            print(formula, " GB")
        if y_type == "TB":
            formula = float(amount) * 125*10**-15
            print(formula, " TB")
        if y_type == "PB":
            formula = float(amount) * 125*10**-18
            print(formula, " PB")
    if x_type == "kb":
        y_type = input("Enter the second unit type(bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
        if y_type == "kb":
            formula = float(amount) * 1
            print(formula, " kb")
        if y_type == "bit":
            formula = float(amount) * 1000
            print(formula, " bit")
        if y_type == "Mb":
            formula= float(amount) * 10**-3
            print(formula, " Mb")
        if y_type == "Gb":
            formula = float(amount) * 10**-6
            print(formula, " Gb")
        if y_type == "Tb":
            formula = float(amount) * 10**-9
            print(formula, " Tb")
        if y_type == "Pb":
            formula = float(amount) * 10**-12
            print(formula, " Pb")
        if y_type == "Byte":
            formula = float(amount) * 125
            print(formula, " Byte")
        if y_type == "kB":
            formula = float(amount) * 0.125
            print(formula, " kB")
        if y_type == "MB":
            formula = float(amount) * 125*10**-6
            print(formula, " MB")
        if y_type == "GB":
            formula = float(amount) * 125*10**-9
            print(formula, " GB")
        if y_type == "TB":
            formula = float(amount) * 125*10**-12
            print(formula, " TB")
        if y_type == "PB":
            formula = float(amount) * 125*10**-15
            print(formula, " PB")
    if x_type == "Mb":
        y_type = input("Enter the second unit type(bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
        if y_type == "Mb":
            formula = float(amount) * 1
            print(formula, " Mb")
        if y_type == "bit":
            formula = float(amount) * 1000000
            print(formula, " bit")
        if y_type == "kb":
            formula = float(amount) * 1000
            print(formula, " kb")
        if y_type == "Gb":
            formula = float(amount) * 10**-3
            print(formula, " Gb")
        if y_type == "Tb":
            formula = float(amount) * 10**-6
            print(formula, " Tb")
        if y_type == "Pb":
            formula = float(amount) * 10**-9
            print(formula, " Pb")
        if y_type == "Byte":
            formula = float(amount) * 125000
            print(formula, " Byte")
        if y_type == "kB":
            formula = float(amount) * 125
            print(formula, " kB")
        if y_type == "MB":
            formula = float(amount) * 0.125
            print(formula, " MB")
        if y_type == "GB":
            formula = float(amount) * 125*10**-6
            print(formula, " GB")
        if y_type == "TB":
            formula = float(amount) * 125*10**-9
            print(formula, " TB")
        if y_type == "PB":
            formula = float(amount) * 125*10**-12
            print(formula, " PB")
    if x_type == "Gb":
        y_type = input("Enter the second unit type(bit, kb, Mb, Gb, Tb, Pb, Byte, kB, MB, GB, TB, PB): ")
        if y_type == "Gb":
            formula = float(amount) * 1
            print(formula, " Gb")
        if y_type == "bit":
            formula = float(amount) * 10**9
            print(formula, " bit")
        if y_type == "kb":
            formula = float(amount) * 10**6
            print(formula, " kb")
        if y_type == "Mb":
            formula = float(amount) * 10**3
            print(formula, " Mb")
        if y_type == "Tb":
            formula = float(amount) * 10**-3
            print(formula, " Tb")
        if y_type == "Pb":
            formula = float(amount) * 10**-6
            print(formula, " Pb")
        if y_type == "Byte":
            formula = float(amount) * 125*10**6
            print(formula, " Byte")
        if y_type == "kB":
            formula = float(amount) * 125*10**3
            print((amount), " kB")
        if y_type == "MB":
            formula = float(amount) * 125
            print(formula, " MB")
        if y_type == "GB":
            formula = float(amount) * 125*10**-3
            print(formula, " GB")
        if y_type == "TB":
            formula = float(amount) * 125*10**-6
            print(formula, " TB")
        if y_type == "PB":
            formula = float(amount) * 125*10**-9
            print(formula, " PB")