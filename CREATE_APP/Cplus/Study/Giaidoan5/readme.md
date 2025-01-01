5️⃣ Giai đoạn 5: Lập trình hướng đối tượng (OOP) (3-4 tuần)
Khái niệm OOP:
Lớp (class), đối tượng (object).
Thuộc tính (attributes), phương thức (methods).
Phạm vi truy cập (public, private, protected).
Tính chất OOP:
Tính đóng gói (Encapsulation).
Tính kế thừa (Inheritance), từ khóa : public.
Tính đa hình (Polymorphism), hàm ảo (virtual), nạp chồng phương thức.
Tính trừu tượng (Abstraction).
Bài tập:
Viết chương trình quản lý học sinh, sinh viên.
Xây dựng hệ thống quản lý sách trong thư viện.
------------------
Giáo trình: Lập trình hướng đối tượng (OOP) với C++

Mục tiêu
	•	Nắm vững các khái niệm cơ bản về lập trình hướng đối tượng trong C++.
	•	Hiểu và triển khai được 4 tính chất OOP: Đóng gói, Kế thừa, Đa hình, Trừu tượng.
	•	Hoàn thành các bài tập thực hành nhằm củng cố kiến thức.

Tuần 1: Tổng quan về OOP trong C++

1. Khái niệm OOP
	•	Lớp (class): Là một mẫu để tạo ra các đối tượng. Một lớp chứa các thuộc tính (dữ liệu) và phương thức (hành vi).
	•	Đối tượng (object): Là một thực thể cụ thể được tạo ra từ lớp.

2. Cách khai báo lớp và đối tượng
#include <iostream>
using namespace std;

class Person {
    // Thuộc tính
    string name;
    int age;

public: // Phạm vi truy cập
    // Hàm khởi tạo
    Person(string n, int a) {
        name = n;
        age = a;
    }

    // Phương thức
    void greet() {
        cout << "Hello, my name is " << name << " and I am " << age << " years old." << endl;
    }
};

int main() {
    Person p("Alice", 25); // Tạo đối tượng
    p.greet();             // Gọi phương thức
    return 0;
}

3. Phạm vi truy cập
	•	public: Có thể truy cập từ mọi nơi trong chương trình.
	•	private: Chỉ có thể truy cập bên trong lớp.
	•	protected: Truy cập trong lớp và các lớp dẫn xuất.

Ví dụ minh họa:
class Demo {
public:
    int publicVar;

protected:
    int protectedVar;

private:
    int privateVar;
};

Tuần 2: Tính chất của OOP

1. Tính đóng gói (Encapsulation)
	•	Giấu thông tin nội bộ của đối tượng, chỉ cung cấp giao diện cần thiết.
	•	Dùng các phương thức getter và setter để truy cập thuộc tính private.

class BankAccount {
private:
    double balance;

public:
    BankAccount(double initialBalance) {
        balance = initialBalance;
    }

    double getBalance() {
        return balance;
    }

    void setBalance(double amount) {
        if (amount >= 0) {
            balance = amount;
        }
    }
};
2. Tính kế thừa (Inheritance)
	•	Lớp con kế thừa thuộc tính và phương thức từ lớp cha.
	•	Từ khóa: public, protected, private.
class Animal {
public:
    void speak() {
        cout << "Animal speaks" << endl;
    }
};

class Dog : public Animal {
public:
    void speak() {
        cout << "Dog barks" << endl;
    }
};

Tuần 3: Tính chất nâng cao

1. Tính đa hình (Polymorphism)
	•	Hàm ảo (Virtual Function): Cho phép ghi đè phương thức của lớp cha trong lớp con.

class Shape {
public:
    virtual void draw() {
        cout << "Drawing Shape" << endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
};

Nạp chồng phương thức (Method Overloading): Một hàm có thể có nhiều phiên bản với các tham số khác nhau.
class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
};
2. Tính trừu tượng (Abstraction)
	•	Lớp trừu tượng chỉ định nghĩa giao diện, không triển khai chi tiết.
	•	Sử dụng từ khóa virtual và = 0.
class Animal {
public:
    virtual void makeSound() = 0; // Phương thức thuần ảo
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow" << endl;
    }
};

Tuần 4: Bài tập thực hành

Bài tập 1: Quản lý học sinh, sinh viên
	1.	Yêu cầu:
	•	Xây dựng lớp Student với các thuộc tính: id, name, age, className.
	•	Xây dựng các phương thức: thêm mới, sửa, xóa, hiển thị danh sách sinh viên.
	2.	Gợi ý:
	•	Sử dụng mảng (hoặc vector) để lưu trữ danh sách sinh viên.
#include <iostream>
#include <vector>
using namespace std;

class Student {
    int id;
    string name;
    int age;
    string className;

public:
    Student(int i, string n, int a, string c) : id(i), name(n), age(a), className(c) {}

    void display() {
        cout << "ID: " << id << ", Name: " << name << ", Age: " << age << ", Class: " << className << endl;
    }
};

int main() {
    vector<Student> students;
    students.push_back(Student(1, "Alice", 20, "CS101"));
    students.push_back(Student(2, "Bob", 21, "CS102"));

    for (auto& s : students) {
        s.display();
    }
    return 0;
}

Bài tập 2: Quản lý sách trong thư viện
	1.	Yêu cầu:
	•	Tạo lớp Book với thuộc tính: id, title, author, status.
	•	Tạo lớp Library với các chức năng: thêm sách, mượn sách, trả sách, hiển thị danh sách sách.
	2.	Gợi ý:
	•	Sử dụng từ điển (hoặc map) để lưu thông tin sách.
#include <iostream>
#include <map>
using namespace std;

class Book {
    int id;
    string title;
    string author;
    bool isAvailable;

public:
    Book(int i, string t, string a, bool av) : id(i), title(t), author(a), isAvailable(av) {}

    void display() {
        cout << "ID: " << id << ", Title: " << title << ", Author: " << author
             << ", Available: " << (isAvailable ? "Yes" : "No") << endl;
    }

    bool borrowBook() {
        if (isAvailable) {
            isAvailable = false;
            return true;
        }
        return false;
    }

    void returnBook() {
        isAvailable = true;
    }
};

int main() {
    map<int, Book> library;
    library[1] = Book(1, "C++ Programming", "Author A", true);
    library[2] = Book(2, "Data Structures", "Author B", true);

    // Hiển thị sách
    for (auto& b : library) {
        b.second.display();
    }

    return 0;
}

Tài liệu tham khảo
	1.	C++ Documentation
	2.	Sách “Object-Oriented Programming in C++” (tác giả Robert Lafore).