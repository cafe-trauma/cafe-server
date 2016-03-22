from django.db import models
from django.contrib.auth.models import User
# imports for user token creation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Definition():
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

QUESTION_TYPES = (('combo', 'Combo Box'),
                  ('check', 'Check Boxes'),
                  ('text', 'Text Field'),
                  ('int', 'Integer Field'),
                  ('bool', 'Yes or No'))
    
class Question(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    order = models.IntegerField()
    q_type = models.CharField(max_length=5, choices=QUESTION_TYPES)
    options = models.ManyToManyField('Option', blank=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    help_text = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return "{} - {} - {}".format(self.category.id, self.order, self.text[:100])

class Option(models.Model):
    text = models.CharField(max_length=200)
    free = models.BooleanField(default=False)
    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length=50, null=True, blank=True)
    check = models.CommaSeparatedIntegerField(max_length=20, blank=True, null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answer')
    integer = models.IntegerField(null=True, blank=True)
    yesno = models.NullBooleanField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'question')
    def __str__(self):
        return "{} - {}".format(self.user, self.question.id)

class Statement(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    predicate = models.CharField(max_length=255)
    obj = models.CharField(max_length=255)
    choice = models.ForeignKey('Option', on_delete=models.CASCADE, null=True, blank=True)
    value = models.BooleanField()
    def __str__(self):
        return "{} - {} {} {}".format(self.question, self.subject, self.predicate, self.obj)

class RDFPrefix(models.Model):
    prefix = models.CharField(max_length=255)
    def __str__(self):
        return self.prefix
    
# Create user tokens
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
