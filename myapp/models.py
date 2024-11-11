from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"Entry by {self.user.username} on {self.date}"

class SuggestedContent(models.Model):
    diary_entry = models.ForeignKey(DiaryEntry, on_delete=models.CASCADE)
    suggestion = models.TextField()

    def __str__(self):
        return f"Suggestion for Entry {self.diary_entry.id}"
