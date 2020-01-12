from django.db import models
from django.utils import timezone



################### novel ###################

class Novel(models.Model):
	title = models.CharField(
		max_length=100
    )
	novel_comment = models.CharField(
		max_length=200
	)
	
	novel_summary = models.TextField(
		max_length=3000
	)
	
	novel_status = models.CharField(
		max_length=5,
		default='rensaichuu'
	)
	
	novel_category = models.CharField(
		max_length=5,
		default='tyouhen'
	)
    
	total_page = models.IntegerField(
    	default=999
	)
	total_chapter = models.IntegerField(
		default=999
	)
	created_at = models.DateTimeField(
		default=timezone.now
	)
	updated_at = models.DateTimeField(
        default=timezone.now
	)
	def __str__(self):
		return self.title


################### chapter ###################

class Chapter(models.Model):
	title = models.ForeignKey(
		'Novel',
		on_delete=models.CASCADE
	)
	chapter_title = models.CharField(
        	max_length=200
	)
	chapter_id = models.IntegerField(
		default=999
	)
	page_count = models.IntegerField(
		default=999
	)
	chapter_content = models.TextField()

	created_at = models.DateTimeField(
		default=timezone.now
	)
	updated_at = models.DateTimeField(
		default=timezone.now
	)
	def __str__(self):
		return "{}-{}-{}".format(self.title,self.chapter_id,self.chapter_title)


################### diary_category ###################
class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            post_count=models.Count('diary_contents')
        )


class Diary_Category(models.Model):
	category = models.CharField(
		max_length=20
	)
	objects = CategoryManager()
	def __str__(self):
		return self.category


################### diary_contents ###################

class Diary_Contents(models.Model):
	title = models.CharField(
		max_length=100
	)

	category = models.ForeignKey(
		'Diary_Category',
		on_delete=models.CASCADE
    )
	
	daiary_content = models.TextField()
	
	created_at = models.DateTimeField(
		default=timezone.now
    )

	def __str__(self):
		return "{}-{}-{}".format(self.created_at, self.category, self.title)



