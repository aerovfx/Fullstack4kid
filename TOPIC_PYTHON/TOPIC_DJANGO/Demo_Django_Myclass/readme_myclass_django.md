Ứng dụng webapp tạo danh sách thành viên lớp học <br>
Yêu cầu:<br>
Trang thành viên<br>
Trang chi tiết thông tin mỗi thành viên<br>
Chức năng cơ bản: CRUD.<br>


Bước 1: Cài đặt sẵn Python để sử dụng gói PIP.<br>
Cú pháp cài đặt các module là: pip install tên module<br>

Bước 2: Cài đặt môi trường chạy ứng dụng<br>
python -m venv myenvironment<br>
source myenvironment/bin/activate<br>

Bước 3: Cài đặt Django<br>
Cú pháp:<br>
(myenvironment) ... $ python -m pip install Django<br>

Bước 4: Tạo dự án<br>
Cú pháp:<br>
django-admin startproject my_class<br>

Cấu trúc dự án:<br>
my_class<br>
    manage.py<br>
    my_class/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

Bước 5: Chạy thử dự án
Cú pháp:
python manage.py runserver

Bước 6: Tạo app, ứng dụng
Cú pháp:
python manage.py startapp py members

Cấu trúc thư mục dự án như sau:
my_class
    manage.py
    my_class/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

Bước 7: 
