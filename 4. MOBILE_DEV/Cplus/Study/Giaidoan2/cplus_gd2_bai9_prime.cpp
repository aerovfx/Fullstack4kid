#include<iostream>
int main(){
    int n;
    std::cout << "Nhập vào số n: ";
    std::cin >> n;
    bool isPrime = true;
    
    if (n < 2) {
        isPrime = false;
    } else {
        for (int i = 2; i*i <= n; i++){
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
    }
    if (isPrime){
        std::cout << n << " là số nguyên tố." << std::endl;
    } else {
        std::cout << n << " không phải là số nguyên tố." << std::endl;
    }
    return 0;
}