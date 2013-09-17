# Create your views here.

from django.views.generic import CreateView, UpdateView, DetailView, ListView

#from braces.views import LoginRequiredMixin

from .models import Person


class PersonCreateView(CreateView):
    model = Person


# class PersonUpdateView(LoginRequiredMixin, UpdateView):
class PersonUpdateView(UpdateView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class PersonResultsView(PersonDetailView):
    template_name = "person/results.html"


class PersonListView(ListView):
    model = Person
    template_name = "person/list.jade"
