def dttamgiac(a,b,c):
   if a*a == (b*b) + (c*c):  return b*c/2
   if b*b == a*a + c*c : return a*c/2
   if c*c == b*b + a*a : return b*a/2
   
   return -1
f_in = open("TAMGIAC.INP","r"); f_out = open("TAMGIAC.OUT","w")
line = f_in.readline().split()

int_a = [int(x) for x in line] #Tao mang so nguyen tu mang cac chuoi da nhap
S= dttamgiac(int_a[0], int_a[1], int_a[2])
f_out.write(str(round(S,0)))
f_in.close(); f_out.close();