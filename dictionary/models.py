from django.db import models

class Entry(models.Model):
    """dictionary entry"""
    #  created = models.DateTimeField (auto_now_add= True)
    text = models.CharField (max_length = 100, unique = True)
    length = models.IntegerField (null=True)

    def __repr__(self):
        return f"<Entry text:{self.text}>"
    
    def __str__(self):
        return f"{self.text}"
