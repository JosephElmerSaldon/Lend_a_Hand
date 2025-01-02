from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_items')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item_detail', kwargs={"pk": self.pk})

class Borrowing(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_items')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrower.username} borrowed {self.item.name}"

class Reminder(models.Model):
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"Reminder for {self.borrowing.borrower.username} to return {self.borrowing.item.name}"

class Feedback(models.Model):
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.borrowing.item.name}"