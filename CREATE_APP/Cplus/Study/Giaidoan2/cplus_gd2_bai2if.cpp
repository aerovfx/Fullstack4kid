// Bài tập yêu cầu nhập vào 1 số và chương trình sẽ in ra x là số dương hay số âm hay số 0.
#include <iostream>
//using namespace std;

int main() {
    int x;
    // Nhập số x
    std::cout << "Nhập số x: ";
    std::cin >> x;
    if (x > 0) {
        std::cout << "x là số dương" << std::endl;
    } else if (x == 0) {
        std::cout << "x bằng 0" << std::endl;
    } else {
        std::cout << "x là số âm" << std::endl;
    }
    return 0;
}