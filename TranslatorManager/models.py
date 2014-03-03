from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=200)
    clientContact = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.clientName

class JobType(models.Model):
    client = models.ForeignKey(Client)
    ENGLISH = 'EN'
    FRENCH = 'FR'
    SPANISH = 'ES'
    LANGUAGES = (
        (ENGLISH, 'English'),
        (FRENCH, 'French'),
        (SPANISH, 'Spanish'),
    )

    TRANSLATION = 'Translation'
    REVIEW = 'Review'
    DTP = 'DTP'

    SERVICES = (
        (TRANSLATION, 'Translation'),
        (REVIEW, 'Review'),
        (DTP, 'DTP'),
    )
    languageFrom = models.CharField(max_length=2, choices=LANGUAGES, default=ENGLISH)
    languageTarget = models.CharField(max_length=2, choices=LANGUAGES, default=SPANISH)

    service = models.CharField(max_length=20, choices=SERVICES, default=TRANSLATION)
    #currency = models.
    pay_hourly = models.FloatField(default=0)
    pay_minimum = models.FloatField(default=0)

    #multiply total with this percentage value e.g. 100 * 1.50 (50% rush charge)
    pay_rush = models.FloatField(default=0)

    words_new = models.FloatField(default=0)
    words_fuzzy50 = models.FloatField(default=0)
    words_fuzzy75 = models.FloatField(default=0)
    words_fuzzy85 = models.FloatField(default=0)
    words_fuzzy95 = models.FloatField(default=0)
    words_match = models.FloatField(default=0)
    words_rep = models.FloatField(default=0)
    words_ice = models.FloatField(default=0)



    def __unicode__(self):  # Python 3: def __str__(self):
        if self.service == "DTP":
            return self.service
        else:
            return self.service + "-" + self.languageFrom+"-" + self.languageTarget


class ClientJob(models.Model):
    ENGLISH = 'EN'
    FRENCH = 'FR'
    SPANISH = 'ES'
    LANGUAGES = (
        (ENGLISH, 'English'),
        (FRENCH, 'French'),
        (SPANISH, 'Spanish'),
    )
    TRANSLATION = 'Translation'
    REVIEW = 'Review'
    DTP = 'DTP'

    SERVICES = (
        (TRANSLATION, 'Translation'),
        (REVIEW, 'Review'),
        (DTP, 'DTP'),
    )
    client = models.ForeignKey(Client)
    clientContact = models.CharField(max_length=100)
    languageFrom = models.CharField(max_length=2, choices=LANGUAGES, default=ENGLISH)
    languageTarget = models.CharField(max_length=2, choices=LANGUAGES, default=SPANISH)
    description = models.CharField(max_length=300)
    service = models.CharField(max_length=20, choices=SERVICES, default=TRANSLATION)
    deadLine = models.DateTimeField()
    #currency = models.
    hours_Spent = models.FloatField(default=0)
    words_new = models.FloatField(default=0)
    words_fuzzy50 = models.FloatField(default=0)
    words_fuzzy75 = models.FloatField(default=0)
    words_fuzzy85 = models.FloatField(default=0)
    words_fuzzy95 = models.FloatField(default=0)
    words_match = models.FloatField(default=0)
    words_rep = models.FloatField(default=0)
    words_ice = models.FloatField(default=0)
    #multiply total with this percentage value e.g. 100 * 1.50 (50% rush charge)
    pay_rush = models.FloatField(default=0)


    def __unicode__(self):
        if self.service == "DTP":
            return self.service
        else:
            return self.service + "-" + self.languageFrom+"-" + self.languageTarget