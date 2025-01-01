#include <iostream>
//us  ing namespace std;

int main() {
    int x = 10;
    if (x > 0) {
        std::cout << "x là số dương" << std::endl;
    } else if (x == 0) {
        std::cout << "x bằng 0" << std::endl;
    } else {
        std::cout << "x là số âm" << std::endl;
    }
    return 0;
}