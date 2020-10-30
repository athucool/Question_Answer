from django.urls import path,include
from rest_framework.routers import DefaultRouter

from questions.api import views as qv 
from .views import AnswerCreateViewSet,AnswerListApiView,AnswerupdateAPIview,AnswerlikeApiView
router = DefaultRouter()
router.register(r"questions",qv.QuestionViewSet)

urlpatterns = [
    path("",include(router.urls)),
    path("questions/<slug:slug>/answer/",AnswerCreateViewSet.as_view(),name="create_Ans"),
    path("questions/<slug:slug>/answers/",AnswerListApiView.as_view(),name="answerlist"),
    path("answers/<int:pk>/",AnswerupdateAPIview.as_view(),name="ans-update"),
    path("answers/<int:pk>/like/",AnswerlikeApiView.as_view(),name="ans-like")
  ]
