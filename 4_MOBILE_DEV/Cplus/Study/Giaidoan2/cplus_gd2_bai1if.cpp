#include <iostream>
int main(){
    int x = 0;
   if (x > 0){
    //thuc hien dieu kien
    std::cout << "x là số dương" << std::endl;
   } else if (x== 0){
    // thực hiện điều kiện đúng khác
    std::cout << "x bằng 0" << std::endl;
   } else {
    //thực hiện các điều kiện sai
    std::cout << "x là số âm" << std::endl;
   }
return 0;
}