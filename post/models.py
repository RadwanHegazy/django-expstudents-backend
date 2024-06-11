from django.db import models
from users.models import User

class Post (models.Model) : 
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='user_post', on_delete=models.CASCADE)
    description = models.TextField()
    building_name = models.CharField(max_length=225)
    room_number = models.CharField(max_length=225)
    floor_number = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.user.full_name
    
    class Meta:
        ordering = ('-created_at',)