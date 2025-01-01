7️⃣ Giai đoạn 7: Dự án hoàn chỉnh (2-4 tuần)
Xây dựng một dự án C++ hoàn chỉnh:
Trò chơi mini (cờ caro, rắn săn mồi...).
Quản lý học sinh/sinh viên có sử dụng file.
Xây dựng hệ thống quản lý nhân viên với tính kế thừa.
Rèn luyện thói quen:
Làm quen với các nguyên tắc clean code.
Áp dụng các mẫu thiết kế (Design Patterns) cơ bản.

Giáo trình: Dự Án Hoàn Chỉnh trong C++

Mục tiêu
	•	Xây dựng một dự án C++ hoàn chỉnh từ đầu đến cuối.
	•	Tăng cường kỹ năng sử dụng OOP, xử lý file, và áp dụng các nguyên tắc clean code.
	•	Làm quen và áp dụng một số mẫu thiết kế (Design Patterns) cơ bản.

Tuần 1: Lên Ý Tưởng và Lập Kế Hoạch

1. Chọn ý tưởng dự án

Sinh viên có thể chọn một trong các dự án sau:
	1.	Trò chơi mini:
	•	Cờ caro: Trò chơi 2 người trên lưới kích thước n x n.
	•	Rắn săn mồi: Di chuyển trên lưới, ăn mồi để tăng kích thước.
	2.	Hệ thống quản lý:
	•	Quản lý học sinh/sinh viên: Hỗ trợ thêm, sửa, xóa, lưu dữ liệu vào file.
	•	Quản lý nhân viên: Sử dụng tính kế thừa để tổ chức thông tin (Nhân viên thường, Quản lý…).

2. Phân tích yêu cầu
	•	Xác định các chức năng chính của dự án.
	•	Lập sơ đồ luồng dữ liệu hoặc sơ đồ lớp nếu cần thiết.

Ví dụ: Dự án Quản lý Học sinh
	•	Chức năng chính:
	•	Thêm, xóa, sửa thông tin học sinh.
	•	Lưu và đọc dữ liệu từ file.
	•	Thông tin học sinh: ID, Tên, Tuổi, Điểm trung bình.

-----------
Tuần 2: Xây Dựng Cấu Trúc Dự Án

1. Thiết kế cấu trúc OOP
	•	Xây dựng các lớp:
	•	Quản lý học sinh/sinh viên:
	•	Lớp Student để lưu trữ thông tin.
	•	Lớp StudentManager để xử lý các chức năng thêm, sửa, xóa.
	•	Hệ thống quản lý nhân viên:
	•	Lớp cơ sở Employee và các lớp kế thừa như Manager và Staff.

Ví dụ: Cấu trúc lớp cho quản lý nhân viên
class Employee {
protected:
    int id;
    string name;
    double salary;
public:
    virtual void displayInfo() = 0; // Hàm thuần ảo
};

class Manager : public Employee {
private:
    double bonus;
public:
    void displayInfo() override {
        cout << "ID: " << id << ", Name: " << name << ", Salary: " << salary << ", Bonus: " << bonus << endl;
    }
};

class Staff : public Employee {
public:
    void displayInfo() override {
        cout << "ID: " << id << ", Name: " << name << ", Salary: " << salary << endl;
    }
};

2. Tổ chức code theo nguyên tắc Clean Code
	•	Đặt tên rõ ràng: Tên biến, hàm, lớp nên mô tả ý nghĩa.
	•	Chia nhỏ hàm: Mỗi hàm thực hiện một nhiệm vụ duy nhất.
	•	Sử dụng comment khi cần thiết: Giải thích các đoạn code phức tạp.

Ví dụ Clean Code:
// Thay vì viết:
int a(int b) { return b * b; }

// Hãy viết:
int calculateSquare(int number) {
    return number * number;
}
Tuần 3: Tích Hợp và Hoàn Thiện

1. Xử lý file
	•	Đọc và ghi dữ liệu từ/đến file.
	•	Ví dụ: Lưu danh sách sinh viên vào file.
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct Student {
    int id;
    string name;
    double gpa;
};

void saveToFile(const vector<Student>& students, const string& filename) {
    ofstream file(filename);
    for (const auto& student : students) {
        file << student.id << "," << student.name << "," << student.gpa << endl;
    }
    file.close();
}

int main() {
    vector<Student> students = {{1, "Alice", 3.5}, {2, "Bob", 3.8}};
    saveToFile(students, "students.txt");
    return 0;
}
2. Áp dụng Design Patterns
	•	Singleton: Dùng để quản lý trạng thái toàn cục.
	•	Ví dụ: Một lớp FileManager để quản lý tất cả thao tác với file.
	•	Factory: Tạo các đối tượng động.
	•	Ví dụ: Tạo đối tượng Manager hoặc Staff dựa trên loại nhân viên.

Ví dụ Singleton Pattern:
#include <iostream>
using namespace std;

class FileManager {
private:
    static FileManager* instance;
    FileManager() {}
public:
    static FileManager* getInstance() {
        if (!instance) {
            instance = new FileManager();
        }
        return instance;
    }

    void writeFile(const string& data) {
        cout << "Writing data: " << data << endl;
    }
};

FileManager* FileManager::instance = nullptr;

int main() {
    FileManager::getInstance()->writeFile("Hello, Singleton!");
    return 0;
}
Tuần 4: Kiểm Tra và Báo Cáo

1. Kiểm tra
	•	Viết test cho các chức năng chính.
	•	Đảm bảo chương trình không bị lỗi runtime hoặc logic.

2. Báo cáo
	•	Viết tài liệu báo cáo về:
	•	Mục tiêu dự án.
	•	Cách tổ chức code.
	•	Kết quả đạt được.

Gợi Ý Bài Tập

1. Trò chơi mini
	•	Cờ caro: Hai người chơi thay phiên đánh dấu X hoặc O trên bàn cờ, xác định người thắng.
	•	Rắn săn mồi: Di chuyển rắn, ăn mồi để tăng kích thước.

2. Quản lý học sinh
	•	Thêm, sửa, xóa học sinh.
	•	Lưu và đọc dữ liệu từ file.

3. Hệ thống quản lý nhân viên
	•	Tạo nhân viên với các loại khác nhau.
	•	Tính tổng lương dựa trên các mức phụ cấp.
Tài liệu tham khảo
	1.	C++ Clean Code https://www.cppstories.com/
	2.	Design Patterns in C++ https://refactoring.guru/design-patterns/cpp
    
3