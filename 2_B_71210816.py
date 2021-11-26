def check_data_type(data,data2):
    global hasil
    tipe = data2.lower()
    if type(data) == str and tipe == "str":
        hasil = "Jawaban Anda benar"
        return hasil
    
    elif type(data) == int and tipe == "int":
        hasil = "Jawaban Anda benar"
        return hasil
    
    elif type(data) == int:
        hasil = "Jawaban Anda salah, seharusnya adalah: int"
        return hasil

    else:
        hasil = "Jawaban Anda salah, seharusnya adalah: str"
        return hasil

def check(data):
    if data == "Jawaban Anda benar":
        print("True")
    else:
        print("False")

print(check_data_type("Kevin","STr"))
check(hasil)

print(check_data_type("Kevin","str"))
check(hasil)

print(check_data_type(12345,"str"))
check(hasil)

print(check_data_type("9347","int"))
check(hasil)

print(check_data_type(9876,"int"))
check(hasil)