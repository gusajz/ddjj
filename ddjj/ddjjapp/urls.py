from django.conf.urls import patterns, url

from .views import PersonCreateView, PersonUpdateView, PersonDetailView, PersonResultsView, PersonListView


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
                       )
