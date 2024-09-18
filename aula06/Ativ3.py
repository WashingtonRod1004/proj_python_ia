Kg = [1, 2, 5, 10, 0.5, 0.25, 0.01, 3, 4, 7]
g = [(x * 1000) for x in Kg]
peso_terra = [(x * 9.81) for x in Kg]
peso_lua = [(x * 1.62) for x in Kg]
peso_marte = [(x * 3.71) for x in Kg]
peso_mercurio = [(x * 3.7) for x in Kg]

print("{:<4}{:<6}{:<8}{:<10}{:<10}{:<10}{:<10}".format("N°", "Kg", "gramas", "Terra (N)", "Lua (N)", "Marte (N)", "Mercúrio (N)"))
print("===+=====+========+==========+==========+==========+============")
for x in range(len(Kg)):
    print("{:<4}{:<6}{:<8}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}".format(x+1, Kg[x], g[x], peso_terra[x], peso_lua[x], peso_marte[x], peso_mercurio[x]))