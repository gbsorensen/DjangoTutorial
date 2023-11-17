from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from .forms import PersonForm
from .models import Person


'''this is a class view'''
class PersonListView(ListView):
    model = Person
    paginate_by = 100 #how many objects are in a page
    template_name = "myapp/person.html" #html template that we will use for this page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now
        return context
    
class PersonDetailView(DetailView):
    model = Person
    template_name = "myapp/person_detail.html"

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/person_create.html"
    success_url = "/"
    
"""
    'CreateView' - A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
    'DeleteView' - A view that displays a confirmation page and deletes an existing object. 
    'DetailView' - A view for a specific object based on its ID
    'ListView' - Show a list/array of objects in a View
    'UpdateView' - A view that displays a form for updating an object, redisplaying the form with validation errors (if there are any) and saving the object.
"""