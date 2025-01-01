4️⃣ Giai đoạn 4: Hàm và quản lý bộ nhớ (2-3 tuần)
Hàm:
Cú pháp định nghĩa và gọi hàm.
Tham số và giá trị trả về.
Biến cục bộ và biến toàn cục.
Quản lý bộ nhớ:
Con trỏ (pointers), con trỏ và mảng.
Truy xuất địa chỉ của biến (&), con trỏ hàm.
Quản lý bộ nhớ động (new, delete).
Bài tập:
Viết chương trình tính giai thừa, đệ quy tính Fibonacci.
Quản lý bộ nhớ động cho mảng sinh viên.
----------------
Giáo trình: Hàm và Quản lý Bộ nhớ trong C++

Mục tiêu
	•	Hiểu và sử dụng hàm trong C++: cú pháp, tham số, giá trị trả về, biến cục bộ và toàn cục.
	•	Làm quen với con trỏ, truy xuất địa chỉ biến, và con trỏ hàm.
	•	Quản lý bộ nhớ động bằng từ khóa new và delete.
	•	Giải quyết bài tập thực hành: tính giai thừa, đệ quy Fibonacci, và quản lý bộ nhớ động cho danh sách sinh viên.

    Tuần 1: Hàm

1. Cú pháp định nghĩa và gọi hàm
	•	Cú pháp định nghĩa:
    kiểu_dữ_liệu tên_hàm(danh_sách_tham_số) {
    // Thân hàm
    return giá_trị;
}
	•	Ví dụ cơ bản:
    #include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 10, y = 20;
    cout << "Tổng: " << add(x, y) << endl;
    return 0;
}
2. Tham số và giá trị trả về
	•	Tham số:
	•	Tham chiếu: Truyền địa chỉ, thay đổi giá trị ban đầu.
	•	Tham trị: Sao chép giá trị.
	•	Ví dụ truyền tham chiếu:
    #include <iostream>
using namespace std;

void increment(int& x) {
    x++;
}

int main() {
    int num = 10;
    increment(num);
    cout << "Giá trị sau khi tăng: " << num << endl;
    return 0;
}
3. Biến cục bộ và biến toàn cục
	•	Biến cục bộ: Chỉ tồn tại trong phạm vi hàm.
	•	Biến toàn cục: Được khai báo ngoài các hàm, tồn tại suốt chương trình.
	•	Ví dụ:
    #include <iostream>
using namespace std;

int globalVar = 10; // Biến toàn cục

void display() {
    int localVar = 20; // Biến cục bộ
    cout << "Global: " << globalVar << ", Local: " << localVar << endl;
}

int main() {
    display();
    return 0;
}

Tuần 2: Quản lý Bộ nhớ

1. Con trỏ (pointers)
	•	Khai báo con trỏ:
    kiểu_dữ_liệu* tên_con_trỏ;
    •	Ví dụ:
    #include <iostream>
using namespace std;

int main() {
    int a = 10;
    int* p = &a; // Con trỏ trỏ đến địa chỉ của a
    cout << "Địa chỉ của a: " << p << endl;
    cout << "Giá trị của a: " << *p << endl; // Giá trị tại địa chỉ
    return 0;
}
2. Con trỏ và mảng
	•	Ví dụ:
    #include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int* p = arr;
    for (int i = 0; i < 5; i++) {
        cout << *(p + i) << " "; // Duyệt mảng qua con trỏ
    }
    return 0;
}
3. Con trỏ hàm
	•	Ví dụ:
    #include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int (*funcPtr)(int, int) = add; // Con trỏ hàm
    cout << "Kết quả: " << funcPtr(5, 10) << endl;
    return 0;
}
4. Quản lý bộ nhớ động (new, delete)
	•	Cấp phát bộ nhớ động:
    int* p = new int(10); // Cấp phát cho một số nguyên
    	Giải phóng bộ nhớ:
        #include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhập số phần tử: ";
    cin >> n;

    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    delete[] arr; // Giải phóng bộ nhớ
    return 0;
}
Tuần 3: Bài tập thực hành

1. Tính giai thừa
	•	Yêu cầu: Viết hàm tính giai thừa của một số.
	•	Gợi ý:
    #include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    cout << "Nhập số: ";
    cin >> n;
    cout << "Giai thừa: " << factorial(n) << endl;
    return 0;
}

2. Đệ quy tính Fibonacci
	•	Yêu cầu: Viết hàm đệ quy tính số Fibonacci thứ n.
	•	Gợi ý:
    #include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    cout << "Nhập số: ";
    cin >> n;
    cout << "Số Fibonacci thứ " << n << " là: " << fibonacci(n) << endl;
    return 0;
}
3. Quản lý bộ nhớ động cho danh sách sinh viên
	•	Yêu cầu:
	•	Nhập danh sách sinh viên gồm: ID, tên, tuổi.
	•	Dùng con trỏ để quản lý mảng sinh viên.
	•	Hiển thị danh sách sinh viên.
	•	Gợi ý:
    #include <iostream>
#include <string>
using namespace std;

struct Student {
    int id;
    string name;
    int age;
};

int main() {
    int n;
    cout << "Nhập số sinh viên: ";
    cin >> n;

    Student* students = new Student[n];
    for (int i = 0; i < n; i++) {
        cout << "Nhập ID: ";
        cin >> students[i].id;
        cin.ignore(); // Bỏ qua ký tự xuống dòng
        cout << "Nhập tên: ";
        getline(cin, students[i].name);
        cout << "Nhập tuổi: ";
        cin >> students[i].age;
    }

    cout << "\nDanh sách sinh viên:\n";
    for (int i = 0; i < n; i++) {
        cout << "ID: " << students[i].id << ", Tên: " << students[i].name << ", Tuổi: " << students[i].age << endl;
    }

    delete[] students; // Giải phóng bộ nhớ
    return 0;
}
Tài liệu tham khảo
	1.	C++ Functions Documentation https://cplusplus.com/doc/tutorial/functions/
	2.	Pointers in C++ https://cplusplus.com/doc/tutorial/pointers/