from django.db import models

#Model thành viên của lớp học Class bao gồm họ và tên.
class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
#Model lớp gồm có sinh viên là thành viên lớp cùng với tên lớp, ngày mở, ngày kết thúc và đánh giá xếp hạng.
class Class(models.Model):
    student = models.ForeignKey(Members, on_delete=models.CASCADE)
    nameclass = models.CharField(max_length=100)
    open_date = models.DateField()
    close_date = models.DateField()
    num_stars = models.IntegerField()
    
