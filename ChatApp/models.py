from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200,primary_key = True)
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    create_date = models.DateTimeField('User creation Date')
    is_active = models.IntegerField()
    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField('Group Creation Date')
    is_active = models.IntegerField()
    def __str__(self):
        return self.name

class UserGroup(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)
    
class Friendship(models.Model):
    user_A = models.ForeignKey(User,related_name="user_A",on_delete=models.CASCADE)
    user_B = models.ForeignKey(User,related_name = "user_B",on_delete=models.CASCADE)
    def __str__(self):
        return self.user_A,self.user_B

class Report(models.Model):
    reported_user = models.ForeignKey(User,on_delete=models.CASCADE)
    report_date = models.DateTimeField('Report Creation Date')
    report_reason = models.CharField(max_length=200)

class Message(models.Model):
     creator_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator_id")
     recipient_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="received_messages")
     message_body = models.CharField(max_length=1000)
     create_date = models.DateTimeField('Message Creation Date')
     def __str__(self):
         return self.message_body