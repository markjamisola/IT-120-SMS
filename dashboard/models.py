from django.db import models

from twilio.rest import Client
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'AC8ce7ccad83244fdf629c36e47fe8d29e'
            auth_token = '731534ef44f9428fd893233279a3f35b'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name}, your score is {self.score}",
                from_='+17753733918',
                to='+639282402911'
            )
        else:
            account_sid = 'AC8ce7ccad83244fdf629c36e47fe8d29e'
            auth_token = '731534ef44f9428fd893233279a3f35b'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Sorry {self.name}, your score is {self.score}. Try again",
                from_='+17753733918',
                to='+639282402911'
            )

        print(message.sid)
        return super().save(*args, **kwargs)