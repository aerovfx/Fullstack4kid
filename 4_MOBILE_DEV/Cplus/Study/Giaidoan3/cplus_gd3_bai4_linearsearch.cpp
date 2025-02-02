#include<iostream>
// Tạo hàm Linear Search
int linearSearch(int arr[], int n, int target){
    for (int i = 0; i < n; i++){
        if (arr[i] == target){ // So sánh phần tử tại vị trí i với giá trị cần tìm
            return i; // Trả về vị trí tìm thấy
        }
    }
    return -1; // Trả về -1 nếu không tìm thấy
}

int main(){
    // Khởi tạo mảng và giá trị cần tìm
    int arr[] = {3, 40};
    int n = sizeof(arr)/sizeof(arr[0]); // Cập nhật số phần tử của mảng
    int target = 3;

    // Gọi hàm Linear Search
    int result = linearSearch(arr, n, target);

    // Hiển thị kết quả
    if (result != -1) {
        std::cout << "Phần tử " << target << " được tìm thấy tại vị trí: " << result << std::endl;

    } else {
        std::cout << "Phần tử " << target << " không tồn tại trong mảng " << std::endl;
    }
    return 0;

}