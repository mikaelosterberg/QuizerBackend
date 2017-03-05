from rest_framework import  serializers
from .models import Question, Choice, Answer, Result
import datetime


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        if data['startDate'] > data['stopDate']:
            raise serializers.ValidationError("stop date must occur after start date")

        if data['stopDate'] > data['resultDate']:
            raise serializers.ValidationError("result date must occur after stop date")

        return data

    class Meta:
        model = Question
        fields = ('startDate', 'stopDate', 'resultDate', 'region', 'language', 'questionText', 'image', 'slug')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.filter(stopDate__gte=datetime.date.today()).filter(startDate__lte=datetime.date.today())
        )
    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())

    def validate(self, data):
        if data['choice'].question.id != data['question'].id:
            raise serializers.ValidationError("choice don't belong to the question")
        return data

    class Meta:
        model = Answer
        fields = ('choice', 'question', 'answerDateTime', 'region', 'gender')


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.filter(stopDate__gte=datetime.date.today()).filter(startDate__lte=datetime.date.today())
    )

    class Meta:
        model = Choice
        fields = ('question', 'choiceText', 'image', 'slug')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.filter(stopDate__gte=datetime.date.today()))
    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())

    class Meta:
        model = Result
        fields = ('question', 'choice', 'region', 'gender', 'number', 'percent', 'total')
