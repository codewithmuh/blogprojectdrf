from django.db import models
import uuid
from django.contrib.auth.models import User



# > This class is an abstract class that will be inherited by all other models. It will add a UUID
# field, a created_at field, and an updated_at field to all models that inherit from it
class BaseModel(models.Model):
    uid =models.UUIDField(primary_key=True, editable= False, default= uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        
  
# The Blog class inherits from the BaseModel class, and has a one-to-many relationship with the User class      
class Blog(BaseModel):
    user =  models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog_text= models.TextField()  
    main_image = models.FileField()   
        
    def __str__(self):
        return self.title