#include <iostream> // Thư viện nhập/xuất dữ liệu
using std::cout;
using std::endl;
 // Sử dụng không gian tên chuẩn để không cần gõ "std::"

int main() { // Hàm chính, nơi chương trình bắt đầu thực thi
    //// Không cần viết std::cout vì đã khai báo dòng thứ 2.
    cout << "Hello, World!" << endl; // In dòng chữ "Hello, World!" và xuống dòng
    return 0; // Trả về 0, báo hiệu chương trình kết thúc thành công
}
