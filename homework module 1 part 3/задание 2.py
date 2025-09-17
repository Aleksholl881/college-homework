a = int(input())
th = (a//1000)
ha = (a%1000)//100
ds = (a%100)//10
cif = (a%10)
print(th*ha*ds*cif)