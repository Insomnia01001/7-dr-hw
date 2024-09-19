ism = input("ismingizni kiriting  ")
ism_reverse= ism[::-1]
if ism == ism_reverse:
    print(True)
else:
    print(False)

password = int(input("password kiriting  "))
if password == 12345:
    print(True)
else:
    print(False)

son = int(input("son kiriting "))
if son%2==0:
    print(True)
else:
    print(False)