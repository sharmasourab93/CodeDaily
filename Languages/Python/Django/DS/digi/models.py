from django.db import models

# Create your models here.
class MainDB(models.Model):
	urls_db=models.URLField(max_length=300)
	totalTime=models.IntegerField()
	def __unicode__(self):
		return self.url +'   '+ self.totalTime
