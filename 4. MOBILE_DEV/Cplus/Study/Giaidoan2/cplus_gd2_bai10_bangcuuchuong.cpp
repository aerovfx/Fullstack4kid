#include<iostream>
int main(){
    for (int i = 2; i <=9; i++){
        std::cout << "Bảng cửu chương " << i << ":" << std::endl;
        for (int j = 1; j <= 10; j++){
            std::cout << i << " x " << j << " = " << i*j << std::endl;
        }
        std::cout << std::endl;
    }
    return 0;
}