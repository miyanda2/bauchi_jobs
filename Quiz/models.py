from django.db import models
from django.contrib.auth.models import User

from .forms import RegisterForm


from django.urls import reverse
 
 
class User1(models.Model):
 
    #the variable to take the inputs
    user_name = models.CharField(max_length=100)
    user_avatar = models.FileField()
 
    # on submit click on the user entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('uploadfileapp:home')

class Profile(models.Model):
    name = models.CharField(max_length = 50, default='DEFAULT VALUE')
    cv = models.FileField(upload_to='cv /%Y/%m/%d')
    class Meta:
        db_table = "cv"

class Quiz(models.Model):
    date_created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=30)
    no_of_ques = models.IntegerField(default=0)
    taken_by = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    users = models.ManyToManyField(User, through='Score', related_name='quizzes')

    def __str__(self):
        return self.quiz_name

class Score(models.Model):
    score = models.IntegerField()
    taken_on = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_no = models.IntegerField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    right_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
