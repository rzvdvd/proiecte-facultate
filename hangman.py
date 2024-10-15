import csv

frecventa_litere = 'EAÎRNTIOSLCMDPUFBĂVZGHTȘÂJXQK'
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂÎȘȚ'

def citire_cuvinte(cuv_de_verif):
    cuvinte_de_ghicit = []
    with open(cuv_de_verif, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            cod, cuv_cenzurat, cuv_final = row
            cuvinte_de_ghicit.append((cod, cuv_cenzurat.strip(), cuv_final.strip()))
    return cuvinte_de_ghicit

def ghiceste_litera(cuv_curent, cuv_final, litere_incercate):
    for litera in frecventa_litere:
        if litera not in litere_incercate and litera in cuv_final:
            return litera

    for litera in alfabet:
        if litera not in litere_incercate and litera in cuv_final:
            return litera
    return None

def actualizeaza_cuvant(cuv_curent, cuv_final, litera):
    cuvant_actualizat = list(cuv_curent)
    for i, l in enumerate(cuv_final):
        if l == litera:
            cuvant_actualizat[i] = litera
    return ''.join(cuvant_actualizat)

def simulare(cuv_cenzurat, cuv_final, incercari_ramase):
    cuv_curent = cuv_cenzurat
    litere_incercate = set()
    incercari_folosite = 0

    while cuv_curent != cuv_final and incercari_ramase > 0:
        litera = ghiceste_litera(cuv_curent, cuv_final, litere_incercate)
        if litera is None:
            break
        litere_incercate.add(litera)

        cuv_curent = actualizeaza_cuvant(cuv_curent, cuv_final, litera)
        incercari_folosite += 1
        incercari_ramase -= 1

    return cuv_curent, incercari_folosite

def ghicire_cuvinte(cuvinte_de_ghicit, max_incercari):
    incercari_totale = 0
    for cod, cuv_cenzurat, cuv_final in cuvinte_de_ghicit:
        incercari_ramase = max_incercari - incercari_totale
        if incercari_ramase <= 0:
            print(f"Limita de {max_incercari} incercari a fost atinsa.")
            break

        cuv_ghicit, incercari_folosite = simulare(cuv_cenzurat, cuv_final, incercari_ramase)
        incercari_totale += incercari_folosite


        print(f"Cod: {cod}, Cuvant ghicit: {cuv_ghicit}, Incercari folosite: {incercari_folosite}, Incercari totale: {incercari_totale}")

    print(f"Numarul total de incercari este: {incercari_totale}")


cuv_de_verif = "D:/hangman/hangman/cuvinte_de_verificat.txt"
cuvinte_de_ghicit = citire_cuvinte(cuv_de_verif)
max_incercari = 1200
ghicire_cuvinte(cuvinte_de_ghicit, max_incercari)
