from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume


# Create your views here.

def table(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
    form = ResumeForm()
    dict_form = {
        'form': form
    }
    return render(request, 'db.html', dict_form)
