//Bài 2: Tính chu vi và diện tích hình tròn (dựa vào bán kính nhập từ bàn phím).
#include <iostream>
#include <cmath> // Thư viện toán học cho M_PI
//using namespace std;


int main() {
    double banKinh, chuVi, dienTich;


    // Nhập bán kính
    std::cout << "Nhập bán kính hình tròn: ";
    std:: cin >> banKinh;


    // Tính chu vi và diện tích
    chuVi = 2 * M_PI * banKinh; // Chu vi = 2 * π * r
    dienTich = M_PI * banKinh * banKinh; // Diện tích = π * r^2


    // In kết quả
    std::cout << "Chu vi hình tròn là: " << chuVi << std::endl;
    std::cout << "Diện tích hình tròn là: " << dienTich << std::endl;


    return 0;
}
