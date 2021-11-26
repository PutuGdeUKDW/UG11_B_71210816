kalimat = input("Masukkan kalimat awal: ")
sisip = input("Masukkan kata untuk disisipkan: ")
index = int(input("Masukkan index: "))

kalimatlist = list(kalimat)
kalimatlist.insert(-index, sisip)
hasil = "".join(kalimatlist)
print (hasil)