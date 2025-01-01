// Bài tập yêu cầu nhập vào 1 số và chương trình sẽ in ra x là số chẵn hay lẻ
#include <iostream>
int main(){
    int x;
    //nhập vào số x
    std::cout << "Nhập số x: ";
    std::cin >> x;
    std::string result = (x % 2 == 0) ? "Chẵn" : "Lẻ";
    std::cout << "x là số " << result << std::endl;
    return 0;
}