Model Django là một bảng trong cơ sở dữ liệu của bạn. <br>

MODEL DJANGO<br>

Cho đến bây giờ trong hướng dẫn này, đầu ra là dữ liệu tĩnh từ các mẫu Python hoặc HTML.

Bây giờ chúng ta sẽ xem cách Django cho phép chúng ta làm việc với dữ liệu mà không cần phải thay đổi hoặc tải tệp lên trong quy trình.

Trong Django, dữ liệu được tạo trong các đối tượng, được gọi là Model và thực sự là các bảng trong cơ sở dữ liệu.

Tạo bảng (Model)
Để tạo một model, hãy điều hướng đến tệp models.py trong thư mục /members/.
Nội dung như sau:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  