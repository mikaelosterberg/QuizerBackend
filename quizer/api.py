from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializers import AnswerSerializer, ChoiceSerializer, QuestionSerializer, ResultSerializer
from .models import Result, Answer, Choice, Question
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAnswerOwner
import datetime


@permission_classes((IsAuthenticated,))
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(stopDate__gte=datetime.date.today()).filter(startDate__lte=datetime.date.today())
    serializer_class = QuestionSerializer
    lookup_field = 'slug'


@permission_classes((IsAuthenticated, IsAnswerOwner))
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAnswerOwner,)

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@permission_classes((IsAuthenticated,))
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = 'slug'


@permission_classes((IsAuthenticated,))
class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    read_only=True
