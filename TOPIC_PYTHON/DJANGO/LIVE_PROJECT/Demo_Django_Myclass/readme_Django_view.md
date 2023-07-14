VIEW <br>
Chế độ xem Django là các hàm Python nhận yêu cầu http và trả về phản hồi http, giống như tài liệu HTML.<br>

Một trang web sử dụng Django có đầy đủ các chế độ xem với các tác vụ và nhiệm vụ khác nhau.<br>

Lượt xem thường được đặt trong tệp có tên views.py nằm trong thư mục ứng dụng của bạn.<br>

File views.py trong thư mục member (thành viên) của bạn trông như thế này:<br>

my_class/members/views.py:<br>

    from django.shortcuts import render

# Create your views here.<br>

my_class/members/views.py:

    from django.shortcuts import render
    from django.http import HttpResponse

    def members(request):
        return HttpResponse("Hello world!")


Note: 
    Tên của view không nhất thiết phải giống như tên ứng dụng<br>
    Tên app tôi gọi là thành viên vì nó phù hợp với đặc điểm của ứng dụng là quản lí danh sách các thành viên.
