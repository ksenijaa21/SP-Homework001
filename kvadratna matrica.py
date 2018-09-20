n = int(input("Unesite red matrice: "))
X = []

zbir_elemenata_na_glavnoj_dijagonali = zbir_elemenata_na_sporednoj_dijagonali= 0
prvi_element = 1

for i in range(n):

    X.append([])

    for j in range(n):
        X[i].append(prvi_element)

        if i == j:
            zbir_elemenata_na_glavnoj_dijagonali += prvi_element


        if i+j == n-1:
            zbir_elemenata_na_sporednoj_dijagonali += prvi_element

        prvi_element += 1

for i in range(n):
    print(X[i])

print("Zbir elemenata na glavnoj dijagonali je: " + str(zbir_elemenata_na_glavnoj_dijagonali))

print("Zbir elemenata na sporednoj dijagonali je: " + str(zbir_elemenata_na_sporednoj_dijagonali))

#Zbir elemenata na spirali je jednak zbiru svih elemenata u matrici
#Ako je red ove matrice n, matrica ima n**2 elemenata, pa je zbir elemenata suma niza od 1 do n**2

broj_elemenata = n**2
suma = 0

for i in range(1, (n**2)+1):
    suma += i

print("Zbir elemenata na spirali je: " + str(suma))