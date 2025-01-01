//Bài 3: Tính tổng, hiệu, tích và thương
#include <iostream>


int main() {
    double so1, so2;


    // Nhập hai số
    std::cout << "Nhập số thứ nhất: ";
    std::cin >> so1;
   std:: cout << "Nhập số thứ hai: ";
   std:: cin >> so2;


    // Tính toán
    double tong = so1 + so2;  // Tính tổng
    double hieu = so1 - so2;  // Tính hiệu
    double tich = so1 * so2;  // Tính tích
    double thuong = 0;        // Tính thương


    if (so2 != 0) {
        thuong = so1 / so2;   // Chỉ tính thương nếu số chia khác 0
    }


    // In kết quả
    std::cout << "Tổng của hai số là: " << tong << std::endl;
    std::cout << "Hiệu của hai số là: " << hieu << std::endl;
    std::cout << "Tích của hai số là: " << tich << std::endl;


    if (so2 != 0) {
        std::cout << "Thương của hai số là: " << thuong << std::endl;
    } else {
        std::cout << "Không thể tính thương vì số chia bằng 0." << std::endl;
    }


    return 0;
}
