from django.db import models

# Create your models here.

class Article(models.Model):
	title=models.TextField(max_length=254)
	body=models.TextField()
	likes=models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	article=models.ForeignKey(Article,on_delete=models.CASCADE)
	text=models.TextField()