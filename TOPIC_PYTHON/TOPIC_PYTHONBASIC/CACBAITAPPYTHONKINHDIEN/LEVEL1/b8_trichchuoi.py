#Bài 8. Viết một chương trình nhập vào một danh sách các số và tạo một danh sách mới 
#chỉ gồm phần tử đầu tiên và cuối cùng của danh sách đó. Viết chương trình sử dụng hàm.

#Ví dụ, nhập vào danh sách [5, 10, 15, 20, 25] thì kết quả trả về là danh sách [5, 25]
def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
