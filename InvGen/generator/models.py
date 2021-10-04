from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension

class CustomTemplate(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    docfile = models.FileField(upload_to='user_templates/%Y/%m/%d', validators=[validate_file_extension])

    def __str__(self):
        return str(self.owner)


class Invitation(models.Model):

    INVITATION_TEMPLATES = [
    ('black', 'Black'),
    ('happy', 'Happy'),
    ('funny', 'Funny'),
    ('love', 'Love'),
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    p_from = models.CharField(max_length=40, blank=True)
    p_to = models.CharField(max_length=40,blank=True )
    place = models.CharField(max_length=60,blank=True)
    invitation_date = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True)
    template = models.CharField(max_length=50, choices=INVITATION_TEMPLATES,blank=True)
    is_formal = models.BooleanField(blank=True)
    template_name = models.ForeignKey(CustomTemplate, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        if self.owner:
            return "USER: "+str(self.owner)+ " To:" + str(self.p_from)
        else:
            return str(self.p_from)

