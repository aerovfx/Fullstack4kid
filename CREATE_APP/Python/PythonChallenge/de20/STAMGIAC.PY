import math 

def s_vuong():
    a = float(input('nhập độ dài cạnh hình vuông: '))
    s = a*a
    print(s)
def s_tron():
    b = float(input('nhập độ dài bán kính: '))
    p = b*b*3.14
    print(p)
def s_tamgiac():
    c = float(input('nhập độ dài cạnh đáy của tam giác: '))
    d = float(input('nhập độ dài chiều cao: '))
    tg = c*d
    print(tg)
def s_chunhat():
    e = float(input('nhập độ dài chiều dài: '))
    f = float(input('nhập độ dài chiều rộng: '))
    cn = e*f
    print(cn)
def main():
    while True:
        print('\nBảng chọn lệnh')
        print('1. Không làm gì và trở về màn hình')
        print('2. Tính diện tích hình vuông')
        print('3. Tính diện tích hình tròn')
        print('4. Tính diện tích hình tam giác')
        print('5. Tính diện tích hình chữ nhật')

        choice = input('Chọn một lệnh(1-5): ')
        
        if choice == '1':
            break
        elif choice == '2':
            s_vuong()
        elif choice == '3':
            s_tron()
        elif choice == '4':
            s_tamgiac()
        elif choice == '5':
            s_chunhat()
        else:
            print('thông số ko hợp lệ vui lòng nhập lại: ')
            
main()