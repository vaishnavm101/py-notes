from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base_route(request):
    print("Request came to the base route....")
    # return HttpResponse("<h1>Heading</h1>")
    return render(request, "home.html")
    

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


def get_student_detail(request, student_name):
    students = {"yusuf": "Yusuf Shaikh", "adesh": "Adesh T"}
    if student_name in students:
        context = {
            "student": students[student_name]
        }
        return render(request, "student_details.html", context=context)
    context = {
        "student": "Not found"
    }
    return render(request, "student_details.html", context)