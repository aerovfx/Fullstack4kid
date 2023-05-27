https://codeforces.com/contest/1372/problem/B
B. Omkar và Lớp Toán Cuối Cùng
giới hạn thời gian cho mỗi bài kiểm tra 1 giây
giới hạn bộ nhớ cho mỗi bài kiểm tra 256 megabyte
đầu vào đầu vào tiêu chuẩn
đầu ra đầu ra tiêu chuẩn đầu ra
Trong lớp toán cuối cùng của Omkar, anh ấy đã học về bội số chung nhỏ nhất, hoặcLCM
LCM .LCM(a,b) là số nguyên dương nhỏ nhất x cái nào chia hết cho cả hai. 

Omkar, có một tâm trí tò mò đáng khen ngợi, ngay lập tức nghĩ đến một vấn đề liên quan đếnLCM
thao tác: cho một số nguyênn
n
, tìm các số nguyên dươngmột
một
vàb
b
như vậya+b=n
một
+
b
=
n
vàLCM(a,b)
L
C
M
(
một
,
b
)
là giá trị tối thiểu có thể.

Bạn có thể giúp Omkar giải bài toán đầy thử thách lố bịch của anh ấy không?

Đầu vào
Mỗi bài kiểm tra chứa nhiều trường hợp kiểm tra. Dòng đầu tiên chứa số lượng các trường hợp thử nghiệmt
t
(1≤t≤10
1
≤
t
≤
10
). Mô tả các trường hợp thử nghiệm sau đây.

Mỗi trường hợp kiểm tra bao gồm một số nguyên duy nhấtn
n
(2≤n≤109
2
≤
n
≤
10
9
).

Đầu ra
Đối với mỗi trường hợp thử nghiệm, xuất ra hai số nguyên dươngmột
một
vàb
b
, như vậya+b=n
một
+
b
=
n
vàLCM(a,b)
L
C
M
(
một
,
b
)
là mức tối thiểu có thể.

Ví dụ
Bản sao đầu vào
3 4 6 9
Bản sao đầu ra
Số 2 2 Số 3 3 Số 3 6
Lưu ý
Đối với trường hợp thử nghiệm đầu tiên, những con số chúng ta có thể chọn là1,3
1
,
3
hoặc2,2
2
,
2
.LCM(1,3)=3
L
C
M
(
1
,
3
)
=
3
vàLCM(2,2)=2
L
C
M
(
2
,
2
)
=
2
, vì vậy chúng tôi xuất raSố 2 2
2
 
2
.

Đối với trường hợp thử nghiệm thứ hai, những con số chúng ta có thể chọn là1,5
1
,
5
,2,4
2
,
4
, hoặc3,3
3
,
3
.LCM(1,5)=5
L
C
M
(
1
,
5
)
=
5
,LCM(2,4)=4
L
C
M
(
2
,
4
)
=
4
, vàLCM(3,3)=3
L
C
M
(
3
,
3
)
=
3
, vì vậy chúng tôi xuất raSố 3 3
3
 
3
.

Đối với trường hợp thử nghiệm thứ ba,LCM(3,6)=6
L
C
M
(
3
,
6
)
=
6
. Có thể chỉ ra rằng không có cặp số nào khác tính tổng9
9
cái đó có mức thấp hơnLCM
L
C
M
.