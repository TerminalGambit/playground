def dec_to_binf(nums):
    intp, decp = str(nums).split(".")
    resultat = bin(int(intp))[2:] + "."
    decp = float("0." + decp)
    while decp > 0.0:
        a = decp * 2 // 1
        b = decp * 2 % 1
        resultat += str(int(a))
        decp = b
    return resultat

def bin_to_dec(bins: str) -> float:
    intp, decp = bins.split(".")
    resultat = int(intp, 2)
    for i in range(len(decp)):
        if decp[i] == '1':
            resultat += 1 / 2 ** (i + 1)
    return resultat


a = bin_to_dec("1001.1001")
print(a)

int("1001.1001", 2)
