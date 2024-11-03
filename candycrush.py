import random

#genereaza o matrice de 11 pe 11 cu numere alese aleator intre 1 si 4
def creare_matrice():
    matrice = [[random.randint(1, 4) for _ in range(11)] for _ in range(11)]
    return matrice

#itereaza prin matrice in cautarea de tupluri(3 elemente identice, fie pe orizontal sau vertical)
def linie_de_3(matrice):
    formatiuni = []
    for i in range(11):
        for j in range(9):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] != 0:
                formatiuni.append((3, [(i, j), (i, j + 1), (i, j + 2)]))
    for i in range(9):
        for j in range(11):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] != 0:
                formatiuni.append((3, [(i, j), (i + 1, j), (i + 2, j)]))
    return formatiuni

#itereaza prin matrice in cautarea de formatiuni de marimea 4
def linie_de_4(matrice):
    formatiuni = []
    for i in range(11):
        for j in range(8):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] == matrice[i][j + 3] != 0:
                formatiuni.append((4, [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]))
    for i in range(8):
        for j in range(11):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] == matrice[i + 3][j] != 0:
                formatiuni.append((4, [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]))
    return formatiuni

#itereaza in matrice in cautarea de formatiuni de marimea 5
def linie_de_5(matrice):
    formatiuni = []
    for i in range(11):
        for j in range(7):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] == matrice[i][j + 3] == matrice[i][j + 4] != 0:
                formatiuni.append((5, [(i, j), (i, j + 1), (i, j + 2), (i, j + 3), (i, j + 4)]))
    for i in range(7):
        for j in range(11):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] == matrice[i + 3][j] == matrice[i + 4][j] != 0:
                formatiuni.append((5, [(i, j), (i + 1, j), (i + 2, j), (i + 3, j), (i + 4, j)]))
    return formatiuni

#cuata grupuri de 5 elemente in forma de l, in matrice la diferite pozitii;
def linie_forma_L(matrice):
    formatiuni = []
    for i in range(9):
        for j in range(9):
            culoare = matrice[i][j]
            if culoare != 0:
                if (matrice[i + 1][j] == culoare and matrice[i + 2][j] == culoare and
                        matrice[i][j + 1] == culoare and matrice[i][j + 2] == culoare):
                    formatiuni.append((20, [(i, j), (i + 1, j), (i + 2, j), (i, j + 1), (i, j + 2)]))
                elif (matrice[i][j + 1] == culoare and matrice[i][j + 2] == culoare and
                      matrice[i + 1][j + 2] == culoare and matrice[i + 2][j + 2] == culoare):
                    formatiuni.append((20, [(i, j), (i, j + 1), (i, j + 2), (i + 1, j + 2), (i + 2, j + 2)]))
                elif (matrice[i + 1][j] == culoare and matrice[i + 2][j] == culoare and
                      matrice[i + 2][j + 1] == culoare and matrice[i + 2][j + 2] == culoare):
                    formatiuni.append((20, [(i, j), (i + 1, j), (i + 2, j), (i + 2, j + 1), (i + 2, j + 2)]))
                elif (matrice[i][j + 1] == culoare and matrice[i][j + 2] == culoare and
                      matrice[i + 1][j] == culoare and matrice[i + 2][j] == culoare):
                    formatiuni.append((20, [(i, j), (i, j + 1), (i, j + 2), (i + 1, j), (i + 2, j)]))
    return formatiuni

#cauta in matrice formatiuni de tip T, in 2 pozitii, una orizontala si una verticala
def linie_forma_T(matrice):
    formatiuni = []
    for i in range(1, 10):
        for j in range(1, 10):
            culoare = matrice[i][j]
            if culoare != 0:
                if (matrice[i][j - 1] == culoare and matrice[i][j] == culoare and matrice[i][j + 1] == culoare):
                    if (i - 1 >= 0 and matrice[i - 1][j] == culoare and i - 2 >= 0 and matrice[i - 2][j] == culoare):
                        formatiuni.append((30, [(i - 1, j), (i - 2, j), (i, j - 1), (i, j), (i, j + 1)]))
                    elif (i + 1 < 11 and matrice[i + 1][j] == culoare and i + 2 < 11 and matrice[i + 2][j] == culoare):
                        formatiuni.append((30, [(i + 1, j), (i + 2, j), (i, j - 1), (i, j), (i, j + 1)]))
                if (matrice[i - 1][j] == culoare and matrice[i][j] == culoare and matrice[i + 1][j] == culoare):
                    if (j - 1 >= 0 and matrice[i][j - 1] == culoare and j - 2 >= 0 and matrice[i][j - 2] == culoare):
                        formatiuni.append((30, [(i, j - 1), (i, j - 2), (i - 1, j), (i, j), (i + 1, j)]))
                    elif (j + 1 < 11 and matrice[i][j + 1] == culoare and j + 2 < 11 and matrice[i][j + 2] == culoare):
                        formatiuni.append((30, [(i, j + 1), (i, j + 2), (i - 1, j), (i, j), (i + 1, j)]))
    return formatiuni


punctaj_total = 0

#elimina numerele din matrice care au fost identificate in formatiuni de orice tip
def eliminare_bomboane(matrice, formatiuni):
    global punctaj_total
    for punctaj, formatiune in formatiuni:
        punctaj_total += punctaj
        for (i, j) in formatiune:
            matrice[i][j] = 0

#se ocupa de coborarea numerele in josul matricei si urcarea zerourilor in sus
def matrice_actualizata(matrice):
    for j in range(11):
        coloana_fara_zero = [matrice[i][j] for i in range(11) if matrice[i][j] != 0]
        zero_count = 11 - len(coloana_fara_zero)
        for i in range(zero_count):
            matrice[i][j] = 0
        for i in range(zero_count, 11):
            matrice[i][j] = coloana_fara_zero[i - zero_count]

#cauta daca exista formatiuni de genul in matrice
def exista_formatiuni(matrice):
    formatiuni_3 = linie_de_3(matrice)
    formatiuni_4 = linie_de_4(matrice)
    formatiuni_5 = linie_de_5(matrice)
    formatiuni_L = linie_forma_L(matrice)
    formatiuni_T = linie_forma_T(matrice)
    return formatiuni_3 + formatiuni_4 + formatiuni_5 + formatiuni_L + formatiuni_T

#aceasta functie se ocupa de inlocuirea dintre 2 bomboane, pentru a se verifica daca se mai creeaza o alta formatiune
def inlocuire_bomboane(matrice, x1, y1, x2, y2):
    matrice[x1][y1], matrice[x2][y2] = matrice[x2][y2], matrice[x1][y1]
    if exista_formatiuni(matrice):
        return True
    matrice[x1][y1], matrice[x2][y2] = matrice[x2][y2], matrice[x1][y1]
    return False

#verifica daca exista posibile interschimbari valide in matrice, care ar crea formatiuni valide din punct de vedere al regulilor
def incercare_interschimbari(matrice):
    nr_interschimbari = 0
    for i in range(11):
        for j in range(11):
            if j < 10 and inlocuire_bomboane(matrice, i, j, i, j + 1):
                nr_interschimbari += 1
                return nr_interschimbari
            if i < 10 and inlocuire_bomboane(matrice, i, j, i + 1, j):
                nr_interschimbari += 1
                return nr_interschimbari
    return nr_interschimbari

#simularea jocului candycrush
def candycrush():
    global punctaj_total
    total_punctaj = 0
    total_interschimbari = 0

    for nr_joc in range(1, 101):
        matrice = creare_matrice()
        punctaj_total = 0
        interschimbari_joc = 0

        print(f"Jocul {nr_joc}:")
        print("Matricea initiala:")
        for rand in matrice:
            print(rand)

        formatiuni_total_3 = 0
        formatiuni_total_4 = 0
        formatiuni_total_5 = 0
        formatiuni_total_L = 0
        formatiuni_total_T = 0

        while exista_formatiuni(matrice):
            formatiuni = exista_formatiuni(matrice)
            interschimbari_joc += incercare_interschimbari(matrice)
            for punctaj, _ in formatiuni:
                if punctaj == 3:
                    formatiuni_total_3 += 1
                elif punctaj == 4:
                    formatiuni_total_4 += 1
                elif punctaj == 5:
                    formatiuni_total_5 += 1
                elif punctaj == 20:
                    formatiuni_total_L += 1
                elif punctaj == 30:
                    formatiuni_total_T += 1

            eliminare_bomboane(matrice, formatiuni)
            matrice_actualizata(matrice)

        print("\nFormatiuni gasite:")
        print(f"Formatiuni de linie de 3: {formatiuni_total_3}")
        print(f"Formatiuni de linie de 4: {formatiuni_total_4}")
        print(f"Formatiuni de linie de 5: {formatiuni_total_5}")
        print(f"Formatiuni de forma L: {formatiuni_total_L}")
        print(f"Formatiuni de forma T: {formatiuni_total_T}")

        print("\nMatricea finala:")
        for rand in matrice:
            print(rand)

        print("Punctaj final:", punctaj_total)
        total_punctaj += punctaj_total
        total_interschimbari += interschimbari_joc
        print("=" * 40)

    # Afisarea mediei
    media_punctajelor = total_punctaj / 100
    media_interschimbarilor = total_interschimbari / 100
    print(f"Media aritmetica a jocurilor: {media_punctajelor:.2f}")
    print(f"Media interschimbarilor de la jocuri: {media_interschimbarilor:.2f}")


#apelarea jocului
candycrush()
