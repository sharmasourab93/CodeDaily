from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class defaultDB(models.Model):
	"When Supply from MainDB is cut off"
	s_no=models.IntegerField(default="")
	address=models.URLField(max_length=300)

	def __str__(self):
		return self.s_no+'-'+self.address

class MainDB(models.Model):
	s_no=models.IntegerField(default="")
	address=models.URLField(max_length=300)
	auto_date=models.DateTimeField(auto_now_add=False)
	timeA=models.TimeField(auto_now_add=False, auto_now=False)
	timeB=models.TimeField(auto_now_add=False, auto_now=False)

	def get_absolute_url(self):
		return reverse(request,'UI:detail',kwargs={'pk': self.pk})
	def __str__(self):
		return self.s_no+'-'+ self.address +'-'+self.auto_date