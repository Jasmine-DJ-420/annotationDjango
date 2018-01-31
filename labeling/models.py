from django.db import models

class IssueText(models.Model):
    issue_text = models.TextField()
    id = models.IntegerField(default=-1,primary_key=True)
    old_id = models.IntegerField(default=-1)
    url = models.CharField(max_length=200)
    issue_or_comment = models.CharField(max_length=200)

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    page = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class EmotionChoice(models.Model):
    issue = models.ForeignKey(IssueText)
    choice_text = models.CharField(max_length=200)
    user = models.ForeignKey(User)