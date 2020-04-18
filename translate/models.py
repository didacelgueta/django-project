from django.db import models
from django.contrib.auth.models import User

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
)


class Translate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang_1 = models.CharField(max_length=2, verbose_name=u"Source Language", choices=LANGUAGES)
    text = models.CharField(max_length=500)
    lang_2 = models.CharField(max_length=2, verbose_name=u"Target Language", choices=LANGUAGES)

    def __str__(self):
        return "{}. {}".format(self.user, self.lang_1)

class Result(models.Model):
    id_translate = models.IntegerField(default=0)
    translated_text = models.CharField(max_length=500)
