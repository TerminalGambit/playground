#######################################################
#  Automates & Langages  -  L3 I / MI / ST  - 2024/25 #
#  TP 3  - Algorithmes de recherche de motif - II     #
#######################################################

# Boyer-Moore-Horspool Algorithm
###############################

print('### Exercice 1 ###')


# Exercice 1: Dictionary of last occurrences
def dicoDerOcc(motif):
    dico = {}
    for i in range(len(motif)):
        dico[motif[i]] = i
    return dico


# Exercice 2: Boyer-Moore-Horspool search function
def rechercheBMH(motif, texte):
    lm = len(motif)
    lt = len(texte)

    # Step 1: Generate the dictionary of last occurrences
    dico = dicoDerOcc(motif)

    # Step 2: Set up the initial indices for the text and motif
    i = lm - 1
    while i < lt:
        j = lm - 1

        # Step 3: Compare backwards from the end of the pattern
        while j >= 0 and texte[i] == motif[j]:
            i -= 1
            j -= 1

        # Step 4: If the full pattern matches, return the starting index
        if j == -1:
            return i + 1

        # Step 5: If no match, slide the pattern according to the last occurrence table
        i += lm - min(j, dico.get(texte[i], -1) + 1)

    return -1


# Function to read from a file and search for a motif using Boyer-Moore-Horspool
def RechercheBMH(fichier, motif):
    with open(fichier, 'r', encoding='utf-8') as f_in:
        texte = f_in.read()

    position = rechercheBMH(motif, texte)
    if position == -1:
        print(f"Le motif '{motif}' n'apparaît pas dans le fichier {fichier}")
    else:
        print(f"Le motif '{motif}' apparaît en position {position} dans le fichier {fichier}")


# Example usage of Boyer-Moore-Horspool
RechercheBMH('horla.txt', 'Rouen')


# Rabin-Karp Algorithm
#############################

print('### Exercice 3.1 ###')


# Function to convert a string to an integer (used for hashing)
def str2int(s):
    return sum(ord(s[-i]) * 256 ** (i - 1) for i in range(1, len(s) + 1))


# Custom hash function for Rabin-Karp (modulo 101 for simplicity)
def hash(s):
    return str2int(s) % 101


print('### Exercice 3.2 ###')


# Exercice 3: Rabin-Karp search function
def rechercheRK(motif, texte):
    hm = hash(motif)
    lm = len(motif)
    lt = len(texte)

    for i in range(lt - lm + 1):
        # Hash the current substring
        h_text = hash(texte[i:i + lm])

        # If the hash matches, compare the strings character by character
        if h_text == hm:
            if texte[i:i + lm] == motif:
                return i

    return -1


# Function to read from a file and search for a motif using Rabin-Karp
def RechercheRK(fichier, motif):
    with open(fichier, 'r', encoding='utf-8') as f_in:
        texte = f_in.read()

    position = rechercheRK(motif, texte)
    if position == -1:
        print(f"RK : Le motif '{motif}' n'apparaît pas dans le fichier {fichier}")
    else:
        print(f"RK : Le motif '{motif}' apparaît en position {position} dans le fichier {fichier}")


# Example usage of Rabin-Karp
# RechercheRK('horla.txt', 'admirable')


print('### Exercice 4 ###')


# Exercice 4: Amortized hash update function
def update(h, n, s_i, s_j):
    # Calculate the updated hash when moving from s_i to s_j
    return (h - ord(s_i) * 256 ** (n - 1)) * 256 + ord(s_j)

# Uncomment the lines below to test the implementation with your file and motifs
# RechercheBMH('horla.txt', 'Rouen')
# RechercheRK('horla.txt', 'admirable')