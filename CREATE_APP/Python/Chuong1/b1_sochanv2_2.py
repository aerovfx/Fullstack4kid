so = input('nhap vao cac so, cac so cah nhau dau phay: ')
so = so.split(',')

so_chan = []
so_le = []

for i in so:
    i = int(i)
    if i % 2 == 0:
        so_chan.append(str(i))
    else:
        so_le.append(str(i))
print('so chan la: ' , ','.join(so_chan))
print('so le la: ', ','.join(so_le))