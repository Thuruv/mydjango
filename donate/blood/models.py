from django.db import models
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#_

types = ((
    'O+','O-Positive'),
    ('A+','A-Positive'),
    ('O-','O-Negative'),
    ('A-','A-Negative'),
    ('B+','B-Positive'),
    ('B-','B-Negative'),
    ('AB+','AB-Positive'),
    ('AB-','AB-Negative')
)

class Details(models.Model):
    name = models.CharField(max_length = 50)
    btype =models.CharField(choices = types, max_length = 15,blank = True)
    dob = models.DateField()

    full_address = models.CharField(max_length = 256,default = "")
    city = models.CharField(max_length = 20,default = None)
    state  = models.CharField(max_length = 20,default = None)

    phone = models.IntegerField()
    email = models.EmailField(default = None)
    fb  = models.CharField(max_length = 35,default = None)
    twitter = models.CharField(max_length = 20,default = None)

    def __unicode__(self):
        return self.name

class Feedback(models.Model):
    """
    Holds information about one user feedback.
    :user: User account of the poster, if logged in.
    :email: Email field, if user isn't logged in and wants to send her email.
    :current_url: URL of the current page.
    :message: Feedback text.
    :creation_date: Datetime of the feedback creation.
    :content_object: Optional related object the feedback is referring to.
    """

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    message = models.TextField(
        verbose_name=_('Message'),
        max_length=4000,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation Date'),
    )

    # Generic FK to the object this feedback is about
    class Meta:
        ordering = ['-creation_date']

    def __unicode__(self):
            return '{0} - {1}'.format(self.creation_date, self.email)
