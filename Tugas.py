'''
Python dibuat oleh Guido van Rossum, dan dirilis pada tahun 1991.

Python digunakan untuk :
    web development (server-side),
    software development,
    mathematics,
    system scripting.

'''

# 1. menampilkan text pada console menggunakan method print()

print("Hello!")

a = 1
print("a = ", a)

b = 2
c = a+b
print(a, " + ", b, " = ", c)
string = "{} + {} = {}"
print(string.format(a, b, c)) #gunakan method format untuk menampilkan data di tengah string

def garis():
	print()
	print(20*"=")
	print()

garis() # untuk membuat garis


# 2. Penulisan code pada python

#penulisan yang benar
if a == 2:
	print("nilai a : ", a)
else:
	print(False)

'''
Penulisan yang salah :

if a == 2:
print("nilai a : ", a)
else:
print(False)

(harus dengan 'tab' seperti contoh di atas)
'''

garis()


# 3. Variables dan type data

#saat menginisialisasi, python akan secara otomatis mengidentifikasi type data apa yang kita tulis (tergantung velue yang kita berikan)

x = 10
floaat = 1.2
kompleks = 1j
kata = "Hai"

'''
Atau dengan casting :
	x = int(10)
	floaat = float(1.2)
	kata = str("Hai")
'''

# gunakan \" untuk memberi tanda kutip pada string
kalimat = "Saya mengatakan \"SKIP\""
# atau seperti ini :
kalimat2 = 'Teguh mengatakan "AYO!"'
boolean = bool() # jika parameternya dibiarkan kosong, maka defaultnya adalah 'False'

print(x, floaat, kata, kompleks)
print(kata + " Bandung", boolean)
print(kalimat)
print(kalimat2)

# mendapatkan sebuah karakter/lebih dengan indexnya
print(kata[0]) 
print(kalimat[0:5])

# cek type data
print(type(x));
print(type(floaat));
print(type(kompleks));
print(type(kata));

garis()



# 4. Aritmatika

p = 25
y = 2.5
t = 100j
n = 100

# python akan secara otomatis mengkonversi type data
print(p/y, p+y, p*t, p-t)
# pangkat
print(p**y); 
print(n**2)
# mod
print(n%p, n%y);
# membulatkan ke bilangan terkecil
print(n//8)

garis()



# 5. List

saya = "Muhaimin"
myList = [1, 2, 3, 4]
myList2 = ["Aku", "Kamu", "Kita"]
myList3 = [5, "Semua"]
myList4 = [myList, myList2, myList3]

print(myList)
print(myList2)
print(myList3)
print(myList4)

# method append() untuk menambahkan list pada index terakhir
myList4.append(saya) 
print(myList4)

# atau seperti ini :
plus = myList + myList2
print(plus);

# mendapatkan data dari list
print(plus[5]) # return 'kamu'
print(myList[0]) # return 1
print(myList4[1][0]) # return Aku
print(myList4[3]) # return Muhaimin
print(myList4[-1]) # return Muhaimin
print(myList4[3][0]) # return M
print(myList4[1:3]) # return ['Aku', 'Kamu', 'Kita'], [5, 'Semua']
print(myList2[0:2]) # return ['Aku', 'Kamu']

# menghitung jumlah data pada list dengan method len()
print("List 1 : ", len(myList))
print("List 2 : ", len(myList2))
print("List 3 : ", len(myList3))
print("List 4 : ", len(myList4))


# edit list
myList4[3] = "Petrikor" # 'Muhaimin' akan diganti dengan 'Petrikor'
myList4[1][0] = "Urang" # 'Aku' diganti 'Urang'

print(myList4)

# membagi kontent list tapi tidak merubah list induk

arr = [100, 200, 300]
arr2 = [400, 500, 600]

print(arr)
print(arr2)

copy = arr # tidak direkomendasikan seperti ini. Karena jika data copy diubah, data dari arr pun ikut berubah (terasosiasi)
copy[0] = 700 

print(copy)
print(arr) # data arr ikut berubah

# lakukan seperti ini
copy2 = arr2[:] # tambahkan [:]
copy2[0] = 800

print(copy2)
print(arr2) # data tidak ikut berubah 

# Print vertikal
for x in arr2:
	print(x)

garis()



# 6. Dictionaries
'''
List yang indexnya dapat dimanipulasi / atau diubah menjadi string (Mirip assosiative array pada javaScript)
'''

Mahasiswa = {
	"Nama": "Naruto",
	"NIM" : 123,
	"Alamat": "Konoha",
	"Hobi": ["Makan", "Tidur", "Skip"] 
}

print(Mahasiswa)
print(Mahasiswa["Hobi"]) # return ['Makan', 'Tidur', 'Skip']
print(Mahasiswa["Hobi"][1]) # return 'Tidur'

for x in Mahasiswa:
	print(x) # return indext
	print(Mahasiswa[x]) # return value

for x, y in Mahasiswa.items():
	print(x, y) # return both


Dosen = {
	"Matkul": "AI",
	"Kode": 90
}
print(Dosen)

# Tambah index pada Dictionary
Dosen["Alamat"] = "Bandung" 
print(Dosen)

# Hapus index
Dosen.pop("Kode")
print(Dosen)

# copy Dictionaries
Mahasiswa2 = Mahasiswa.copy()
Mahasiswa2["Nama"] = "Kuda"
print(Mahasiswa2);
print(Mahasiswa) # Tidak mengubah Dictionary parent

garis();



# 7. if, elif, else

i = 900
j = 90

if i > j:
	print("i > j")
elif i < j:
	print("i < j")
else:
	print("i == j")

# Ternary operator
result = i if i>j else j
print(result) # result akan bernilai i jika i > j

nilai = 100
nilai = nilai/2 if nilai == 10 else nilai*nilai

print(nilai)



# 8. loop while

l = 0
g = 9
while g >= l:
	print(g)
	g-=1
	if g == 0:
		print("NOL")
		break

k = 0
q = 9
while k <= q:
	k+=1
	if k==9:
		print("Sembilan")
		continue # mengeliminasi angka 9 dan menggantinya dengan dengan kalimat
	print(k)



# 9. for loop

quotes = "Hari ini Budi tidak pergi kuliah"
for i in quotes:
	print(i)

print("Jumlah karakter : ", len(quotes))

for i in range(0, 5):
	for j in range(0, i+1):
		print("*", end=" ")
	print()


for i in range(0, 4):
	for j in range(4, i, -1):
		print("*", end=" ")
	print()

cols = 0
rows = 8
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while cols != (2*i-1):
        print("* ", end="")
        cols = cols + 1
    cols = 0
    print()

 # bikin segi tiga bintang malah lebih pusing dari bahasa lain

garis()


# 10. function
'''
	Struktur kode untuk membuat fungsi pada python :

	def namaFungsi():
		print("Hallo!")

'''

def fungsi():
	print("Ini adalah fungsi")

def functionTambah(num1, num2):
	return num1 + num2

def functionKali(num1, num2):
	return num1 * num2

fungsi()
hasil = functionTambah(2, 3)
print("Hasil dari functionTambah : ", hasil)
hasil2 = functionKali(5, hasil) # functionTambah bisa menjadi argument/parameter untuk functionKali. pun sebaliknya
print("Hasil dari functionKali : ", hasil2)

garis()



# 11. Lambda function

lam = lambda a, b, c : (a * b) / c

print("Lambda : ", lam(10, 2, 5))

garis()



# 11. Class dan Object
'''
	penulisan code :

	class namaClass:

'''

class MyClass:	
	x = "Aku adalah x yang bernilai : "
	y = 10

kelas = MyClass() # instansiasi objek

print(kelas.x, kelas.y)
# print(kelas.__dict__) --> jika diletakkan di sini hanya menamppilkan '{}'

# Merubah velue dari isi class MyClass
kelas.x = "Sembilan :"
kelas.y = 9

print(kelas.__dict__) # method ini hanya dapat digunakan ketika merubah value dari atribut class (atau menambhkan antibut diluar class)
print(kelas.x, kelas.y)

kelas.z = "Hore" # ini juga bisa dilakukan
print(kelas.z)
print(kelas.__dict__,"\n\n")

'''
	class di atas merupakan contoh yang kurang merepresentasikan sebuah class (karena ditulis secara prosedural). maka, gunakan constructor __init__() untuk dapat membedakan antara class di atas dan fungsi dari class sebenarnya yang berorientasi objek
'''

# def __init__(self) --> (magic keyword)
# akan dieksekusi pertama kali ketika objek dari MyClass dibuat. dan keyword 'self' untuk merepresentasikan object yang dibuat dari class tersebut

class MyClassObject:

	countMyClassObject = 0 # untuk menghitung jumlah class yang dibuat

	def __init__(self, x, y):
		self.x = x
		self.y = y
		MyClassObject.countMyClassObject += 1

		print("Construktor dari class myClass")
		
	def functionClass(self):
		print("Ini adalah function dari class myClass")
		print(self.x, self.y)
		print("Jumlah Objek yang dibuat : ", MyClassObject.countMyClassObject, "\n")

# variasi input argument pada class
		
a = "Aku"
b = 10

kelas1 = MyClassObject(a, b)
kelas1.functionClass()

kelas2 = MyClassObject("Kamu", 90)
kelas2.functionClass()

kelas3 = MyClassObject(y="Kita", x=20) # Boleh tidak berurutan, asalkan diinisialisasi
kelas3.functionClass()

print(kelas1.__dict__)
print(kelas2.__dict__)
print(kelas3.__dict__)

garis()


# 12. Inheritance (perwarisan)


class InheritClass(MyClassObject): # masukkan class induk

	def functionInher(self):
		print("Haiii!")



inher = InheritClass("Holla", 2)
inher.functionInher() 
inher.functionClass() # object inher dapat mengakses method/function dari class MyClassObject

garis()

# 13. Modul (Mengimport code dari class lain)
'''
	Saya membuat class lain dengan nama ModuleExample yang berisi :

	def functionInModule():
	print("Function dalam modul")

	animals = ["Kuda", "Kambing", "Guk Guk"]

'''

import ModuleExample

# class dari python
import platform
import datetime

ModuleExample.functionInModule()
ma = ModuleExample.animals

for x in ma:
	print(x)

# atau bisa seperti ini :
from ModuleExample import animals
print(animals[0])


plt = platform.system()
print(plt)

cek = dir(platform)
print("\n\n",cek,"\n\n")

dateNow = datetime.datetime.now()
print(dateNow)
print(dateNow.year) # Tahun
print(dateNow.strftime("%B")) # Bulan
print(dateNow.strftime("%A")) # Hari
print(dateNow.strftime("%d")) # Tanggal
print(dateNow.strftime("%I")) # Jam atau bisa ("%H")


'''
	Saat di run, system akan secara otomatis membuat folder baru bernama __pycache__ yang berisi file dengan ekstensi .pyc

'''

garis()



# 13. JSON

import json

# json --> python

# json :
jsonIdent =  '{"name":"John", "age":30, "city":"New York"}'

# ubah ke python
ident = json.loads(jsonIdent)

for x in ident:
	print(x, ident[x])

print()

# python --> json

# python (Dictionary)
dataPy = {
	"Nama" : "Muhaimin",
	"Kelas" : "A",
	"Nim" : 123
}

# ubah ke json
convData = json.dumps(dataPy)
print(convData, "\n")



'''
	14. install pip : 
--> pip install camelcase
'''

# PC saya --> C:\Users\ASUS\AppData\Local\Programs\Python\Python38\Scripts>pip install camelcase

import camelcase

c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt))



# 15. Try Except

try:
	print(ddd)
except NameError:
	print("Variable belum didefinisikan")
except:
	print("Ada yang error nih")
else:
	print("OKE!")

# variable 'ddd' belum didefinisilan, maka akan keluar pesan "Variable belum didefinisikan" pada console


# 16. User Input

inputName = input("Type something : ")
print("Your type is : " + inputName)



# 17. String formatting

kuant = 2
price = 49
txt = "Harga {} kuda adalah {:.2f} dollar"
print(txt.format(kuant, price))

satu = 1
dua = 2
tiga = 3
kalim = "Martin menghitung {2}, {1}, {0}"
print(kalim.format(satu, dua, tiga)) # --> output dipengatuhi oleh penyusunan variable ini

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

