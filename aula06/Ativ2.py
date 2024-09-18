Kelvin = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
Celsius = [(K - 273.15) for K in Kelvin]
Fahrenheit = [(C * 9/5 + 32) for C in Celsius]
print("{:<4}{:<8}{:<10}{:<12}".format("N°", "Kelvin", "Celsius", "Fahrenheit"))
print("====+=======+========+==========")

for i in range(len(Kelvin)):
    print("{:<4}{:<8}{:<10.2f}{:<12.2f}".format(i+1, Kelvin[i], Celsius[i], Fahrenheit[i]))
