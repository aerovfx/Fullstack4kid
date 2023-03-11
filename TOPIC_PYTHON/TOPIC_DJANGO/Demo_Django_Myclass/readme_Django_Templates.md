Trong trang Django, chúng ta nên trả về kết quả là một trang tĩnh HTML, và trang đó chúng ta tạo sẵn trong thư mục Template.

The file structure should be like this:

my_class
    manage.py
    my_class/
    members/
        templates/
            base.html

Open the HTML file and insert the following:

my_class/members/templates/base.html:

<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>

Chế độ View Members thực hiện như sau:

Tạo một đối tượng mymembers với tất cả các giá trị của mô hình Thành viên.
Tải mẫu all_members.html.
Tạo một đối tượng chứa đối tượng mymembers.
Gửi đối tượng đến model.
Xuất ra HTML được hiển thị bởi model.