prop = ["R", "G", "B", "Y"]
vysledek = [] # Sem budeme ukládat hotové kombinace

def findCombination(proper: list, prefix=[]):
    if len(proper) == 0:
        vysledek.append(prefix) # Máme hotovou celou kombinaci
    else:
        for i in range(len(proper)):
            past = proper.copy()
            item = past.pop(i) # Odstraní a vrátí prvek na indexu i
            findCombination(past, prefix + [item]) # Pošleme zbytek a přidáme prvek k cestě

findCombination(prop)

# Teď jsou všechna data v seznamu 'vysledek'
print(vysledek)