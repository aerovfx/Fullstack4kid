def phansotoigian(phanso):
    # tach tu va mau so
    tu, mau = phanso.split('/')
    tu = int(tu)
    mau = int(mau)
    
    # tim ucln cua tu va mau so
    ucln = find_ucln(tu,mau)
    # chia tu va mau cho ucln de cho phan so toi gian
    tu_toigian = tu // ucln
    mau_toigian = mau // ucln
    
    # tra ve dang toi gian cua phan so
    phanso_toigian = str(tu_toigian) + '/' + str(mau_toigian)
    return phanso_toigian
def find_ucln(a,b):
    while b!=0:
        a,b = b, a%b
    return a

# nhap phan so tu ban phim
n = input('nhap vao phan so muon toi gian: ')

phanso_toigian = phansotoigian(n)
print('toi gian cua phan so la: ',phanso_toigian)