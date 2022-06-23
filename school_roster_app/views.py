from django.shortcuts import render
from .models import School

my_school = School("Django School")

# Create your views here.
def index(request):
    my_data = {
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)

def list_staff(request):
    pass

def staff_detail(request):
    pass

def list_students(request):
    pass

def student_detail(request):
    pass