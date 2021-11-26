def akarKubik(data):
    X = data**(1./3.)
    return X
def genap(data):
    if data %2 ==0:
        akar= akarKubik(data)
        return akar
    else:
        data = ("ganjil")
        return data
angka1  =90
angka2 = 21
angka3 =298745197907834587289340
print(genap(angka1))
print(genap(angka2))
print(genap(angka3))