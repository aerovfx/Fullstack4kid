// Viết chương trình nhập tên và tuổi sau đó in ra màn hình
#include <iostream>
#include<string>

int main()
{
    //code
    std::string ten;
    int tuoi;
    //Nhập tên và tuổi
    std::cout << "Nhập tên của bạn";
    std::getline(std::cin, ten); // Đọc cả dòng để lấy tên đầy đủ

    std::cout << "Nhập tuổi của bạn";
    std::cin >> tuoi;

    //In ra màn hình
    std::cout << "Xin chào" << ten << ", bạn " << tuoi << "tuổi" <<std::endl;


    return 0;

}