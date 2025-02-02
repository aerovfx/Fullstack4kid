#include<iostream>
int main(){
    for (int i = 1; i <= 10; i++){
        if (i== 5){
            continue; //Bỏ qua số 5
        }
        if (i == 8){
            break;//Thoát khỏi vòng lặp
        }
        std::cout << i << " ";
    }
    return 0;
}