# -*- coding: utf-8 -*-
# Create your views here.

from django.views.generic import CreateView, UpdateView, DetailView, ListView, FormView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from django.core.urlresolvers import reverse


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


class DocumentEditMixin(object):
    template_name = "document/form.jade"
    #form_class = DocumentForm
    model = Document

    def get_success_url(self):
        return reverse('document-detail', kwargs={'pk': self.object.pk})


class DocumentCreateView(DocumentEditMixin, CreateView):
    pass


class DocumentUpdateView(DocumentEditMixin, UpdateView):
    pass


class DocumentDetailView(DocumentEditMixin, DetailView):
    template_name = "document/detail.jade"
    model = Document


class DocumentListView(ListView):
    model = Document
    template_name = "document/list.jade"


class AffidavitUpdateView(UpdateView):
    model = Affidavit
    template_name = "affidavit/update.jade"
    form_class = AffidavitForm


class AffidavitScrapView(UpdateView):
    model = Affidavit
    template_name = "affidavit/scrap.jade"
    #form_class = AffidavitForm

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)

        try:
            obj = queryset.get_or_create(original_document_id=pk)
        except ObjectDoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj



#     def get_object(self, queryset=None):
#         import ipdb
#         ipdb.set_trace()
#         return super(CreateView)
# Si no existe, debería crearlo (con el id)
