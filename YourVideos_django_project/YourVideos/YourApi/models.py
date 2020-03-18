from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    
    def average_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(Video=self)
        for rating in ratings:
            sum = sum + rating.stars
            print(sum)
        if len(ratings) >0:
            return sum/len(ratings)
        else:
            return 0


    def comments_list(self):
        allcomments = Rating.objects.filter(video=self)
        list_of_all_comments = []
        for comments in allcomments:
            list_of_all_comments.append(comments.comments)
        return list_of_all_comments


    

class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    def __str__(self):
        return self.stars

    class Meta:
        unique_together = (('user', 'video'))
        index_together = (('user', 'video'))