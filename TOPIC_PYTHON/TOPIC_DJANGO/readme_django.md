
TỔNG QUAN VỀ FRAMEWORK DJANGO

Django là một framework web Python bao gồm một tập hợp các thành phần giải quyết các vấn đề phổ biến trong phát triển web.

Django cho phép bạn phát triển các ứng dụng web nhanh chóng hơn với ít mã hơn bằng cách tận dụng framework của nó.

Django tuân theo nguyên tắc DRY (đừng lặp lại chính mình), cho phép tối đa hóa khả năng tái sử dụng mã.

Django sử dụng mô hình MVT (Model-View-Template), tương đối giống với mô hình MVC (Model-View-Controller).

Mô hình MVT bao gồm ba thành phần chính:

Model - định nghĩa dữ liệu hoặc chứa logic tương tác với dữ liệu trong cơ sở dữ liệu.

View - liên lạc với cơ sở dữ liệu thông qua model và chuyển dữ liệu sang template để hiển thị dữ liệu.

Template - định nghĩa template để hiển thị dữ liệu trên trình duyệt web.

Chính framework Django làm vai trò của một controller. Framework Django sử dụng URL pattern để gửi yêu cầu tới view phù hợp.

Trong thực tế, bạn thường sẽ làm việc với models, templates, views và URLs trong ứng dụng Django.

Kiến trúc Django

Hình ảnh sau đây cho thấy cách Django quản lý chu kỳ yêu cầu/ phản hồi HTTP bằng các thành phần của nó:

Trình duyệt web yêu cầu trang bằng một URL và máy chủ web chuyển yêu cầu HTTP đến Django.
Django khớp URL với các URL pattern để tìm bất kỳ kết quả nào đầu tiên.
Django gọi view tương ứng với URL phù hợp.
View sử dụng model để truy xuất dữ liệu từ cơ sở dữ liệu.
Model trả về dữ liệu cho view.
View kết xuất một template và trả lại nó dưới dạng phản hồi HTTP.
Tạo một môi trường ảo (virtual environment).

Một môi trường ảo tạo ra một môi trường cô lập bao gồm một tập hợp độc lập các gói Python.

Bằng cách sử dụng các môi trường ảo, bạn có thể có các dự án sử dụng các phiên bản Django khác nhau. Ngoài ra, khi bạn di chuyển dự án đến một máy chủ khác, bạn có thể cài đặt tất cả các gói phụ thuộc của dự án bằng một lệnh pip duy nhất.

Đầu tiên, tạo một thư mục mới là django-playground:

mkdir django-playground

Thứ hai, điều hướng đến thư mục django-playground:

cd django-playground

Thứ ba, tạo một môi trường ảo mới bằng module venv:

python -m venv venv

Thứ tư, kích hoạt môi trường ảo:

venv\scripts\activate

Terminal sẽ hiển thị như sau:

(venv) D:\django-playground>

Lưu ý rằng bạn có thể tắt môi trường ảo bằng lệnh deactivate:

deactivate

Cài đặt gói Django

Đầu tiên, sử dụng lệnh pip sau để cài đặt gói Django:

pip install django

Thứ hai, kiểm tra phiên bản Django:

python -m django --version

Nó sẽ hiển thị một cái gì đó như thế này:

4.1.1

Lưu ý rằng bạn có thể thấy một phiên bản cao hơn.

Khám phá các lệnh Django

Django đi kèm với một chương trình tiện ích dòng lệnh được gọi là django-admin để quản lý các nhiệm vụ quản trị như tạo một dự án mới và thực thi máy chủ phát triển Django.

Để chạy Django, bạn thực hiện lệnh sau để liệt kê tất cả các lệnh trung tâm Django:

django-admin

Đầu ra:

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
check
compilemessages
createcachetable
dbshell
diffsettings
dumpdata
flush
inspectdb
loaddata
makemessages
makemigrations
migrate
optimizemigration
runserver
sendtestemail
shell
showmigrations
sqlflush
sqlmigrate
sqlsequencereset
squashmigrations
startapp
startproject
test
testserver

Đối với bây giờ, chúng ta quan tâm đến lệnh startproject để tạo một dự án Django mới. Lệnh startproject sau đây tạo một dự án mới được gọi là django_project:

django-admin startproject

cd django_project

Lúc đó chúng ta có một cấu trúc thư mục như sau:

├── django_project
| ├── asgi.py
| ├── settings.py
| ├── urls.py
| ├── wsgi.py
| └── __init__.py
└── manage.py

Dưới đây là chức năng của mỗi file trong cấu trúc trên:

Đây là một tổng quan nhanh về mỗi tệp trong dự án Django:

manage.py là một chương trình dòng lệnh mà bạn sử dụng để tương tác với dự án như bắt đầu một máy chủ phát triển và thực hiện các thay đổi trên cơ sở dữ liệu.

django_project là một gói Python bao gồm các tệp sau:

init.py - là một tệp rỗng cho biết thư mục django_project là một gói.
settings.py - chứa các thiết lập dự án như các ứng dụng đã cài đặt, kết nối cơ sở dữ liệu và các thư mục mẫu.
urls.py - lưu trữ danh sách các đường dẫn URL được ánh xạ đến các chế độ xem.
wsgi.py - chứa các cấu hình chạy dự án như một ứng dụng cổng web server gateway interface (wsgi) với các máy chủ web tương thích WSGI.
asgi.py - chứa các cấu hình chạy dự án như một ứng dụng cổng web server gateway interface bất đồng bộ (AWSGI) với các máy chủ web tương thích AWSGI.

Chạy máy chủ phát triển Django

Django đi kèm với một máy chủ web tích hợp sẵn cho phép bạn nhanh chóng chạy dự án Django của mình cho mục đích phát triển.

Máy chủ web phát triển Django sẽ liên tục kiểm tra các thay đổi mã và tự động tải lại dự án. Tuy nhiên, bạn vẫn cần khởi động lại máy chủ web thủ công trong một số trường hợp như thêm các tệp mới vào dự án.

Để chạy máy chủ phát triển Django, bạn sử dụng lệnh runserver:

python manage.py runserver

Đầu ra:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
...
Django version 4.1.1, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Sau khi máy chủ đã hoạt động, bạn có thể mở ứng dụng web bằng URL được liệt kê trong đầu ra. Thông thường, URL sẽ có dạng như sau:

http://127.0.0.1:8000/

Lúc này sẽ có một trang chủ mặc định xuất hiện.


The urls.py contains a default route that maps /admin path with the admin.site.urls view:

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
Code language: Python (python)
To open the admin page, you use the following URL:

http://127.0.0.1:8000/admin
Code language: JavaScript (javascript)
It’ll show a login page:

django getting started - login
Stop the Django development server

Để dừng hoạt động của trang chủ mặc định tại cổng 8000 bạn gõ Ctrl-C (or Command-C) với macos.

Create requirements.txt file

Để tạo những sao lưu về phiên bản các module của ứng dụng chúng ta tạo file có tên là requirements.txt 
Bạn chạy cú pháp sau:

pip freeze > requirements.txt

Khi bạn di chuyển dự án sang một máy chủ mới, ví dụ như máy chủ thử nghiệm hoặc sản xuất, bạn có thể cài đặt tất cả các phụ thuộc được sử dụng bởi dự án Django hiện tại bằng lệnh pip sau:


pip install -r requirements.txt
Code language: plaintext (plaintext)


