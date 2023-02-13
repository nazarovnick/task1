from django.db import models

# Create your models here.
class news_model(models.Model):
    header = models.CharField(max_length = 200, blank = False)
    date_created = models.DateTimeField(auto_now_add = True)
    description = models.CharField(max_length = 450, blank = False)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.header