from django.shortcuts import render
from .models import School

my_school = School("Django School")

# Create your views here.
def index(request):
    my_data = {
        "school_name": my_school.name
    }
    
    return render(request, "school_roster_app/index.html", my_data)

def list_staff(request):
    
    my_data = {
        "school_name": my_school.name,
        "staff": my_school.staff
    }

    return render(request, "school_roster_app/list_staff.html", my_data)

def staff_detail(request, employee_id):
    staff = my_school.find_staff_by_id(employee_id)
    my_data = {
        "school_name": my_school.name,
        "staff": staff
    }
            
    return render(request, "school_roster_app/staff_detail.html", my_data)

def list_students(request):
    my_data = {
        "school_name": my_school.name,
        "students": my_school.students
    }
    return render(request,"school_roster_app/list_students.html", my_data )

def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)

    my_data = {
        "School_name": my_school.name,
        "student": student
    }
    return render(request, "school_roster_app/student_detail.html", my_data)