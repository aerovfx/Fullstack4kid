Bài 01: Viết một chương trình Python in ra dãy số Fibonacci

Gợi ý:

Sử dụng đệ quy
Không sử dụng đệ quy
Code mẫu: In dãy số Fibonacci trong Python không sử dụng đệ quy.

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
"""
 * Tính số fibonacci thứ n
 *
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
 """
def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
  
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
  
print("10 số đầu tiên của dãy số Fibonacci: ");
sb = "";
for i in range(0, 10):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)
Kết quả:

10 so dau tien cua day so Fibonacci: 
0 1 1 2 3 5 8 13 21 34 
Bài 02: Viết một chương tình Python kiểm tra số nguyên tố.

Code mẫu:

?
1
2
3
4
5
6
7
8
"""
 * check so nguyen to trong Python
 * 
 * 
 * @param n: so nguyen duong
 * @return 1 la so nguyen so, 
 *         0 khong la so nguyen to
"""
Kết quả:

Cac so nguyen to nho hon 100 la: 
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Bài 03: Viết một chương trình Python tính giai thừa của một số bằng cách không sử dụng đệ quy và có sử dụng đệ quy.

Gợi ý:

Sử dụng đệ quy
Không sử dụng đệ quy
Code mẫu: Tính giai thừa trong Python không sử dụng đệ quy.

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
"""
 * tinh giai thua

 * @param n: so nguyen duong
 * @return giai thua cua so n
"""
def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
  
n = int(input("Nhập số nguyên dương n = "));
print("Giai thừa của", n, "là", tinhgiaithua(n));
Kết quả:

Nhập số nguyên dương n = 10
Giai thừa của 10 là 3628800
Bài 04: Viết một chương trình Python để chuyển đổi số nguyên N sang hệ cơ số B (2 <= B <= 32) bất kỳ.

Code mẫu: Chuyển đối hệ cơ số 10 sang hệ cơ số B

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
"""
# Chuyển đổi số nguyên n sang hệ cơ số b
#
# @author viettuts.vn
# @param n: so nguyen
# @param b: he co so
# @return he co so b
"""
def convert_number(n, b):
    if (n < 0 or b < 2 or b > 16):
        return "";
  
    sb = "";
    m = 0;
    remainder = n;
  
    while (remainder > 0):
        if (b > 10):
            m = remainder % b;
            if (m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return "".join(reversed(sb)); # đảo ngược chuỗi sb
  
n = int(input("Nhập số nguyên dương n = "));
print("Hệ cơ số 2 của số nguyên ", n, "là:", convert_number(n, 2))
print("Hệ cơ số 16 của số nguyên ", n, "là:", convert_number(n, 16))
Kết quả:

Nhập số nguyên dương n = 15
Hệ cơ số 2 của số nguyên  15 là: 1111
Hệ cơ số 16 của số nguyên  15 là: F
2. Bài tập Python cơ bản

Danh sách bài tập:

Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 10 và 200 (tính cả 10 và 200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
Viết một chương trình tính giai thừa của một số nguyên dương n. Với n được nhập từ bàn phím. Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.
Hãy viết chương trình để tạo ra một dictionary chứa (i, i*i), trong đó i là số nguyên từ 1 đến n (bao gồm cả 1 và n), n được nhập từ bàn phím. Sau đó in ra dictionary này ra màn hình. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
Viết chương trình Python giải phương trình bậc 2: ax2 + bx + c = 0.
Viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất (BSCNN) của hai số nguyên dương a và b nhập từ bàn phím.
Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n. Số nguyên dương n được nhập từ bàn phím.
Viết chương trình liệt kê n số nguyên tố đầu tiên trong Python. Số nguyên dương n được nhập từ bàn phím.
Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số trong Python.
Viết chương trình phân tích số nguyên n thành các thừa số nguyên tố trong Python. Ví dụ: 100 = 2x2x5x5.
Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python. Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10
Viết chương trình kiểm tra một số n là số thuận nghịch trong Python. Số nguyên dương n được nhập từ bàn phím.
Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố trong Python. N là số nguyên dương được nhập từ bàn phím.
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
Bài 01:

Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 10 và 200 (tính cả 10 và 200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

Gợi ý:

Sử dụng range(#begin, #end)
Code mẫu:

?
1
2
3
4
5
arr = []
for i in range(10, 201):
    if (i % 7 == 0) and (i % 5 != 0):
        arr.append(str(i))
print (', '.join(arr))
Kết quả:

14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98, 112, 119, 126, 133, 147, 154, 161, 168, 182, 189, 196
Bài 02:

Viết một chương trình tính giai thừa của một số nguyên dương n. Với n được nhập từ bàn phím. Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.

Gợi ý:

Sử dụng đệ quy hoặc vòng lặp để tính giai thừa.
Code mẫu: sử dụng đệ quy

?
1
2
3
4
5
6
7
8
n = int(input("Nhập số cần tính giai thừa: "))
 
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
 
print (giaiThua(n))
Kết quả:

Nhập số cần tính giai thừa: 8
40320
Bài 03:

Hãy viết chương trình để tạo ra một dictionary chứa (i, i*i), trong đó i là số nguyên từ 1 đến n (bao gồm cả 1 và n), n được nhập từ bàn phím. Sau đó in ra dictionary này ra màn hình. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

Gợi ý:

Sử dụng vòng lặp for để lặp i từ 1 đến n.
Code mẫu:

?
1
2
3
4
5
6
7
n = int(input("Nhập số nguyên dương n = "))
 
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
 
print (d)
Kết quả:

Nhập số nguyên dương n = 8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Bài 04:

Viết chương trình giải phương trình bậc 2: ax2 + bx + c = 0.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
import math
 
"""
# Giải phương trình bậc 2: ax2 + bx + c = 0
# @param a: hệ số bậc 2
# @param b: hệ số bậc 1
# @param c: số hạng tự do
"""
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b));
        return;
 
    # tính delta
    delta = b * b - 4 * a * c;
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");
 
# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "));
b = float(input("Nhập hệ số bậc 1, b = "));
c = float(input("Nhập hằng số tự do, Python = "));
# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)
Kết quả:

Nhập hệ số bậc 2, a = 2
Nhập hệ số bậc 1, b = 1
Nhập hằng số tự do, Python = -1
Phương trình có 2 nghiệm là: x1 =  0.5  và x2 =  -1.0
Bài 05:

Viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất (BSCNN) của hai số nguyên dương a và b nhập từ bàn phím.

Gợi ý:

Sử dụng giải thuật Euclid.
Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
"""
 * Tìm ước số chung lớn nhất (USCLN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return USCLN của a và b
"""
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
 
"""
 * Tìm bội số chung nhỏ nhất (BSCNN)
 * 
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return BSCNN của a và b
"""
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
Kết quả:

Nhập số nguyên dương a = 15
Nhập số nguyên dương b = 20
Ước số chung lớn nhất của 15 và 20 là: 5
Bội số chung nhỏ nhất của 15 và 20 là: 60
Bài 06:

Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n. Số nguyên dương n được nhập từ bàn phím.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
import math
 
"""
 * check so nguyen to
 * 
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return true la so nguyen so, 
 *         false khong la so nguyen to
"""
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:");
sb = "";
if (n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " ";
    i = i + 2;
print(sb);
Kết quả:

Nhập số nguyên dương n = 100
Tất cả các số nguyên tố nhỏ hơn 100 là:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Bài 07:

Viết chương trình liệt kê n số nguyên tố đầu tiên trong Python. Số nguyên dương n được nhập từ bàn phím.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
import math
 
"""
 * check so nguyen to
 * 
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return true la so nguyen so, 
 *         false khong la so nguyen to
"""
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
n = int(input("Nhập số nguyên dương n = "));
print (n, "Số nguyên tố đầu tiên là:");
dem = 0; # đếm số số nguyên tố
i = 2;   # tìm số nguyên tố bắt dầu từ số 2
sb = "";
while (dem < n):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " ";
        dem = dem + 1;
    i = i + 1;
print(sb);
Kết quả:

Nhập số nguyên dương n = 10
10 Số nguyên tố đầu tiên là:
2 3 5 7 11 13 17 19 23 29 
Bài 8:

Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số trong Python.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
import math
 
"""
 * check so nguyen to
 * 
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return true la so nguyen so, 
 *         false khong la so nguyen to
"""
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
print ("Liệt kê tất cả số nguyên tố có 5 chữ số:");
dem = 0;
for i in range(10001, 99999):
    if (isPrimeNumber(i)):
        print(i);
        dem = dem + 1;
print("Tổng các số nguyên tố có 5 chữ số là:", dem);
Kết quả:

Liệt kê tất cả số nguyên tố có 5 chữ số:
10007
10009
10037
...
99971
99989
99991
Tổng các số nguyên tố có 5 chữ số là: 8363
Bài 9:

Viết chương trình phân tích số nguyên n thành các thừa số nguyên tố trong Python. Ví dụ: 100 = 2x2x5x5.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
"""
 * Phân tích số nguyên thành tích các thừa số nguyên tố
 *
 * @param positiveInt
 * @return
"""
def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    # phân tích
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers;
 
n = int(input("Nhập số nguyên dương n = "));
# phân tích số nguyên dương n
listNumbers = phanTichSoNguyen(n);
size = len(listNumbers);
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listNumbers[i]) + " x ";
sb = sb + str(listNumbers[size-1]);
# in kết quả ra màn hình
print("Kết quả:", n, "=", sb);
Kết quả:

Nhập số nguyên dương n = 100
Kết quả: 100 = 2 x 2 x 5 x 5
Bài 10:

Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python. Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
""""
 * Tính tổng của các chữ số của một số nguyên dương n
 *
 * @param n: số nguyên dương
 * @return
"""
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));
Kết quả:

Nhập số nguyên dương n = 1234
Tổng các chữ số của 1234 là 10
Bài 11:

Viết chương trình kiểm tra một số n là số thuận nghịch trong Python. Số nguyên dương n được nhập từ bàn phím.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
"""
 * Kiểm tra số thuận nghịch
 *
 * @param n: số nguyên dương
 * @return true là số thuận nghịch
 *         false không là số thuận nghịch
"""
def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
m = int(input("Nhập số nguyên dương m = "));
print("Tổng các chữ số của", m , "là", isThuanNghich(m));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
Kết quả:

Nhập số nguyên dương n = 123321
Tổng các chữ số của 123321 là True
Nhập số nguyên dương m = 123451
Tổng các chữ số của 123451 là False
Bài 12:

Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố trong Python. N là số nguyên dương được nhập từ bàn phím.

Code mẫu:

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
import math
 
"""
 * Tính số fibonacci thứ n
 *
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
"""
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
 
"""
 * check so nguyen to
 * 
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return true la so nguyen so, 
 *         false khong la so nguyen to
"""
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
 
"""
 *  Chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố.
 *  Với n được nhập từ bàn phím.
 *  
 * @author viettuts.vn
"""
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số fibonacci nhỏ hơn", n, "và nguyên tố:");
i = 0;
fin = fibonacci(i);
while(fin < n):
    fin = fibonacci(i);
    if (isPrimeNumber(fin)):
        print(fin)
    i = i + 1;
Kết quả:

Nhập số nguyên dương n = 100
Tất cả các số fibonacci nhỏ hơn 100 và nguyên tố:
2
3
5
13
89
Bài 13:

Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.

Ví dụ: Đầu vào được cung cấp là 34, 67, 55, 33, 12, 98 thì đầu ra là:

['34', '67', '55', '33', '12', '98'] 
('34', '67', '55', '33', '12', '98')

Gợi ý:

Viết lệnh yêu cầu nhập vào các giá trị sau đó dùng quy tắc chuyển đổi kiểu dữ liệu để hoàn tất.
Code mẫu:

?
1
2
3
4
5
values=input("Nhập vào các giá trị: ")
l=values.split(",")
t=tuple(l)
print (l)
print (t)
Kết quả:

Nhập vào các giá trị: 34, 67, 55, 33, 12, 98
['34', ' 67', ' 55', ' 33', ' 12', ' 98']
('34', ' 67', ' 55', ' 33', ' 12', ' 98')