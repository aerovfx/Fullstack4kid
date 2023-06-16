Bài tập Python cơ bản lớp 10
sieusale.daySIEUSALE.DAY15/02/2023LẬP TRÌNH, CÔNG NGHỆ, PYTHON, TỔNG HỢP

Bài viết này cung cấp một số bài tập Python cơ bản giúp các bạn bước đầu làm quen với ngôn ngữ lập trình Python về cách nhập dữ liệu, in kết quả ra màn hình, cách sử dụng các hàm số học chuẩn, câu lệnh điều kiện if, câu lệnh vòng lặp for,…

Mời bạn tham khảo thêm 100+ Bài tập Python cơ bản có lời giải.

1. Nhập xuất cơ bản

Bài 1. Viết chương trình xuất ra màn hình nhiệt độ (oK) tương ứng khi nhập vào nhiệt độ (oC)?

# Nhập nhiệt độ Celsius từ người dùng
celsius = float(input("Nhập nhiệt độ Celsius: "))
# Chuyển đổi nhiệt độ từ Celsius sang Kelvin
kelvin = celsius + 273.15
# Xuất ra màn hình nhiệt độ Kelvin tương ứng
print("Nhiệt độ tương ứng là:", kelvin, "K")
Bài 2. Viết chương nhập vào 2 số nguyên dương m và n (m>n), hãy in ra màn hình phần nguyên và phần dư của m chia cho n?


# Nhập vào 2 số nguyên dương m và n
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n (n < m): "))
# Tính phần nguyên và phần dư của m chia n
div = m // n
mod = m % n
# In kết quả ra màn hình
print("Kết quả phép chia m/n là:", div, "với phần dư là:", mod)
Bài 3. Viết chương trình Python nhập vào độ dài 2 cạnh của hình chữ nhật, tính chu vi và diện tích hình chữ nhật đó.


#chu vi, dien tich hcn
a = float(input('Nhập độ dài cạnh thứ nhất: '))
b = float(input('Nhập độ dài cạnh thứ hai: '))
cv = (a+b)*2
dt = a*b
print('Chu vi = {0}'.format(cv))
print('Dien tich = {0}'.format(dt))
Bài 4. Viết chương trình Python nhập vào bán kính của hình tròn, tính chu vi và diện tích hình tròn đó.


# chu vi, dien tich hinh tron
r = float(input('Nhập bán kính hình tròn: '))
cv = 2*r*3.14
dt = r*r*3.14
print('Chu vi = {0}'.format(cv))
print('Dien tich = {0}'.format(dt))
Bài 5. Viết chương trình Python nhập vào ba số a,b,c bất kì. Kiểm tra xem 3 số đó có thể  là độ dài ba cạnh tam giác hay không, nếu  không  thì in  ra màn  hình  ‘ Không tạo thành tam giác’. Ngược lại, tính chu vi và diện tích tam giác đó.


#kiểm tra tam giac, chu vi, diện tích tam giác
import math
a = float(input('Nhập độ dài cạnh thứ nhất: '))
b = float(input('Nhập độ dài cạnh thứ hai: '))
c = float(input('Nhập độ dài cạnh thứ ba: '))
if a+b>c and a+c>b and b+c>a:
   cv = a+b+c
   p = (a+b+c)/2
   dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
   print('Chu vi = {0}'.format(cv))
   print('Dien tich = {0}'.format(dt))
else: print('Không tạo thành tam giác')

Bài 6. Viết chương trình nhập ba số nguyên dương a, b, h từ bàn phím lần lượt là độ dài đáy lớn, đáy bé và chiều cao của một hình thang. Tính diện tích hình thang và in kết quả ra màn hình.


# Nhập ba số nguyên dương a, b, h từ bàn phím
a = int(input("Nhập độ dài đáy lớn a: "))
b = int(input("Nhập độ dài đáy bé b: "))
h = int(input("Nhập chiều cao h: "))
# Tính diện tích hình thang
area = (a + b) * h / 2
# In kết quả ra màn hình
print("Diện tích hình thang là:", area)
2. Cấu trúc rẽ nhánh

Bài 1: Viết chương trình nhập vào số nguyên dương n, kiểm tra và xuất ra màn hình n là số chẵn hay số lẻ?


n = int(input("Nhap vao mot so nguyen duong: "))
if n % 2 == 0:
    print(n, "la so chan")
else:
    print(n, "la so le")
Trong đoạn code trên, hàm input() được sử dụng để nhập vào một chuỗi từ bàn phím và sau đó hàm int() được sử dụng để chuyển chuỗi đó thành một số nguyên. Lệnh điều kiện if-else được sử dụng để kiểm tra xem n có chia hết cho 2 hay không, nếu có thì n là số chẵn, ngược lại thì n là số lẻ. Sau đó, kết quả được in ra trên màn hình bằng cách sử dụng hàm print().


Ví dụ:


Nhap vao mot so nguyen duong: 5
5 la so le
Nhap vao mot so nguyen duong: 6
6 la so chan
Bài 2: Cho biểu thức f(x,y)=3*sin(x)+4*cos(x). Viết chương trình tính giá trị của biểu thức f(x,y) tại x, y nhập vào từ bàn phím.


Để tính giá trị của biểu thức f(x, y) = 3*sin(x) + 4*cos(x) tại x, y nhập vào từ bàn phím trong Python, ta có thể sử dụng thư viện math để tính toán các hàm sin và cos. Cụ thể, ta có thể viết mã nguồn như sau:


import math
x = float(input("Nhập giá trị x: "))
y = float(input("Nhập giá trị y: "))
result = 3 * math.sin(x) + 4 * math.cos(y)
print("Giá trị của biểu thức f(x, y) là:", result)
Bài 3: Viết chương trình nhập vào năm bất kỳ (ví dụ 2023), hãy cho biết năm đó có phải năm nhuận hay không?

year = int(input("Nhập vào một năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "là năm nhuận")
else:
    print(year, "không phải là năm nhuận")
Bài 4: Em hãy viết đoạn chương trình để xuất ra màn hình xếp loại học lực của học sinh theo giá trị điểm của học sinh?

Để xếp loại học lực của học sinh dựa trên giá trị điểm của học sinh, ta có thể sử dụng các quy tắc sau:

Nếu điểm trung bình của học sinh >= 9.0, xếp loại học sinh là “Xuất sắc”.
Nếu điểm trung bình của học sinh >= 8.0 và < 9.0, xếp loại học sinh là “Giỏi”.
Nếu điểm trung bình của học sinh >= 7.0 và < 8.0, xếp loại học sinh là “Khá”.
Nếu điểm trung bình của học sinh >= 5.0 và < 7.0, xếp loại học sinh là “Trung bình”.
Nếu điểm trung bình của học sinh < 5.0, xếp loại học sinh là “Yếu”.
Ví dụ: Giả sử ta có điểm trung bình của học sinh là 8.5. Kết quả xếp loại học lực của học sinh đó là “Giỏi”.


Dưới đây là mã nguồn Python để xác định xếp loại học lực của học sinh dựa trên giá trị điểm của học sinh:


diem_trung_binh = float(input("Nhập vào điểm trung bình của học sinh: "))
if diem_trung_binh >= 9.0:
    print("Xuất sắc")
elif diem_trung_binh >= 8.0:
    print("Giỏi")
elif diem_trung_binh >= 7.0:
    print("Khá")
elif diem_trung_binh >= 5.0:
    print("Trung bình")
else:
    print("Yếu")
Ở đoạn mã trên, ta sử dụng hàm input() để nhập vào giá trị điểm trung bình của học sinh. Sau đó, ta sử dụng lệnh if-elif để kiểm tra giá trị điểm và xác định xếp loại học lực tương ứng. Kết quả sẽ được in ra trên màn hình bằng cách sử dụng hàm print().


Ví dụ:


Nhập vào điểm trung bình của học sinh: 8.5
Giỏi
Bài 5: Viết chương trình giải phương trình bậc nhất một ẩn ax + b = 0, với hệ số a, b nhập vào từ bàn phím.


# Giải phương trình bậc nhất ax+b=0
a, b= map(float, input('Nhập a, b: ').split())
if a==0 and b!=0: print('Phương trình vô nghiệm')
else:
    if a==0 and b==0: print('Phương trình vô số nghiệm')
    else: print('x= {0}'.format(-b/a))

Bài 6: Viết chương trình giải phương trình bậc hai ax2 + bx + c = 0 (a≠0), với hệ số a, b, c nhập vào từ bàn phím.


import math
a, b, c = map(int, input('Nhập a, b, c: ').split())
d=b**2-4*a*c
if d<0: print('Phương trình vô nghiệm')
else:
    if d==0: print('phuong trinh co nghiem kep')
    else:
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print('x1={0}, x2={1}'.format(x1,x2))

Bài 7: Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, với x, y, a, b, R nhập vào từ bàn phím?


Để kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính R hay không, ta cần tính khoảng cách giữa điểm M và tâm I, sau đó so sánh khoảng cách đó với bán kính R của hình tròn. Nếu khoảng cách nhỏ hơn hoặc bằng bán kính R, thì điểm M nằm trong hoặc trên hình tròn, ngược lại, điểm M nằm ngoài hình tròn.


Dưới đây là mã nguồn Python để thực hiện việc kiểm tra:


import math
# Nhập giá trị x, y, a, b, R từ bàn phím
x = float(input("Nhập giá trị x của điểm M: "))
y = float(input("Nhập giá trị y của điểm M: "))
a = float(input("Nhập giá trị a của tâm I: "))
b = float(input("Nhập giá trị b của tâm I: "))
R = float(input("Nhập giá trị bán kính R của hình tròn: "))
# Tính khoảng cách giữa điểm M và tâm I
distance = math.sqrt((x - a)**2 + (y - b)**2)
# So sánh khoảng cách với bán kính R của hình tròn
if distance <= R:
    print(True)
else:
    print(False)
Bài 8: Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều hay không phải là bộ ba cạnh của tam giác.

Để kiểm tra xem bộ ba số a, b, c có phải là bộ ba cạnh của một loại tam giác nào đó hay không, ta cần kiểm tra các điều kiện sau:

Tổng hai cạnh bất kỳ phải lớn hơn cạnh thứ ba.
Điều kiện của từng loại tam giác cụ thể, ví dụ:
Tam giác thường: Không có đặc điểm gì đặc biệt, tức là không phải tam giác vuông, cân, vuông cân hoặc đều.
Tam giác vuông: Có một góc vuông.
Tam giác cân: Hai cạnh bằng nhau.
Tam giác vuông cân: Vừa có một góc vuông và hai cạnh bằng nhau.
Tam giác đều: Có ba cạnh bằng nhau.
Dưới đây là mã nguồn Python để thực hiện việc kiểm tra:


# Nhập giá trị a, b, c từ bàn phím
a = float(input("Nhập giá trị cạnh a: "))
b = float(input("Nhập giá trị cạnh b: "))
c = float(input("Nhập giá trị cạnh c: "))
# Kiểm tra xem bộ ba số a, b, c có phải là bộ ba cạnh của tam giác hay không
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Đây là bộ ba cạnh của tam giác đều.")
    elif a == b or a == c or b == c:
        if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
            print("Đây là bộ ba cạnh của tam giác vuông cân.")
        else:
            print("Đây là bộ ba cạnh của tam giác cân.")
    elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        print("Đây là bộ ba cạnh của tam giác vuông.")
    else:
        print("Đây là bộ ba cạnh của tam giác thường.")
else:
    print("Đây không phải là bộ ba cạnh của tam giác.")
Bài 9. Viết chương trình tìm số lớn nhất trong ba số nhập vào từ bàn phím.

# Tìm giá trị lớn nhất trong 3 số
a,b,c=map(float,input('Nhập a, b, c: ').split())
max=a
if b>max: max=b
if c>max: max=c
print('So lon nhat= {0}'.format(max))
Bài 10. Viết chương trình tìm số nhỏ nhất trong bốn số nhập vào từ bàn phím.

# Tìm giá trị nhỏ nhất trong 4 số
a,b,c,d=map(float,input('Nhập a, b, c, d: ').split())
min=a
if b<min: min=b
if c<min: min=c
if d<min: min=d
print('Số nhỏ nhất= {0}'.format(min))
Bài 11. Viết chương trình in ra bảng cửu chương.

# In bảng cửu chương
for n in range(2,10):
     for i in range(1,11): print('%1d x %1d = %2d' %(n,i,n*i))
     print()
3. Cấu trúc lặp

Bài 1: Viết chương trình tính tổng các số từ 1 đến n, với n là số nguyên dương nhập vào từ bàn phím.

Để tính tổng các số từ 1 đến n, chúng ta có thể sử dụng vòng lặp for để lặp từ 1 đến n, sau đó cộng dồn các số lại.

n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    tong += i
print("Tổng các số từ 1 đến", n, "là:", tong)
Bài 2: Viết chương trình tính tổng của bình phương các số lẻ từ 1 đến n, với n là số nguyên dương nhập vào từ bàn phím.

Để tính tổng của bình phương các số lẻ từ 1 đến n, chúng ta có thể sử dụng vòng lặp for để lặp từ 1 đến n và kiểm tra từng số có phải là số lẻ hay không. Nếu là số lẻ thì ta tính bình phương của nó và cộng vào tổng.

n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    if i % 2 == 1:
        tong += i**2
print("Tổng bình phương các số lẻ từ 1 đến", n, "là:", tong)
Bài 3: Viết chương trình nhập vào hai số nguyên dương m và n (m>n), xuất ra màn hình ước chung lớn nhất và bội chung nhỏ nhất của 2 số đó.

Để tìm ước chung lớn nhất của 2 số m và n, ta sử dụng thuật toán Euclid như sau:

Đặt a = m, b = n.
Thực hiện phép chia lấy dư a % b và gán a = b, b = phép dư được lấy.
Lặp lại bước 2 cho đến khi b = 0.
Kết quả là giá trị a cuối cùng.
Để tính bội chung nhỏ nhất của 2 số m và n, ta sử dụng công thức:

lcm(m,n) = (m * n) / gcd(m,n)

Trong đó gcd(m,n) là ước chung lớn nhất của m và n.

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
# Tìm ước chung lớn nhất
a = m
b = n
while b != 0:
    r = a % b
    a = b
    b = r
gcd = a
print("Ước chung lớn nhất của", m, "và", n, "là:", gcd)
# Tìm bội chung nhỏ nhất
lcm = (m * n) // gcd
print("Bội chung nhỏ nhất của", m, "và", n, "là:", lcm)
Bài 4: Viết chương trình kiểm tra số nguyên dương n nhập vào từ bàn phím có phải là số hoàn hảo hay không.

Một số nguyên dương n được gọi là số hoàn hảo (số hoàn thiện) nếu tổng các ước của n (không tính chính nó) bằng n. Ví dụ: số 6 là số hoàn hảo vì 6 = 1 + 2 + 3.

Để kiểm tra xem một số nguyên dương n có phải là số hoàn hảo hay không, ta có thể sử dụng thuật toán sau:

Khởi tạo biến sum = 0.
Duyệt từ i = 1 đến n//2 (lấy phần nguyên của n chia 2).
Nếu n chia hết cho i, cộng i vào sum.
Kiểm tra nếu sum = n, thì n là số hoàn hảo. Ngược lại, n không là số hoàn hảo.
n = int(input("Nhập vào số nguyên dương n: "))
sum = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        sum += i
if sum == n:
    print(n, "là số hoàn hảo.")
else:
    print(n, "không là số hoàn hảo.")
Bài 5: Viết chương trình đếm các số nguyên tố nhỏ hơn n, với n là số nguyên dương nhập vào từ bàn phím.

Để đếm số lượng các số nguyên tố nhỏ hơn n, chúng ta cần viết một hàm kiểm tra số nguyên tố và sử dụng vòng lặp để duyệt qua tất cả các số từ 2 đến n-1. Nếu số đó là số nguyên tố, chúng ta sẽ tăng biến đếm lên 1.

Hàm is_prime(number) được sử dụng để kiểm tra xem một số nguyên dương có phải là số nguyên tố hay không. Trong hàm này, chúng ta sử dụng vòng lặp để duyệt qua tất cả các số từ 2 đến căn bậc hai của number để kiểm tra xem có số nào chia hết cho number hay không. Nếu có, number không phải là số nguyên tố và hàm sẽ trả về False. Nếu không, number là số nguyên tố và hàm sẽ trả về True.
Trong chương trình chính, chúng ta nhập vào số nguyên dương n, sau đó khởi tạo biến count bằng 0 để đếm số lượng các số nguyên tố. Chúng ta sử dụng vòng lặp để duyệt qua tất cả các số từ 2 đến n-1. Nếu số đó là số nguyên tố, chúng ta tăng biến count lên 1. Cuối cùng, chúng ta xuất ra màn hình số lượng các số nguyên tố nhỏ hơn n.
def is_prime(number):
    """
    Kiểm tra số nguyên dương number có phải là số nguyên tố hay không.
    Trả về True nếu là số nguyên tố, False nếu không phải.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
n = int(input("Nhập số nguyên dương n: "))
count = 0
for i in range(2, n):
    if is_prime(i):
        count += 1
print(f"Số lượng các số nguyên tố nhỏ hơn {n} là: {count}")
Bài 6: Viết chương trình tính tổng:

S=1/a + 1/(a+1) + 1/(a+2) +…+ 1/(a+n)+…

Cho đến khi 1/(a+n)<0,0001. Với a là số thực bất kỳ nhập vào từ bàn phím

Bài 7. In ra các số chia hết cho 3 từ 1 đến 100.

# Duyệt từ 1 đến 100 và in ra các số chia hết cho 3
for i in range(1, 101):
  if i % 3 == 0:
    print(i)
Bài 8: Nhập vào một số nguyên dương, hãy phân tích số nguyên dương đó thành tích các thừa số nguyên tố.

Khởi tạo một biến result để lưu trữ các thừa số nguyên tố của n.
Khởi tạo biến i bằng 2.
Sử dụng vòng lặp while để lặp lại cho đến khi n bằng 1: a. Kiểm tra n có chia hết cho i không, nếu có thì: i. Thêm i vào biến result. ii. Chia n cho i. b. Nếu n không chia hết cho i, tăng giá trị i lên 1.
Trả về giá trị của biến result.
n = int(input("Nhập số nguyên dương n: "))
result = []
i = 2
while n != 1:
    if n % i == 0:
        result.append(i)
        n = n // i
    else:
        i += 1
print("Các thừa số nguyên tố của", n, "là:", result)
Nếu sử dụng hàm, ta có thể sử dụng thuật toán sau:

Khởi tạo một biến i bằng 2 và một danh sách factors rỗng.
Lặp cho đến khi số đầu vào n là 1: a. Nếu n chia hết cho i, thêm i vào danh sách factors và lấy n chia i. b. Nếu n không chia hết cho i, tăng giá trị của i lên 1.
Trả về danh sách factors.
def prime_factors(n):
    i = 2	

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022

TÀI LIỆU CHỨNG KHOÁN
Tài liệu học đầu tư chứng khoán được tải nhiều nhất năm 2023

TÀI LIỆU CHỨNG KHOÁN
Tài liệu học đầu tư chứng khoán được tải nhiều nhất năm 2023

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022

TÀI LIỆU CHỨNG KHOÁN
Top 1 eBook hướng dẫn đầu tư chứng khoán dành cho người mới
TÌM HIỂU THÊM	

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022
TÌM HIỂU THÊM
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
# Sử dụng hàm prime_factors để phân tích số nguyên dương nhập từ bàn phím
n = int(input("Nhập một số nguyên dương: "))
print("Phân tích thành tích các thừa số nguyên tố của", n, "là:", prime_factors(n))	

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022

TÀI LIỆU CHỨNG KHOÁN
Tải miễn phí ebook học chứng khoán mới nhất năm 2023

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022

TÀI LIỆU CHỨNG KHOÁN
Top 1 eBook hướng dẫn đầu tư chứng khoán dành cho người mới

TÀI LIỆU CHỨNG KHOÁN
Tặng tài liệu tự học chứng khoán tại nhà miễn phí

EBOOK ĐẦU TƯ
Nhận miễn phí ebook đào tạo chứng khoán từ A đến Z tại đây!

EBOOK ĐẦU TƯ
Nhận miễn phí ebook đào tạo chứng khoán từ A đến Z tại đây!
Bài 9. Tính tổng các số từ 1 đến 100.

Tính tổng các số từ 1 đến 100:
# Gán biến sum bằng 0
sum = 0
# Duyệt từ 1 đến 100 và cộng từng số vào sum
for i in range(1, 101):
  sum += i
# In kết quả
print("Tổng các số từ 1 đến 100 là:", sum)
Bài 10. In ra các số chẵn từ 2 đến 100.

# Duyệt từ 2 đến 100 và in ra các số chẵn
for i in range(2, 101, 2):
  print(i)
Bài 11. In ra một tam giác Pascal.



# Khởi tạo một danh sách 2 chiều chứa các số 0
triangle = [[0 for j in range(i+1)] for i in range(10)]
# Gán giá trị cho các phần tử đầu tiên của mỗi hàng bằng 1
for i in range(10):
  triangle[i][0] = 1
# Tính toán các giá trị còn lại trong tam giác
for i in range(1, 10):
  for j in range(1, i+1):
    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
# In ra tam giác
for row in triangle:
  print(" ".join(str(x) for x in row))
Bài 12. Tìm số nguyên tố trong một khoảng từ 2 đến 100.

# Duyệt từ 2 đến 100 và kiểm tra xem số đó có phải là số nguyên tố hay không
for i in range(2, 101):
  is_prime = True
  for j in range(2, i):
    if i % j == 0:
      is_prime = False
      break
  if is_prime:
    print(i)
4. Chương trình con

Bài 1: Viết chương trình có sử dụng hàm lambda để trả về số giây tương ứng với các tham số giờ, phút, giây tương ứng nhập vào từ bàn phím.
Câu 2: Viết chương trình tính tổng sau: S = 1/1! + 1/2! + … + 1/n!, với n là số nguyên dương nhập vào từ bàn phím.

# Tính S=1 + 1/2! + 1/3! + ... + 1/n!
n=int(input('Nhập n: '))
gt=1
s=0
for i in range(1,n+1):
    gt=gt*i
    s+=1/gt
print('s={0}'.format(s))

Bài 3: Viết chương trình để in ra màn hình các số nguyên tố từ 1 đến n, với n là số nguyên dương nhập vào từ bàn phím.
Bài 4: Viết chương trình giải bài toán Tháp Hà Nội. Bài toán Tháp Hà Nội (Tower of Hanoi) là một trò chơi toán học bao gồm 3 cột và với số đĩa nhiều hơn 1. Các đĩa có kích cỡ khác nhau và xếp theo tự tự tăng dần về kích cỡ từ trên xuống: đĩa nhỏ hơn ở trên đĩa lớn hơn. Nhiệm vụ của trò chơi là di chuyển các đĩa có kích cỡ khác nhau sang cột khác sao cho vẫn đảm bảo thứ tự ban đầu của các đĩa: đĩa nhỏ nằm trên đĩa lớn.

5. Kiểu dữ liệu xâu

Bài 1: Viết chương trình “chuẩn hóa” họ và tên khi người dùng nhập vào họ tên bất kỳ từ bàn phím?
Bài 2: Viết chương trình nhập vào một xâu bất kỳ, xuất ra màn hình xâu đó sau khi đã xóa đi các ký tự số?
Bài 3: Viết chương trình nhập vào một xâu bất kỳ, xuất ra màn hình xâu sau khi đã xóa các ký tự giống nhau liền kề.

Bài 4. Đếm số lần xuất hiện của mỗi từ trong một đoạn văn.


EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022
TÌM HIỂU THÊM

TÀI LIỆU CHỨNG KHOÁN
Tài liệu học đầu tư chứng khoán được tải nhiều nhất năm 2023
TÌM HIỂU THÊM

TÀI LIỆU CHỨNG KHOÁN
Chập chững học chứng khoán, tải ngay bộ ebook miễn phí này!
TÌM HIỂU THÊM

TÀI LIỆU CHỨNG KHOÁN
Tài liệu học đầu tư chứng khoán được tải nhiều nhất năm 2023
TÌM HIỂU THÊM

EBOOK ĐẦU TƯ
Tải miễn phí bộ tài liệu học chứng khoán hot nhất năm 2022
TÌM HIỂU THÊM

TÀI LIỆU CHỨNG KHOÁN
Tài liệu học đầu tư chứng khoán được tải nhiều nhất năm 2023
TÌM HIỂU THÊM
# Khởi tạo một đoạn văn
text = "This is a sample text. It has some words in it. We want to count the number of times each word appears in the text."
# Tách các từ trong văn bản thành một danh sách
words = text.split()
# Tạo một từ điển để lưu số lần xuất hiện của từng từ
word_count = {}
# Duyệt qua các từ trong danh sách và tăng số lần xuất hiện của từng từ lên 1
for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
# In kết quả
print("Số lần xuất hiện của từng từ trong văn bản:")
for word, count in word_count.items():
  print(f"{word}: {count}")
6. Kiểu dữ liệu tệp

Bài 1: Viết chương trình tính tổng các số lẻ trong tệp DATA.INP gồm 1 dòng duy nhất chứa dãy các số nguyên dương cách nhau bởi dấu cách. Xuất kết quả ra tệp DATA.OUT
Bài 2: Viết chương trình lọc các số ở văn bản gồm có nhiều dòng trong tệp DATA.INP và xuất ra tệp DATA.OUT gồm dãy các số của từng dòng tương ứng ở trong tệp DATA.INP

7. Kiểu dữ liệu mảng

Bài 1: Viết chương trình nhập vào mảng gồm n số nguyên dương, hãy xuất ra màn hình tổng của các số lẻ trong mảng đó, với n>2
Bài 2: Viết chương trình nhập vào số nguyên dương n, xuất ra màn hình các số nguyên tố nhỏ hơn n, với n>2
Bài 3: Viết chương trình nhập vào dãy các số bất kỳ, tìm số lớn nhất trong dãy số đó và xuất ra màn hình?
Bài 4: Viết chương trình dung phương pháp list comprehension để tạo các list sau:
a) Dãy các số là bội của 3 và nhỏ hơn 100
b) Dãy 10 số chính phương đầu tiên
Bài 5: Viết chương trình nhập vào dãy các số nguyên bất kỳ, kiểm tra và xuất ra màn hình xem dãy số đó có tạo thành cấp số cộng hay không?

Bài 6: Viết chương trình nhập vào dãy gồm n số nguyên cách nhau bởi dấu cách. Sau đó đếm và xuất ra màn hình xem trong dãy vừa nhập có bao nhiêu số nguyên tố.
Bài 7: Viết chương trình nhập vào bàn phím số nguyên dương n, xuất ra màn hình dãy số Fibonaxi. Biết rằng dãy Fibonaxi có dạng như sau: F0 = 1, F1 = 1, Fn = Fn-1 + Fn-2 với n>1
Bài 8: Viết chương trình nhập vào 2 ma trận số nguyên kích thước mxn, sau đó xuất ra màn hình tổng của 2 ma trận đó?
Bài 9: Viết chương trình nhập vào danh sách gồm n người, mỗi người sẽ có các thông tin như: họ và tên, tuổi, giới tính và quê quán. Sau đó xuất ra màn hình thông tin của từng người đã nhập.

Bài 10. Tìm số lớn nhất trong một danh sách số.

# Khởi tạo danh sách số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Gán biến max bằng số đầu tiên trong danh sách
max = numbers[0]
# Duyệt qua các số trong danh sách và cập nhật max nếu có số lớn hơn
for number in numbers:
  if number > max:
    max = number
# In kết quả
print("Số lớn nhất trong danh sách là:", max)
Bài 11. Sắp xếp các số trong một danh sách theo thứ tự tăng dần.

Hướng dẫn. Để sắp xếp các số trong một danh sách theo thứ tự tăng dần, bạn có thể sử dụng một thuật toán sắp xếp như “sắp xếp chọn” (selection sort), “sắp xếp nổi bọt” (bubble sort), “sắp xếp chèn” (insertion sort) hoặc “sắp xếp nhanh” (quick sort).

Dưới đây là một ví dụ về cách sử dụng Python để sắp xếp một danh sách các số theo thứ tự tăng dần bằng thuật toán sắp xếp nhanh:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)
Bài 12. Tìm số lẻ lớn nhất trong một danh sách số.

# Khởi tạo danh sách số
numbers = [5, 3, 1, 8, 4, 9, 2, 7, 6]
# Gán biến max bằng số đầu tiên trong danh sách
max = numbers[0]
# Duyệt qua các số trong danh sách và cập nhật max nếu có số lớn hơn và lẻ
for number in numbers:
  if number > max and number % 2 == 1:
    max = number
# In kết quả
print("Số lớn nhất trong danh sách là:", max)
8. Kiểu dữ liệu từ điển

Bài 1. Viết chương trình nhập vào một xâu bất kỳ, xuất ra màn hình số lần lặp của các từ đơn trong xâu vừa nhập.

Bài 2. Tính tổng các phần tử trong một dictionary.

# Khởi tạo dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Tính tổng các giá trị trong dictionary
total = 0
for value in my_dict.values():
  total += value
# In kết quả
print("Tổng các giá trị trong dictionary là:", total)
Bài 3. Tìm phần tử lớn nhất trong một dictionary.

# Khởi tạo dictionary
my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 3}
# Tìm phần tử lớn nhất trong dictionary
max_key = max(my_dict, key=my_dict.get)
# In kết quả
print("Phần tử lớn nhất trong dictionary là:", max_key)
9. Kiểu dữ liệu xâu

Bài 1: Viết chương trình “chuẩn hóa” họ và tên khi người dùng nhập vào họ tên bất kỳ từ bàn phím?

Bài 2: Viết chương trình nhập vào một xâu bất kỳ, xuất ra màn hình xâu đó sau khi đã xóa đi các ký tự số?

Bài 3: Viết chương trình nhập vào một xâu bất kỳ, xuất ra màn hình xâu sau khi đã xóa các ký tự giống nhau liền kề.

Bài 4. Cho hai xâu s1, s2. Viết đoạn chương trình chèn xâu s1 vào giữa s2, tại vị trí len(s2)//2. In kết quả ra màn hình.

Bài 5. Viết chương trình nhập số học sinh và họ tên học sinh. Sau đó đếm xem trong danh sách có bao nhiêu bạn tên là “Hương”.

Bài 6. Viết chương trình nhập họ tên đầy đủ của người dùng, sau đó in thông báo tên và họ đệm của người đó.

Bài 7. Viết chương trình nhập số tự nhiên n rồi nhập n họ tên học sinh. Sau đó yêu cầu nhập một tên và thông báo số bạn có cùng tên trong lớp.

Bài 8. Đếm số lần xuất hiện của từng ký tự trong một chuỗi.

Hướng dẫn. Để đếm số lần xuất hiện của từng ký tự trong một chuỗi trong Python, bạn có thể sử dụng một từ điển để lưu trữ số lần xuất hiện của từng ký tự. Sau đó, bạn có thể duyệt qua các ký tự trong chuỗi và tăng số lần xuất hiện của từng ký tự lên 1.

# Khởi tạo chuỗi
my_string = "This is a sample string. It has some characters in it."
# Tạo một từ điển để lưu số lần xuất hiện của từng ký tự
char_count = {}
# Duyệt qua các ký tự trong chuỗi và tăng số lần xuất hiện của từng ký tự lên 1
for char in my_string:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
# In ra màn hình số lần xuất hiện của từng ký tự
print("Số lần xuất hiện của từng ký tự trong chuỗi:")
for char, count in char_count.items():
  print(char, "xuất hiện", count, "lần")
10. Hướng đối tượng

Bài 1. Tạo một lớp Hình chữ nhật (Rectangle) có các thuộc tính chiều dài (length) và chiều rộng (width) và các phương thức tính diện tích (area) và chu vi (perimeter) của hình chữ nhật đó.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
Bài 2. Tạo một lớp Hình tròn (Circle) có thuộc tính bán kính (radius) và phương thức tính diện tích (area) và chu vi (circumference) của hình tròn đó.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def circumference(self):
        return 2 * math.pi * self.radius
Bài 3. Tạo một lớp Điểm (Point) có các thuộc tính x và y và phương thức tính khoảng cách đến điểm khác.

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)
Bài 4. Tạo một lớp Người (Person) có các thuộc tính tên (name), tuổi (age) và địa chỉ (address) và phương thức in ra thông tin của người đó.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
Bài 5. Tạo một lớp Điện thoại di động (MobilePhone) có các thuộc tính tên (name), giá (price) và nhà sản xuất (manufacturer) và phương thức in ra thông tin của điện thoại đó.

class MobilePhone:
    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Manufacturer: {self.manufacturer}")
Bài 6. Tạo một lớp Phân số (Fraction) có hai thuộc tính là tử số (numerator) và mẫu số (denominator) và các phương thức tính toán phép cộng, phép trừ, phép nhân và phép chia giữa các phân số.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __add__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)
    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
Bài 7. Tạo một lớp Mảng (Array) có các thuộc tính là độ dài (length) và các phần tử (elements) và phương thức thêm phần tử (append), lấy phần tử tại vị trí (get) và tính tổng các phần tử (sum).

class Array:
    def __init__(self):
        self.length = 0
        self.elements = []
        
    def append(self, element):
        self.elements.append(element)
        self.length += 1
        
    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        return self.elements[index]
    
    def sum(self):
        return sum(self.elements)
Bài 8. Tạo một lớp Động vật (Animal) có các thuộc tính tên (name), tuổi (age) và màu lông (fur_color) và phương thức in ra thông tin của động vật đó.

class Animal:
    def __init__(self, name, age, fur_color):
        self.name = name
        self.age = age
        self.fur_color = fur_color
        
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Fur color: {self.fur_color}")
Bài 9. Tạo một lớp Học sinh (Student) có các thuộc tính tên (name), tuổi (age), lớp (class_name) và phương thức in ra thông tin của học sinh đó.

class Student:
    def __init__(self, name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name
        
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Class:", self.class_name)
Ở đây, lớp Student có ba thuộc tính là name, age và class_name. Phương thức khởi tạo __init__() được sử dụng để khởi tạo các thuộc tính này khi đối tượng được tạo ra. Phương thức display_info() được sử dụng để in ra thông tin của học sinh, bao gồm tên, tuổi và lớp.

Cách sử dụng lớp Student như sau:

student1 = Student("John", 18, "12A")
student2 = Student("Mary", 17, "11B")
student1.display_info()  # Output: Name: John, Age: 18, Class: 12A
student2.display_info()  # Output: Name: Mary, Age: 17, Class: 11B
Trong ví dụ này, chúng ta tạo hai đối tượng học sinh student1 và student2 với các thuộc tính khác nhau. Sau đó, chúng ta gọi phương thức display_info() của từng đối tượng để in ra thông tin của học sinh đó.

Bài 10. Xây dựng lớp tam giác kế thừa từ lớp đa giác.

Để xây dựng lớp tam giác (Triangle) kế thừa từ lớp đa giác (Polygon), ta có thể định nghĩa lớp Triangle như sau:

class Polygon:
    def __init__(self, sides):
        self.sides = sides
        
    def perimeter(self):
        return sum(self.sides)
class Triangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)
        
    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
Ở đây, lớp Triangle kế thừa từ lớp Polygon bằng cách sử dụng từ khóa super(). Lớp Triangle có thêm phương thức area() để tính diện tích của tam giác, dựa trên công thức Heron.

Cách sử dụng lớp Triangle như sau:

triangle = Triangle([3, 4, 5])
print(triangle.perimeter())  # Output: 12
print(triangle.area())  # Output: 6.0
Trong ví dụ này, chúng ta khởi tạo một đối tượng tam giác với độ dài các cạnh lần lượt là 3, 4 và 5. Sau đó, chúng ta gọi hai phương thức perimeter() và area() của lớp Triangle để tính chu vi và diện tích của tam giác.