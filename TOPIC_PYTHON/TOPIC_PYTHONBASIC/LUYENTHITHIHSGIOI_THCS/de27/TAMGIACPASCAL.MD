Lập tam giác PASCAL, dùng chương trình con.
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
Trong chương trình trên, chúng ta sử dụng hai chương trình con đệ quy: pascal_triangle và pascal_value.

Hàm pascal_value tính giá trị của một phần tử trong tam giác Pascal dựa trên giá trị của hai phần tử trước đó trong hàng trên đó. Nếu cột col bằng 0 hoặc bằng hàng row, giá trị sẽ là 1 (điều kiện dừng của đệ quy). Trong trường hợp khác, giá trị được tính bằng cách gọi đệ quy với hàng row - 1 và cột col - 1, cộng với giá trị từ đệ quy với hàng row - 1 và cột col.

Hàm pascal_triangle tạo ra tam giác Pascal bằng cách gọi pascal_value cho mỗi phần tử trong mỗi hàng của tam giác. Kết quả cuối cùng là một danh sách các hàng của tam giác Pascal.