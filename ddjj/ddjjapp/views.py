# Create your views here.

from django.views.generic import CreateView, UpdateView, DetailView, ListView, FormView

#from braces.views import LoginRequiredMixin

from .models import Person, Document, Affidavit

from .forms import DocumentForm, AffidavitForm


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


class DocumentUpdateView(UpdateView):
    model = Document
    template_name = "document/update.jade"
    form_class = DocumentForm


class DocumentDetailView(DetailView):
    model = Document
    template_name = "document/detail.jade"
    form_class = DocumentForm


class DocumentListView(ListView):
    model = Document
    template_name = "document/list.jade"


class AffidavitUpdateView(UpdateView):
    model = Affidavit
    template_name = "affidavit/update.jade"
    form_class = AffidavitForm


class AffidavitScrapView(FormView):
    model = Affidavit
    template_name = "affidavit/scrap.jade"
    form_class = AffidavitForm
