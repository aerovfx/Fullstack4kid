6️⃣ Giai đoạn 6: Các chủ đề nâng cao (4-6 tuần)
Xử lý file:
Đọc/ghi file với fstream, ifstream, ofstream.
Cấu trúc dữ liệu và giải thuật:
Ngăn xếp (Stack), hàng đợi (Queue), danh sách liên kết (Linked List).
Cây nhị phân (Binary Tree), đồ thị (Graph).
Các khái niệm bổ sung:
Template (hàm và lớp template).
Xử lý ngoại lệ (Exception Handling) với try, catch, throw.
Tính đa luồng (Multithreading) cơ bản.
Bài tập:
Quản lý hàng đợi bệnh nhân.
Xây dựng hệ thống quản lý bán hàng (có thao tác đọc/ghi file).


Giáo trình: Các Chủ Đề Nâng Cao trong C++

Mục tiêu
	•	Làm quen với xử lý file trong C++: đọc/ghi file sử dụng fstream, ifstream, ofstream.
	•	Hiểu và triển khai các cấu trúc dữ liệu và giải thuật cơ bản: ngăn xếp, hàng đợi, danh sách liên kết, cây nhị phân, và đồ thị.
	•	Nắm vững các khái niệm bổ sung: hàm và lớp template, xử lý ngoại lệ, và lập trình đa luồng cơ bản.
	•	Hoàn thành các bài tập thực hành: quản lý hàng đợi bệnh nhân và hệ thống quản lý bán hàng.

Tuần 1: Xử Lý File

1. Đọc/ghi file với fstream, ifstream, ofstream
	•	Khai báo và sử dụng:
	•	ofstream: Ghi dữ liệu vào file.
	•	ifstream: Đọc dữ liệu từ file.
	•	fstream: Đọc và ghi.
	•	Ví dụ: Ghi dữ liệu vào file


#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("output.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào các bạn!" << endl;
        outFile << "Lập trình C++ thật thú vị." << endl;
        outFile.close();
        cout << "Dữ liệu đã được ghi vào file." << endl;
    } else {
        cout << "Không thể mở file!" << endl;
    }
    return 0;
}

	•	Ví dụ: Đọc dữ liệu từ file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream inFile("output.txt");
    string line;
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            cout << line << endl;
        }
        inFile.close();
    } else {
        cout << "Không thể mở file!" << endl;
    }
    return 0;
}
Tuần 2: Cấu Trúc Dữ Liệu

1. Ngăn xếp (Stack)
	•	Đặc điểm: LIFO (Last In, First Out).
	•	Ví dụ: Triển khai ngăn xếp bằng mảng
#include <iostream>
using namespace std;

class Stack {
    int top;
    int arr[100];
public:
    Stack() { top = -1; }

    void push(int x) {
        if (top >= 99) {
            cout << "Stack đầy!" << endl;
            return;
        }
        arr[++top] = x;
    }

    int pop() {
        if (top < 0) {
            cout << "Stack rỗng!" << endl;
            return -1;
        }
        return arr[top--];
    }

    bool isEmpty() {
        return (top < 0);
    }
};

int main() {
    Stack stack;
    stack.push(10);
    stack.push(20);
    cout << "Phần tử lấy ra: " << stack.pop() << endl;
    return 0;
}
2. Hàng đợi (Queue)
	•	Đặc điểm: FIFO (First In, First Out).
	•	Ví dụ: Hàng đợi dùng mảng

#include <iostream>
using namespace std;

class Queue {
    int front, rear, size;
    int arr[100];
public:
    Queue() {
        front = rear = -1;
        size = 100;
    }

    void enqueue(int x) {
        if (rear >= size - 1) {
            cout << "Hàng đợi đầy!" << endl;
            return;
        }
        arr[++rear] = x;
        if (front == -1) front = 0;
    }

    int dequeue() {
        if (front == -1 || front > rear) {
            cout << "Hàng đợi rỗng!" << endl;
            return -1;
        }
        return arr[front++];
    }
};

int main() {
    Queue queue;
    queue.enqueue(10);
    queue.enqueue(20);
    cout << "Phần tử lấy ra: " << queue.dequeue() << endl;
    return 0;
}
3. Danh sách liên kết (Linked List)
	•	Ví dụ cơ bản:
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

void printList(Node* n) {
    while (n != nullptr) {
        cout << n->data << " ";
        n = n->next;
    }
}

int main() {
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = nullptr;

    printList(head);
    return 0;
}

Tuần 3: Các Khái Niệm Bổ Sung

1. Template
	•	Hàm template:

#include <iostream>
using namespace std;

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << "Tổng (int): " << add(3, 5) << endl;
    cout << "Tổng (double): " << add(2.5, 4.5) << endl;
    return 0;
}
2. Xử lý ngoại lệ (Exception Handling)
	•	Ví dụ:
#include <iostream>
using namespace std;

int main() {
    try {
        int a = 10, b = 0;
        if (b == 0) {
            throw "Chia cho 0 là không hợp lệ!";
        }
        cout << a / b << endl;
    } catch (const char* e) {
        cout << "Lỗi: " << e << endl;
    }
    return 0;
}
3. Tính đa luồng (Multithreading)
	•	Ví dụ cơ bản với std::thread:
#include <iostream>
#include <thread>
using namespace std;

void printNumbers() {
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
}

int main() {
    thread t(printNumbers);
    t.join();
    return 0;
}
Tuần 4-6: Bài Tập Thực Hành

1. Quản lý hàng đợi bệnh nhân
	•	Yêu cầu:
	•	Sử dụng hàng đợi để quản lý danh sách bệnh nhân.
	•	Hỗ trợ thêm, xóa, và hiển thị danh sách bệnh nhân.

2. Hệ thống quản lý bán hàng
	•	Yêu cầu:
	•	Quản lý danh sách sản phẩm: ID, tên, giá, số lượng.
	•	Lưu và đọc dữ liệu từ file.
	•	Hỗ trợ thêm, xóa, sửa sản phẩm.
	•	Gợi ý xử lý file:
ofstream file("products.txt");
file << "ID: 1, Tên: Sản phẩm A, Giá: 100, Số lượng: 10" << endl;
file.close();

ifstream file("products.txt");
string line;
while (getline(file, line)) {
    cout << line << endl;
}
Tài liệu tham khảo
	1.	C++ File Handling https://cplusplus.com/doc/tutorial/files/
	2.	C++ Templates https://cplusplus.com/doc/tutorial/templates/
	3.	Multithreading in C++ https://en.cppreference.com/w/cpp/thread
    