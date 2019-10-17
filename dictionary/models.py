from django.db import models

class Entry(models.Model):
    """dictionary entry"""
    #  created = models.DateTimeField (auto_now_add= True)
    text = models.CharField (max_length = 100, unique = True)
