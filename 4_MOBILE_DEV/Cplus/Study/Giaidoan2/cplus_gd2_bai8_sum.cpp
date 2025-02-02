#include<iostream>
int main(){
    int n, sum = 0;
    std::cout << "Nhập n: ";
    std::cin >> n;
    for (int i = 1; i <= n; i++){
        sum += i;
    }
    std::cout << "Tổng từ 1 đến " << n << " là: " << sum << std::endl;
    return 0;
}

