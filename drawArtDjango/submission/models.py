# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Submission(models.Model):

    name = models.CharField(max_length=200)
    info = models.TextField(max_length=200)
    feelings = models.CharField(max_length=200)
    email = models.EmailField(max_length=150, blank=False, null=True)

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.info, self.feelings)
