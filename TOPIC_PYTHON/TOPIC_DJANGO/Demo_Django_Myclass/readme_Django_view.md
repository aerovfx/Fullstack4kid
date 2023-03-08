Views
Chế độ xem Django là các hàm Python nhận yêu cầu http và trả về phản hồi http, giống như tài liệu HTML.

Một trang web sử dụng Django có đầy đủ các chế độ xem với các tác vụ và nhiệm vụ khác nhau.

Lượt xem thường được đặt trong tệp có tên views.py nằm trong thư mục ứng dụng của bạn.

File views.py trong thư mục member (thành viên) của bạn trông như thế này:

my_class/members/views.py:

    from django.shortcuts import render

# Create your views here.

my_class/members/views.py:

    from django.shortcuts import render
    from django.http import HttpResponse

    def members(request):
        return HttpResponse("Hello world!")


Note: The name of the view does not have to be the same as the application.

I call it members because I think it fits well in this context.