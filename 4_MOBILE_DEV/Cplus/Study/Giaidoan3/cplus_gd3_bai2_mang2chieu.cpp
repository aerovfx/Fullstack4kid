#include<iostream>
int main(){
    int matrix[2][3] = {{1,3,5},{2,4,6}};
    for (int i = 0; i <2; i++){
        for (int j = 0; j < 3; j++){
            std::cout << matrix[i][j] << " ";

        }
        std::cout << std::endl;
        
    }
    std::cout << matrix[0][2];
    return 0;
}
//matrix[0][0] = 1
//matrix[0][1] = 3
//matrix[0][2] = 5