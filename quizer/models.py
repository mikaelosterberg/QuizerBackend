from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Question(models.Model):
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, db_index=True)
    stopDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, db_index=True)
    resultDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    region = models.CharField(max_length=3, default='INT', db_index=True)
    language = models.CharField(max_length=10, default='en', db_index=True)
    questionText = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/question', null=True, blank=True)

    def __str__(self):
        return self.questionText

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.questionText)
        super(Question, self).save(*args, **kwargs)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, db_index=True)
    choiceText = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/choice', null=True, blank=True)

    def __str__(self):
        return self.choiceText

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.choiceText)
        super(Choice, self).save(*args, **kwargs)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    answerDateTime = models.DateTimeField(auto_now_add=True)

    region = models.CharField(max_length=3, db_index=True)
    gender = models.CharField(max_length=1, db_index=True)


class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    region = models.CharField(max_length=3, db_index=True)
    gender = models.CharField(max_length=1, db_index=True)

    number = models.BigIntegerField(default=0)
    percent = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)
    total = models.BigIntegerField(default=0)
