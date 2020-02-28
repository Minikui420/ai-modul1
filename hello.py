list = ["Satu", "Dua"]
print(list[0])
print("Hello")

x = 10
y = " Kuda"
z = bool()
print(type(x))
print(type(y))
print(x, y)

a = 4
b = 40
c = a+b
print(a, " + ", b, " = ", c)
string = "{} + {} = {}"
print(string.format(a, b, c))
print(a==b)
if a > b:
    print(z)


def myFunc():
    print(list[1], y)

myFunc()

s = "Nyamuk"
print(s[0:3])
print(s[3:6])
print(len(s))
print(s.strip())
print(s.lower())
print(s.upper())

anim = s + y
print(anim)

text = "Aku adalah \"Kuda\" jantan"
just = text.rjust(20, "0") #kalimat tidak bisa menggunakan fingsi rjust()
print(just)

txt = "banana" #kata bisa menggunakan fingsi rjust()

xy = txt.rjust(20, "=")

print(xy)

print("Selesai")






