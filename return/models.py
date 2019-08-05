from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 
    
    
    def __str__(self):
            return self.user.username
    class Meta:
        ordering =['bio']
    
    def save_profile(self):
        self.save()
    def update_profile(self):
        self.update()
    def delete_profile(self):
        self.delete()

class Project(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    description = models.CharField(max_length =200)
    link = models.URLField(blank=True, null=True)
    ratings = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
            ordering =['pub_date']
    
    

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    @classmethod
    def search_project(cls, repos):
        project = cls.objects.filter(title__icontains=repos)
        return project
    @classmethod
    def filter_by_user_id(cls,user_id):
        projects = Project.objects.filter(profile=user_id)
        return projects
