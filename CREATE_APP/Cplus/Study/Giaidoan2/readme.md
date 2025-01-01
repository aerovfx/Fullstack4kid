2️⃣ Giai đoạn 2: Cấu trúc điều khiển và vòng lặp (2-3 tuần)
Câu lệnh điều kiện:
if, else if, else, toán tử 3 ngôi.
Vòng lặp:
Vòng for, while, do-while.
Cách sử dụng break, continue.
Bài tập:
Tính tổng dãy số, kiểm tra số nguyên tố, in bảng cửu chương.

Giáo trình: Cấu trúc điều khiển và vòng lặp trong C++

Mục tiêu
	•	Hiểu và sử dụng được các câu lệnh điều kiện (if, else if, else, toán tử ba ngôi).
	•	Thành thạo các vòng lặp cơ bản (for, while, do-while).
	•	Biết cách sử dụng từ khóa break và continue trong các vòng lặp.
	•	Giải quyết các bài tập thực hành: tính tổng dãy số, kiểm tra số nguyên tố, in bảng cửu chương.

Tuần 1: Câu lệnh điều kiện

1. Câu lệnh if, else if, else
	•	Cú pháp:
if (điều_kiện) {
    // Thực hiện nếu điều kiện đúng
} else if (điều_kiện_khác) {
    // Thực hiện nếu điều kiện_khác đúng
} else {
    // Thực hiện nếu tất cả các điều kiện sai
}

•	Ví dụ:
#include <iostream>
//us  ing namespace std;

int main() {
    int x = 10;
    if (x > 0) {
        std::cout << "x là số dương" << std::endl;
    } else if (x == 0) {
        std::cout << "x bằng 0" << std::endl;
    } else {
        std::cout << "x là số âm" << std::endl;
    }
    return 0;
}
2. Toán tử ba ngôi (ternary operator)
	•	Cú pháp:
kết_quả = (điều_kiện) ? giá_trị_nếu_đúng : giá_trị_nếu_sai;
	•	Ví dụ:
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    string result = (x % 2 == 0) ? "Chẵn" : "Lẻ";
    cout << "x là số " << result << endl;
    return 0;
}

Tuần 2: Vòng lặp cơ bản

1. Vòng lặp for
	•	Cú pháp:

for (khởi_tạo; điều_kiện; bước_nhảy) {
    // Thực hiện nếu điều kiện đúng
}
	•	Ví dụ:
    #include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        cout << i << " ";
    }
    return 0;
}
2. Vòng lặp while
	•	Cú pháp:
while (điều_kiện) {
    // Thực hiện nếu điều kiện đúng
}
	•	Ví dụ:
    #include <iostream>
using namespace std;

int main() {
    int i = 1;
    while (i <= 10) {
        cout << i << " ";
        i++;
    }
    return 0;
}
3. Vòng lặp do-while
	•	Cú pháp:

do {
    // Thực hiện ít nhất một lần
} while (điều_kiện);
	•	Ví dụ:
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    do {
        cout << i << " ";
        i++;
    } while (i <= 10);
    return 0;
}
4. Cách sử dụng break và continue
	•	break: Dừng vòng lặp ngay lập tức.
	•	continue: Bỏ qua lần lặp hiện tại và tiếp tục với lần lặp tiếp theo.
	•	Ví dụ:
    #include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            continue; // Bỏ qua số 5
        }
        if (i == 8) {
            break; // Thoát vòng lặp
        }
        cout << i << " ";
    }
    return 0;
}
Tuần 3: Bài tập thực hành

1. Tính tổng dãy số
	•	Mô tả: Nhập số n, tính tổng các số từ 1 đến n.
	•	Gợi ý:
#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    cout << "Nhập n: ";
    cin >> n;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    cout << "Tổng từ 1 đến " << n << " là: " << sum << endl;
    return 0;
}
2. Kiểm tra số nguyên tố
	•	Mô tả: Nhập một số n, kiểm tra xem n có phải là số nguyên tố không.
	•	Gợi ý:

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhập số n: ";
    cin >> n;
    bool isPrime = true;

    if (n < 2) {
        isPrime = false;
    } else {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    if (isPrime) {
        cout << n << " là số nguyên tố." << endl;
    } else {
        cout << n << " không phải là số nguyên tố." << endl;
    }
    return 0;
}
3. In bảng cửu chương
	•	Mô tả: In bảng cửu chương từ 2 đến 9.
	•	Gợi ý:
#include <iostream>
using namespace std;

int main() {
    for (int i = 2; i <= 9; i++) {
        cout << "Bảng cửu chương " << i << ":" << endl;
        for (int j = 1; j <= 10; j++) {
            cout << i << " x " << j << " = " << i * j << endl;
        }
        cout << endl;
    }
    return 0;
}
Tài liệu tham khảo
	1.	C++ Loops and Conditions Documentation
    https://cplusplus.com/doc/tutorial/control/
	2.	Sách “Programming in C++” (tác giả Bjarne Stroustrup).