from django.conf.urls import patterns, url

from .views import PersonCreateView, PersonUpdateView, PersonDetailView, PersonResultsView, PersonListView
from .views import DocumentDetailView, DocumentListView, DocumentUpdateView, AffidavitScrapView


urlpatterns = patterns("",
                       url(
                       regex=r"^$",
                       view=PersonListView.as_view(),
                       name="index"
                       ),
                       url(
                       regex=r"^(?P<pk>\d+)/$",
                       view=PersonDetailView.as_view(),
                       name="detail"
                       ),
                       url(
                       regex=r"^(?P<pk>\d+)/results/$",
                       view=PersonResultsView.as_view(),
                       name="results"
                       ),

                       # Documents
                       url(
                       regex=r"^document$",
                       view=DocumentListView.as_view(),
                       name="document-index"
                       ),

                       url(
                       regex=r"^document/(?P<pk>\d+)/$",
                       view=DocumentUpdateView.as_view(),
                       name="document-update"
                       ),
# Affidavit

                       url(
                       regex=r"^affidavit/(?P<pk>\d+)/$",
                       view=AffidavitScrapView.as_view(),
                       name="affidavit-scrap"
                       ),

                       )
