so_chan = [] # gán so_chan thành mãng rỗng
for i in range(1,10): # lặp i chạy từ 1 đến 10
    if (i%2==0): # nếu i chia hết cho 2 thì
        so_chan.append(str(i)) # ghi chuỗi vào sau mãng
print(','.join(so_chan)) # in ra số chẵn và cách nhau dấu ,