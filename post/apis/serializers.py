from ..models import Post
from rest_framework import serializers
from django.contrib.humanize.templatetags import humanize

class PostSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Post
        exclude = ('user',)

    def save(self, **kwargs):
        self.validated_data['user'] = self.context['user']
        post = Post.objects.create(**self.validated_data)
        post.save()
        return post
    
    def to_representation(self, instance:Post):
        data = super().to_representation(instance)
        data['created_at'] = humanize.naturaltime(instance.created_at)
        data['user'] = {
            'full_name' : instance.user.full_name,
            'phonenumber' : instance.user.phonenumber,
        }
        return data