from django.db import models
class userreg(models.Model):
    profilepic=models.FileField(upload_to='profilepic/',blank=True,null=True)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=10) 

class product(models.Model):
     productname=models.CharField(max_length=30)
     productprice=models.IntegerField()
     category=models.CharField(max_length=30)
     description=models.CharField(max_length=100)
     image=models.FileField(upload_to='productpic/',blank=True,null=True)
     
     
class PostModel(models.Model):
    user=models.ForeignKey(userreg,on_delete=models.CASCADE,blank=True)
    post_pic = models.FileField(upload_to='post_pics/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    likes_count= models.IntegerField(null=True,blank=True)
    liked_users = models.ManyToManyField(userreg,related_name='liked_posts',null=True)
    

class CommentSectionModel(models.Model):
    user=models.ForeignKey(userreg,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    comment=models.TextField()
# Create your models here.