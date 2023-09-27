from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberCreationForm
from .models import Member, Course,Department


def index(request):

    department=Department.objects.all()
    d={'department':department}

    return render(request,"index.html",d)

def create_view(request):

    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Order placed")
            return redirect('add')
    return render(request, 'home.html', {'form': form})


def update_view(request, pk):

    member = get_object_or_404(Member, pk=pk)
    form = MemberCreationForm(instance=member)
    if request.method == 'POST':
        form = MemberCreationForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_courses(request):

    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request,'course_list.html',{'courses': courses})


