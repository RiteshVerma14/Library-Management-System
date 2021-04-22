from django.contrib import admin
from . models import *

# Register your models here.

class addStaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name','id','staff_mob_no','staff_email','staff_img')
admin.site.register(add_staff_info,addStaffAdmin)

class addBookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_no','book_author','book_title')
admin.site.register(add_book_info,addBookAdmin)

class addSectionsAdmin(admin.ModelAdmin):
    list_display = ('course_name','id','branch_name')
admin.site.register(add_section_info,addSectionsAdmin)

class addStudentAdmin(admin.ModelAdmin):
    list_display = ('st_roll_no', 'st_name', 'st_year')
admin.site.register(add_student_info,addStudentAdmin)

class addDayAndFee(admin.ModelAdmin):
    list_display = ('issue_day', 'id', 'penalty')
admin.site.register(add_day_and_fee,addDayAndFee)

class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'b_no', 'b_name')
admin.site.register(issued_book,IssuedBookAdmin)