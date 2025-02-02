#include <iostream> // Thư viện hỗ trợ nhập/xuất
using std::cout;
using std::endl;
using std::cin;

int main() {
    int number;
    cout << "Nhap so: "; // Hiển thị yêu cầu nhập
    cin >> number;       // Nhập số từ bàn phím
    cout << "Ban da nhap: " << number << endl; // Hiển thị giá trị vừa nhập
    return 0;// Trả về giá trị 0, báo hiệu chương trình kết thúc thành công
}