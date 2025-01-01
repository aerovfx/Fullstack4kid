
3️⃣ Giai đoạn 3: Mảng và chuỗi (2-3 tuần)
Mảng:
Mảng 1 chiều, 2 chiều.
Duyệt mảng, sắp xếp, tìm kiếm (Bubble sort, Linear search...).
Chuỗi (String):
Nhập, xuất chuỗi, thao tác với chuỗi (nối chuỗi, tách chuỗi...).
Thư viện string trong C++.
Bài tập:
Xây dựng chương trình quản lý danh sách sinh viên.
Đếm số từ trong chuỗi, tìm kiếm từ trong chuỗi.

------------
Giáo trình: Mảng và Chuỗi trong C++

Mục tiêu
	•	Hiểu và sử dụng được mảng 1 chiều và 2 chiều trong C++.
	•	Thành thạo các thuật toán cơ bản trên mảng: duyệt mảng, sắp xếp, tìm kiếm.
	•	Làm quen với chuỗi trong C++, các thao tác cơ bản với chuỗi, và thư viện string.
	•	Giải quyết các bài tập thực hành: quản lý danh sách sinh viên, đếm từ, tìm kiếm từ trong chuỗi.

Tuần 1: Mảng

1. Mảng 1 chiều
	•	Cú pháp khai báo:
kiểu_dữ_liệu tên_mảng[kích_thước];
	•	Ví dụ:
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
2. Mảng 2 chiều
	•	Cú pháp khai báo:
kiểu_dữ_liệu tên_mảng[số_hàng][số_cột];

#include <iostream>
using namespace std;

int main() {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
3. Duyệt mảng
	•	Ví dụ duyệt mảng 1 chiều:
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
4. Sắp xếp mảng (Bubble Sort)
	•	Thuật toán:
Duyệt qua mảng, hoán đổi các phần tử nếu chúng không theo thứ tự.
	•	Ví dụ:

#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
5. Tìm kiếm (Linear Search)
	•	Thuật toán:
Duyệt qua mảng để tìm phần tử khớp với giá trị cần tìm.
	•	Ví dụ:
#include <iostream>
using namespace std;

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int x = 30;
    int index = linearSearch(arr, 5, x);
    if (index != -1) {
        cout << "Phần tử tìm thấy ở vị trí: " << index << endl;
    } else {
        cout << "Không tìm thấy phần tử." << endl;
    }
    return 0;
}
uần 2: Chuỗi

1. Khai báo và nhập/xuất chuỗi
	•	Cách sử dụng:
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Nhập chuỗi: ";
    getline(cin, str); // Nhập chuỗi có dấu cách
    cout << "Chuỗi vừa nhập: " << str << endl;
    return 0;
}
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cout << "Nhập chuỗi: ";
    getline(cin, str); // Nhập chuỗi có dấu cách
    cout << "Chuỗi vừa nhập: " << str << endl;
    return 0;
}
2. Thao tác cơ bản với chuỗi
	•	Nối chuỗi:
string str1 = "Hello";
string str2 = " World";
string result = str1 + str2;
	•	Tách chuỗi (dựa trên chỉ số):
string subStr = str.substr(0, 5); // Lấy 5 ký tự đầu tiên
	•	Tìm chuỗi con:
    size_t pos = str.find("World");
if (pos != string::npos) {
    cout << "Tìm thấy tại vị trí: " << pos << endl;
}

3. Thư viện string
	•	Một số hàm thường dùng:
	•	length() hoặc size(): Độ dài chuỗi.
	•	append(): Nối chuỗi.
	•	erase(): Xóa một phần chuỗi.
	•	find(): Tìm chuỗi con.

Tuần 3: Bài tập thực hành

1. Xây dựng chương trình quản lý danh sách sinh viên
	•	Yêu cầu:
	•	Tạo lớp Student với thuộc tính: id, name, age.
	•	Lưu danh sách sinh viên trong mảng.
	•	Hiển thị danh sách sinh viên.
	•	Gợi ý:
    #include <iostream>
#include <vector>
using namespace std;

struct Student {
    int id;
    string name;
    int age;
};

void displayStudents(vector<Student>& students) {
    for (auto& student : students) {
        cout << "ID: " << student.id << ", Name: " << student.name << ", Age: " << student.age << endl;
    }
}

int main() {
    vector<Student> students = {
        {1, "Alice", 20},
        {2, "Bob", 21},
        {3, "Charlie", 22}
    };

    displayStudents(students);
    return 0;
}
2. Đếm số từ trong chuỗi
	•	Yêu cầu:
Đếm số từ trong chuỗi, mỗi từ cách nhau bởi một khoảng trắng.
	•	Gợi ý:
#include <iostream>
#include <sstream>
using namespace std;

int countWords(string str) {
    stringstream ss(str);
    string word;
    int count = 0;
    while (ss >> word) {
        count++;
    }
    return count;
}

int main() {
    string str = "Xin chào các bạn";
    cout << "Số từ trong chuỗi: " << countWords(str) << endl;
    return 0;
}
3. Tìm kiếm từ trong chuỗi
	•	Yêu cầu:
Nhập chuỗi và từ cần tìm, xác định từ đó có trong chuỗi không.
	•	Gợi ý:
    #include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "Hello World";
    string word = "World";

    size_t pos = str.find(word);
    if (pos != string::npos) {
        cout << "Tìm thấy từ \"" << word << "\" tại vị trí: " << pos << endl;
    } else {
        cout << "Không tìm thấy từ \"" << word << "\"" << endl;
    }

    return 0;
}

Tài liệu tham khảo
	1.	C++ String Documentation https://cplusplus.com/reference/string/
	2.	C++ Array Documentation https://cplusplus.com/doc/tutorial/arrays/