metros = [0.5, 1.0, 2.5, 5.0, 10.0, 15.0, 20.0, 25.0, 50.0, 100.0]

polegadas = [x * 39.3701 for x in metros]
pes = [x * 3.28084 for x in metros]
jardas = [x * 1.09361 for x in metros]
milhas_maritimas = [x * 0.000539957 for x in metros]

print("{:<4} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Nº", "Metros", "Polegadas", "Pés", "Jardas", "Milhas Marítimas"))
print("="*60)

for i in range(len(metros)):
    print("{:<4} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.6f}".format(i+1, metros[i], polegadas[i], pes[i], jardas[i], milhas_maritimas[i]))