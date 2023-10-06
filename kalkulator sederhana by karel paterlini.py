#fungsi penjumlahan
def add(x,y):
    return x+y

#fungsi pengurangan
def subtract(x,y):
    return x-y 
    
#fungsi perkalian
def multiply(x,y):
   return x*y
  
#fungsi pembagian
def divide(x,y):
  return x/y

# menu operasi
print("pilih operasi.")
print("1.jumlah")
print("2.pengurangan")
print("3.kali")
print("4.bagi")

#meminta input dari user
choice=input("masukan pilihan(1/2/3/4):")
num1=int(input("masukkan bilangan pertama:"))
num2=int(input("masukkan bilangan kedua:"))

if choice=='1':
  print(num1,"+",num2,"=",add (num1,num2))
  
elif choice=='2':
  print (num1,"-",num2,"=",subtract(num1,num2))
  
elif choice=='3':
  print(num1,"*",num2,"=",multiply(num1,num2))
  
elif choice=='4':
  print(num1,"/",num2,"=",divide(num1,num2))
  
else:
  print("input salah")