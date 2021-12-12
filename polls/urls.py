from django.urls import path

from . import views
from .factories import RetrieveMembersUseCaseFactory
from .infrastructure.rest.ViewWrapper import ViewWrapper

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/<int:question_id2>', ViewWrapper.as_view(usecaseFactory=RetrieveMembersUseCaseFactory()) ),
    path('<int:question_id>/<int:question_id2>',
         ViewWrapper.as_view(usecaseFactory=RetrieveMembersUseCaseFactory())),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

