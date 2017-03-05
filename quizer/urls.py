from django.conf.urls import url, include
from rest_framework import routers
from .api import AnswerViewSet, ChoiceViewSet, QuestionViewSet, ResultViewSet

router = routers.DefaultRouter()

router.register(r'answer', AnswerViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'result', ResultViewSet)
print (router.urls)
urlpatterns = [
    url(r'^v1.0/', include(router.urls)),
    ]
