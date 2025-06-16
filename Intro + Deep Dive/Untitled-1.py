# %%
print("tes!")

# %%
#fundamental
var_int=1
var_float=3.14
var_string="Hello World"
#print
print(var_int)
#print type
print(type(var_float))
print(type(var_string))


# %%

print("var_int =",var_int)
print("var_int = ",var_int,"dan var_float =",var_float)
print("var_int = {} var_float = {}".format(var_int,var_float))
print(f'var_int = {var_int} var_float = {var_float}')

# %%
a=b=c=10
print(a,b,c)

# %%
nama=input("Masukkan nama anda: ")
kota=input("Masukkan kota anda: ")

print("Nama saya",nama)
print("Kota saya",kota)    

# %%
str = "Hello World!"
print(str)
print(str[0])  # H
print(str[2:5])  # llo
print(str[2:])  # llo World
print(str * 2)  # Hello WorldHello World
print(str + "TEST")  # Hello WorldTEST
# List
list1 = [1, 2, 3, 'empat', 'lima', 6.0, True]
print(list1)
print(list1[0:3])




# %%
print(str[0:6])
print(str[6:11])
print(str[6:-1])
print(str[:6])
print(str[6:])  # World!

# %%
print(str.split())
print(str.split()[1])
print(str.split('o'))
print(str.split()[1][:-1])
print(len(str))  # 12
print((str + ' ')*2)

# %%
for huruf in str:
    print(huruf)

# %%
for i in range(1,101,2):
    print(i)
for i in range(2,101,2):
    print(i)

# %%
list2 = ['satu','dua','tiga']
print(len(list2))
for i in range(len(list2)):
    print("Elemen ke-",i+1,"adalah",list2[i])

# %%
dict = {}
dict['one'] = "This is one"
dict[2] = 'This is two'
tinyDict = {'name': 'John', 'code': 6734, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinyDict)
print(tinyDict.keys())
print(tinyDict.values())

# %%
set1= {1, 2, 3, 4, 4}
print(set1)
tup1=(1,2,3,4,4)
print(tup1)
print(tup1[0])  # 1

# %%
a=None
print(bool(a))

# %%
huruf = input("Masukkan huruf: ")
vokal = 'aieuo'
#huruf ='1'
if huruf.isalpha() == False:
    print("Input harus berupa huruf!")
else:
    if huruf in 'aieuo':
        print(f'huruf {huruf} adalah huruf vokal')
    else:
        print(f'huruf {huruf} adalah huruf konsonan')

#style one liner
print(f'huruf{huruf} adalah vokal') if huruf in vokal else print(f'huruf {huruf} adalah konsonan')



# %%
str="Hello World!"
print(len(str))
print(str[11])
for huruf in range(len(str)-1,-1,-1):
    print(str[huruf])


# %%
for i in range(5,-1,-1):
    print(i)

# %%
#match statement
def checkVowel(n):
    match n:
        case 'a':return 'Vowel alphabet'
        case 'e':return 'Vowel alphabet'
        case 'i':return 'Vowel alphabet'    
        case 'o':return 'Vowel alphabet'
        case 'u':return 'Vowel alphabet'
        case _:return 'Consonant alphabet'
print (checkVowel('a'))
print (checkVowel('b'))
print (checkVowel('e'))

# %%
#for loop
words = ["one", "two", "three"]
for x in words:
    print(x)

#while loop
i = 1
while i < 6:
    print(i)
    i += 1

# %%
#break
x=0
while x<10:
    print("x :", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1
print("End")

#continue
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

# %%
#pakai while cetak 1 s/d 10
i=1
while i <=10:
    print(i)
    tanya = input("Lanjutkan? (y/n): ")
    while tanya.lower() not in ['y', 'n','ya','yes','no','tidak']:
        tanya = input("Input tidak valid. Lanjutkan? (y/n): ")
    if tanya.lower() not in ['ya','y','yes']:
        break
    else:
        i += 1

# %%
#nested if statement
var = 100
if var == 100:
    print("The number is equal to 100")
    if var % 2 ==0:
        print("The number is even")
    else:
        print("The number is odd")
elif var ==0:
    print("The number is zero")
else:
    print("The number is negative")

# %%
def hello(nama ='Ira'):
    print(f'Hello {nama}')
hello()
hello('Budi')

def hasil(a,b):
    hasil = a + b
    return hasil

a =hasil(10,20)
print(a)

# %%
sum = lambda a, b: a + b
print("Value of total: ", sum(10, 20))

# %%
a =4
b=0
#hasil = a/b
#print(hasil)
#try except 
try:
    hasil = a / b
    print(hasil)
except ZeroDivisionError:
    print("Error: pembagi tidak boleh nol")

# %%
#num = float(input("Masukkan angka: "))
#print(f'Bilangan yang dimasukkan adalah {num}')
try:
    num = float(input("Masukkan angka: "))
    print(f'Bilangan yang dimasukkan adalah {num}')
except ValueError:
    print("Masukkan bilangan yang valid!")


