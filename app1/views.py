from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base_route(request):
    print("Request came to the base route....")
    # return HttpResponse("<h1>Heading</h1>")
    return render(request, "home.html")
    

def get_students(request):
    # students = ["Adesh", "Yusuf", "Raj"]
    student1 = "Yash"
    context = {
        "student1": student1
    }
    return render(request, "students.html", context=context)