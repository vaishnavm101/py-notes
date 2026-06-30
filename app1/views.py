from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student

# Create your views here.

def base_route(request):
    print("Request came to the base route....")
    # return HttpResponse("<h1>Heading</h1>")
   
    return render(request, "home.html")

def view_all_students(request):
    objs = Student.objects.all()
    print(f"Objs: {objs}")
    data = {
        "objs": objs
    }
    return render(request, "view_all_students.html", context=data)



def add_student(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        age = request.POST.get("student_age")
        student = Student.objects.create(
            name=name,
            age=age
        )
        if not student:
            context = {
                "success": False,
                "message": "Error in creating student!"
            }
            return render(request, "add_student.html", context)
        return redirect("view_all_students")

    return render(request, "add_student.html")
    

def get_students(request):
    # students = ["Adesh", "Yusuf", "Raj"]
    student = {
        "name": "Adesh",
        "marks": [70, 87,55]
    }
    context = {
        "student": student
    }
    return render(request, "students.html", context=context)

def get_student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student": student
    }
    return render(request, "student_details.html", context)