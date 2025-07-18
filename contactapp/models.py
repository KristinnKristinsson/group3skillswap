from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class ContactMessage(models.Model):
    sender= models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recieved_messages', on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.AddSkills', related_name="skills_interested", on_delete=models.CASCADE)
    email= models.EmailField()  
    message= models.TextField()
    submitted_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient} asking for ({self.skill})"
