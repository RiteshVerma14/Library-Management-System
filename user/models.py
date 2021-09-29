from django.db import models

# Create your models here.

class add_staff_info(models.Model):
    staff_id = models.AutoField
    staff_name = models.CharField(max_length=30)
    staff_mob_no = models.CharField(max_length=25, unique=True)
    staff_email = models.CharField(max_length=50, unique=True)
    staff_pass = models.CharField(max_length=50)
    staff_img = models.ImageField(upload_to="static/ImgStaff/", default="")
    def __str__(self):
        return self.staff_name

class add_book_info(models.Model):
    book_no = models.CharField(max_length=50, unique=True)
    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_title = models.CharField(max_length=50)
    def __str__(self):
        return self.book_name

class add_section_info(models.Model):
    id = models.AutoField
    course_name = models.CharField(max_length=70)
    branch_name = models.CharField(max_length=50)
    def __str__(self):
        return "%s %s" % (self.course_name, self.branch_name)

class add_student_info(models.Model):
    st_roll_no = models.CharField(max_length=30, primary_key=True)
    st_name = models.CharField(max_length=50, null=False)
    st_mob_no = models.CharField(max_length=25, unique=True, null=False)
    st_email = models.CharField(max_length=50, unique=True, null=False)
    st_course = models.CharField(max_length=50, default="", null=False)
    st_branch = models.CharField(max_length=50, default="", null=False)
    st_year = models.IntegerField()
    st_dob = models.DateField()
    st_img = models.ImageField(upload_to="static/ImgStaff/", null=False, default="")
    def __str__(self):
        return self.st_roll_no

class add_day_and_fee(models.Model):
    id = models.AutoField
    issue_day = models.CharField(max_length=10, null=False)
    penalty = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.issue_day

class issued_book(models.Model):
    b_no = models.CharField(max_length=50, primary_key=True)
    b_name = models.CharField(max_length=50, null=False)
    roll_no = models.CharField(max_length=30, null=False)
    def __str__(self):
        return  self.b_no