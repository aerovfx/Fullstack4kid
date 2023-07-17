def ngto(n):
    for i in range(2, int(n)-1):
        if (n%i==0): return 0
        if (n%i!=0): return 1
f_in = open('SONGUYENTO.INP','r'); f_out = open('SONGUYENTO.OUT','w')
line = f_in.readline().split()

int_n = [int(x) for x in line] #Tao mang so nguyen tu mang cac chuoi da nhap
nt= ngto(int_n[0])
f_out.write(str(round(nt,0)))
f_in.close(); f_out.close();