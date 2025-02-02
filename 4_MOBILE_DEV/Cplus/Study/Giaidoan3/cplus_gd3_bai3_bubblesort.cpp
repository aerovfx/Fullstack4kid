#include<iostream> // Thư viện hỗ trợ nhập và xuất dữ liệu

//Hàm thực hiện thuật toán nổi bọt
void bubbleSort(int arr[], int n){
    // Lặp qua mảng và so sánh các cặp phần tử liền kề nhau
    for (int i = 0; i < n -1; i++){
        for (int j = 0; j < n - i - 1; j++){
            // Nếu phần tử trước lớn hơn phần tử sau thì đổi chỗ cho nhau.
            if (arr[j] > arr[j + 1]){
                std::swap(arr[j], arr[j+1]); // Hàm swap đổi giá trị hai phần tử nếu thoả điều kiện
            }
        }
    }
}

int main(){
    // Khởi tại mảng arr với các giá trị cho trước.
    int arr[] = {4, 6, 0, 9, 79, 21};
    int n = sizeof(arr)/sizeof(arr[0]); // Tính số phần tử của mảng bằng cách chia tổng kích thức mảng cho kích thước một phần tử

    // Gọi hàm sắp xếp nổi bọt 
    bubbleSort(arr, n);

    // Duyệt qua mảng và in từng phần tử sau khi sắp xếp
    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " "; // In giá trị phần tử 

    }
    return 0; // Kết thúc chương trình, trả về 0 cho hệ điều hành
}