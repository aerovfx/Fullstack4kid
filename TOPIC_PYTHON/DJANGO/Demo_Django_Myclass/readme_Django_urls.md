URLs<br>
Tạo một file có tên là urls.py cùng cấp với file views.py ở bài học trước, sau đó gõ cú pháp lệnh như sau:<br>

my_class/members/urls.py:<br>

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]


Tệp urls.py bạn vừa tạo dành riêng cho ứng dụng members. Chúng tôi cũng phải thực hiện một số định tuyến trong thư mục gốc my_class. Điều này có vẻ phức tạp, nhưng bây giờ, chỉ cần làm theo các hướng dẫn bên dưới.<br>

Có một tệp tên là urls.py trên thư mục my_class. <br>
Hãy mở tệp đó và thêm mô-đun bao gồm trong câu lệnh nhập, đồng thời thêm một hàm path() trong danh sách urlpatterns[], với các đối số sẽ định tuyến người dùng truy cập qua 127.0.0.1:8000/.<br>

my_class/my_class/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

Để xem kết quả chúng ta tạo ra, gõ dòng lệnh:<br>

python manage.py runserver

Trong trình duyệtm gõ 127.0.0.1:8000/members/<br>
Vậy chúng ta đã chay trang members vừa tạo ra.

