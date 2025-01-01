#include <iostream>
using namespace std;

int main() {
    int x;
    // Nhập số x
    std::cout << "Nhập số x: ";
    std::cin >> x;
    string result = (x % 2 == 0) ? "Chẵn" : "Lẻ";
    cout << "x là số " << result << endl;
    return 0;
}
