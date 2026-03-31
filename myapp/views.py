from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        Person.objects.create(
            name=name,
            age=age
        )
        
        return redirect("/")
    else:
        return render(request, "form.html")

def index(request):
    persons = Person.objects.all()
    return render(request, "index.html", {"persons": persons})

def delete(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect("/")
