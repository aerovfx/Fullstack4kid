"""
#In ra các số chẵn với vòng lặp for
n = input("Nhap vao n= ")
s =0 
for i in range(0, int(n)):
    s = s +1
    if s%2 == 0:
        print(s)

"""

#In ra các số lẻ với vòng lặp for
n = input("Nhap vao n= ")
s =0 
for i in range(0, int(n)):
    s = s +1
    if s%2 != 0:
        print(s)