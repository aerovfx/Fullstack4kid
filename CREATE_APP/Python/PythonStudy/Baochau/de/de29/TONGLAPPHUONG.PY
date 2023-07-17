def tonglapphuong(): # hàm kiểm tra tổng lặp phương
    for num in range(100, 1000):
        digit1 = num // 100  # Chữ số hàng trăm
        digit2 = (num % 100) // 10  # Chữ số hàng chục
        digit3 = num % 10  # Chữ số hàng đơn vị

        tlp = digit1 ** 3 + digit2 ** 3 + digit3 ** 3
        if num == tlp:
            print('số amstrong là: ',num)
tonglapphuong()