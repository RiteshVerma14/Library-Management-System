from datetime import datetime
from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db import connection
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def StaffLogin(request):
    return render(request, 'lstaff/s_login.html')

def s_staff_panel(request):
    if request.user.is_authenticated:
        return render(request, 'lstaff/s_staff_panel.html')
    else:
        return render(request, 'lstaff/s_login.html')

def s_log_in(request):
    if request.method == 'POST':
        s_email = request.POST.get("email", "")
        s_password = request.POST.get("password", "")
        user = auth.authenticate(username=s_email, password=s_password)
        if user is not None:
            login(request,user)
            return render(request, 'lstaff/s_staff_panel.html', context={"Valid":True})
        else:
            return render(request, 'lstaff/s_login.html', context={"Invalid":True})

def s_book_issue(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_no = request.POST.get('st_roll_no')
            details = add_student_info.objects.filter(st_roll_no=roll_no)
            result = issued_book.objects.filter(roll_no = roll_no)
            if details:
                return render(request, 'lstaff/s_book_issue.html', context={"details" : details, "result" : result})
            else:
                status = "Please enter correct Roll No."
                return render(request, 'lstaff/s_book_issue.html', context={"S" : status})
        return render(request, 'lstaff/s_book_issue.html')
    else:
        return render(request, 'lstaff/s_login.html')

def s_book_issue_2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            b_no = request.POST.get('book_no')
            roll_no = request.POST.get('roll_no')
            data = add_book_info.objects.filter(book_no = b_no)
            if data:
                result = issued_book.objects.filter(b_no = b_no)
                if result:
                    response = HttpResponse("already_issued")
                    return response
                else:
                    b_name = ""
                    for d in data:
                        b_name = d
                    res = issued_book(b_no = b_no, b_name = str(b_name), roll_no = roll_no)
                    res.save()
                    response = HttpResponse("issue")
                    return response
            else:
                response = HttpResponse("wrong_data")
                return response
        return render(request, 'lstaff/s_book_issue.html')
    else:
        return render(request, 'lstaff/s_login.html')

def s_return_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_no = request.POST.get('st_roll_no')
            details = add_student_info.objects.filter(st_roll_no=roll_no)
            result = issued_book.objects.filter(roll_no = roll_no)
            if details:
                return render(request, 'lstaff/s_return_book.html', context={"details" : details, "result" : result})
            else:
                status = "Please enter correct Roll No."
                return render(request, 'lstaff/s_return_book.html', context={"S" : status})
        return render(request, 'lstaff/s_return_book.html')
    else:
        return render(request, 'lsatff/s_login.html')

def s_return_book_2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            b_no = request.POST.get('book_no')
            roll_no = request.POST.get('roll_no')
            data = add_book_info.objects.filter(book_no = b_no)
            if data:
                result = issued_book.objects.filter(b_no = b_no)
                if result:
                    r_no = ""
                    for r in result:
                        r_no = r.roll_no
                    if (r_no == roll_no):
                        dlt = issued_book.objects.filter(b_no = b_no)
                        dlt.delete()
                        response = HttpResponse("returned")
                        return response
                    else:
                        response = HttpResponse("not_this_user")
                        return response
                else:
                    response = HttpResponse("not_issued")
                    return response
            else:
                response = HttpResponse("wrong_data")
                return response
        return render(request, 'lstaff/s_book_issue.html')
    else:
        return render(request, 'lstaff/s_login.html')

def s_issued_book(request):
    if request.user.is_authenticated:
        value = issued_book.objects.all().order_by("-b_no")
        return render(request, 'lstaff/s_issued_book.html', context={"data":value})
    else:
        return render(request, 'lstaff/s_login.html')

def s_search_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            book_no = request.POST.get('book_no')
            details = add_book_info.objects.filter(book_no=book_no)
            if details:
                result = issued_book.objects.filter(b_no = book_no)
                if result:
                    return render(request, 'lstaff/s_search_book.html', context={"details": details, "result" : result})
                else:
                    return render(request, 'lstaff/s_search_book.html', context={"details": details})
            else:
                status = "Please enter correct book number."
                return render(request, 'lstaff/s_search_book.html', context={"S": status})
        return render(request, 'lstaff/s_search_book.html')
    else:
        return render(request, 'lstaff/s_login.html')

def s_log_out(request):
    logout(request)
    return render(request, 'lstaff/s_login.html')

def AdminLogin(request):
    return render(request, 'ladmin/a_login.html')

def a_sign_in(request):
    if request.method == 'POST':
        a_email = request.POST.get("a_email", "")
        a_password = request.POST.get("a_password", "")
        user = auth.authenticate(username=a_email, password=a_password)
        if user is not None:
            login(request,user)
            return render(request, 'ladmin/a_admin_panel.html', context={"Valid":True})
        else:
            return render(request, 'ladmin/a_login.html', context={"Invalid":True})

def a_admin_panel(request):
    if request.user.is_authenticated:
        return render(request, 'ladmin/a_admin_panel.html')
    else:
        return render(request, 'ladmin/a_login.html')

def a_profile(request):
    if request.user.is_authenticated:
        return render(request, 'ladmin/a_profile.html')
    else:
        return render(request, 'ladmin/a_login.html')

def a_change_password(request):
    if request.user.is_authenticated:
        return render(request, 'ladmin/a_change_password.html')
    else:
        return render(request, 'ladmin/login.html')

def a_staff(request):
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("Select s.id, s.staff_name, s.staff_mob_no, s.staff_email, s.staff_pass, s.staff_img from user_add_staff_info s")
        value = cursor.fetchall()
        staff_id = request.GET.get('s_id')
        page = request.GET.get('page')
        email = request.GET.get('email')
        if page == 'dlt':
            delt = add_staff_info.objects.filter(id=staff_id)
            delt.delete()
            dlt_user = User.objects.filter(email=email)
            dlt_user.delete()
            cursor.execute("Select s.id, s.staff_name, s.staff_mob_no, s.staff_email, s.staff_pass, s.staff_img from user_add_staff_info s")
            value = cursor.fetchall()
            return render(request, 'ladmin/a_staff.html', {"value": value})
        return render(request, 'ladmin/a_staff.html', {"value":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_add_staff(request):
    if request.user.is_authenticated:
        status = ""
        if request.method == 'POST':
            if request.POST.get("sf_password") == request.POST.get("sf_con_password"):
                Name = request.POST.get("sf_name")
                Mob_no = request.POST.get("sf_mob_no")
                Email = request.POST.get("sf_email")
                Password = request.POST.get("sf_password")
                Img = request.FILES.get("sf_img")
                res = add_staff_info(staff_name=Name,staff_mob_no=Mob_no,staff_email=Email,staff_pass=Password,staff_img=Img)
                res.save()
                myuser = User.objects.create_user(Email, Email, Password)
                myuser.first_name = Name
                myuser.last_name = Name
                myuser.save()
                status = "Staff Added Successfully."
            else:
                status = "Password and Confirm password does not matched."
        return render(request, 'ladmin/a_add_staff.html', context={"S":status})
    else:
        return render(request, 'ladmin/a_login.html')

def a_update_staff(request):
    if request.user.is_authenticated:
        staff_id = request.GET.get('s_id')
        email = request.GET.get('email')
        s_detail = add_staff_info.objects.filter(id=staff_id)
        status = ""
        if request.method == 'POST':
            s_detail.staff_name = request.POST.get("sf_name")
            s_detail.staff_mob_no = request.POST.get("sf_mob_no")
            #Email = request.POST.get("sf_email")
            s_detail.staff_img = request.FILES.get("sf_img")
            s_detail.save()
            ##res.save()
            #myuser = User.objects.filter(email=email)
            #myuser.first_name = Name
            #myuser.last_name = Name
            #myuser.save()
            status = "Staff Updated Successfully."
            print(status)
            return render(request, 'ladmin/a_edit_staff.html', {"s_detail": s_detail, "S": status})
        return render(request, 'ladmin/a_edit_staff.html', {"s_detail": s_detail, "S": status})
    else:
        return render(request, 'ladmin/a_login.html')

def a_student(request):
    if request.user.is_authenticated:
        value = add_student_info.objects.all().order_by("-st_roll_no")
        page = request.GET.get('page')
        roll_no = request.GET.get('roll_no')
        if page == 'dlt':
            delt = add_student_info.objects.filter(st_roll_no=roll_no)
            delt.delete()
            value = add_student_info.objects.all().order_by("-st_roll_no")
        return render(request, 'ladmin/a_student.html', {"data":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_add_student(request):
    if request.user.is_authenticated:
        status = ""
        cursor = connection.cursor()
        cursor.execute("Select c.id, c.course_name, c.branch_name from user_add_section_info c order by c.id desc")
        value = cursor.fetchall()
        if request.method == 'POST':
            Roll_no = request.POST.get("st_roll_no")
            Name = request.POST.get("st_name")
            Mob_no = request.POST.get("st_mob_no")
            Email = request.POST.get("st_email")
            Course = request.POST.get("st_course")
            Branch = request.POST.get("st_branch")
            Year = request.POST.get("st_year")
            Dob = request.POST.get("st_dob")
            Img = request.FILES.get("st_img")
            res = add_student_info(st_roll_no=Roll_no, st_name=Name, st_mob_no=Mob_no, st_email=Email, st_course=Course, st_branch=Branch, st_year=Year, st_dob=Dob, st_img=Img)
            res.save()
            status = "Student Added Successfully."
            return render(request, 'ladmin/a_add_student.html', {"value": value, "S":status})
        return render(request, 'ladmin/a_add_student.html', {"value": value, "S":status})
    else:
        return render(request, 'ladmin/a_login.html')

def a_update_student(request):
    if request.user.is_authenticated:
        roll_no = request.GET.get('roll_no')
        cursor = connection.cursor()
        cursor.execute("Select c.id, c.course_name, c.branch_name from user_add_section_info c order by c.id desc")
        value = cursor.fetchall()
        st_details = add_student_info.objects.filter(st_roll_no=roll_no)
        return render(request, 'ladmin/a_update_student.html', {"st_details":st_details, "value":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_book(request):
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("Select b.book_no, b.book_name, b.book_author, b.book_title from user_add_book_info b order by b.book_no desc")
        value = cursor.fetchall()
        book_id = request.GET.get('b_id')
        page = request.GET.get('page')
        if page == 'dlt':
            delt = add_book_info.objects.filter(book_no=book_id)
            delt.delete()
            cursor.execute("Select b.book_no, b.book_name, b.book_author, b.book_title from user_add_book_info b order by b.book_no desc")
            value = cursor.fetchall()
            return render(request, 'ladmin/a_book.html', {"value": value})
        return render(request, 'ladmin/a_book.html', {"value":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_add_book(request):
    if request.user.is_authenticated:
        status = ""
        if request.method == 'POST':
            Book_no = request.POST.get("b_no")
            Book_name = request.POST.get("b_name")
            Book_author = request.POST.get("b_author")
            Book_title = request.POST.get("b_title")
            res = add_book_info(book_no=Book_no, book_name=Book_name, book_author=Book_author, book_title=Book_title)
            res.save()
            status = "Book Added Successfully."
        return render(request, 'ladmin/a_add_book.html', context={"S":status})
    else:
        return render(request, 'ladmin/a_login.html')

def a_update_book(request):
    if request.user.is_authenticated:
        book_id = request.GET.get('b_id')
        b_details = add_book_info.objects.filter(book_no=book_id)
        return render(request, 'ladmin/a_update_book.html', {"b_details":b_details})
    else:
        return render(request, 'ladmin/a_login.html')

def a_course(request):
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("Select c.id, c.course_name, c.branch_name from user_add_section_info c order by c.id desc")
        value = cursor.fetchall()
        course_id = request.GET.get('c_id')
        page = request.GET.get('page')
        if page == 'dlt':
            delt = add_section_info.objects.filter(id=course_id)
            delt.delete()
            cursor.execute("Select c.id, c.course_name, c.branch_name from user_add_section_info c order by c.id desc")
            value = cursor.fetchall()
            return render(request, 'ladmin/a_course.html', {"value": value})
        return render(request, 'ladmin/a_course.html', {"value":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_add_course(request):
    if request.user.is_authenticated:
        status = ""
        if request.method == 'POST':
            c_name = request.POST.get("c_name")
            br_name = request.POST.get("br_name")
            res = add_section_info(course_name=c_name, branch_name=br_name)
            res.save()
            status = "Course Added Successfully."
        return render(request, 'ladmin/a_add_course.html', context={"S":status})
    else:
        return render(request, 'ladmin/a_login.html')

def a_update_course(request):
    if request.user.is_authenticated:
        course_id = request.GET.get('c_id')
        c_details = add_section_info.objects.filter(id=course_id)
        return render(request, 'ladmin/a_update_course.html', {"c_details":c_details})
    else:
        return render(request, 'ladmin/a_login.html')

def a_setting(request):
    if request.user.is_authenticated:
        return render(request, 'ladmin/a_setting.html')
    else:
        return render(request, 'ladmin/a_login.html')

def a_add_day_fee(request):
    if request.user.is_authenticated:
        status = ""
        value = add_day_and_fee.objects.all()
        if request.method == 'POST':
            issue_day = request.POST.get("issue_day")
            penalty = request.POST.get("penalty")
            res = add_day_and_fee.objects.get(id=1)
            res.issue_day = issue_day
            res.penalty = penalty
            res.save()
            status = "Updated Successfully."
        return render(request, 'ladmin/a_add_day_fee.html', context={"S": status, "data":value})
    else:
        return render(request, 'ladmin/a_login.html')

def a_log_out(request):
    logout(request)
    return render(request, 'ladmin/a_login.html')