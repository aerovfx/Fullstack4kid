#include<iostream>
#include<string> // Thư viện hỗ trợ kiểu dữ liệu chuỗi

int main(){
    // Khởi tạo chuỗi
    std::string str1, str2;

    // Nhập chuỗi từ người dùng
    std::cout << "Nhập chuỗi thứ nhất: ";
    std::getline(std::cin,str1); // Hàm getline để nhập chuỗi có khoảng trống
    std::cout << "Nhập chuỗi thứ hai: ";
    std::getline(std::cin,str2); // Hàm getline để nhập chuỗi có khoảng trống
    
    // Nối hai chuỗi
    std::string concatenated = str1 + " " +str2;
    std::cout << "Chuỗi sau khi nối: " << concatenated << std::endl;

    // Độ dài của chuỗi
    std::cout << "Độ dài của chuỗi sau khi nối là: " << concatenated.length() << std::endl;

    // Tìm kiếm ký tự trong chuỗi
    char target;
    std::cout << "Nhập vào ký tự cần tìm: ";
    std::cin >> target;
    size_t pos = concatenated.find(target); // Hàm find tìm vị trí ký tự

    if (pos != std::string::npos){
        std::cout << "Ký tự " << target << " được tìm thấy tại vị trí " << pos << std::endl;

    } else {
        std::cout << "Ký tự " << target << " không tồn tại trong chuỗi " << std::endl;

    }

    // Đảo ngược chuỗi
    std::string reversed = concatenated; // Sao chép chuỗi
    reverse(reversed.begin(), reversed.end()); //hàm reversed để đảo chuỗi
    std::cout << "Chuỗi sau khi đảo người là: " << reversed << std::endl;
    return 0; //Kết thúc chương trình
}