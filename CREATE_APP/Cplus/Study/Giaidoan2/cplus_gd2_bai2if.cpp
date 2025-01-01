// Bài tập yêu cầu nhập vào 1 số và chương trình sẽ in ra x là số dương, số âm hay là số 0
#include <iostream>
int main(){
    int x;
    //nhập vào số x
    std::cout << "Nhập số x: ";
    std::cin >> x;
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