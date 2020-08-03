from django.db import models



class Queries(models.Model):
    name = models.CharField(max_length=50)
    query = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(default="Not Answered Yet")
    def __str__(self):
        return self.name