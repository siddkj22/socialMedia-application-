from django.db import models

# Create your models here.



class HashTag(models.Model):
    """A topic the user wants to post"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of model"""
        return self.text 

    
class Entry(models.Model):
    """Something specific learned about a topic """
    twit = models.ForeignKey(HashTag,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'twits'

    def __str__(self):
        """return a string of model"""
        return f"{self.text[:50]}..."

        