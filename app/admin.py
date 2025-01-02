from django.contrib import admin
from .models import User, Borrowing, Feedback, Item, Reminder

admin.site.register(User)
admin.site.register(Borrowing)
admin.site.register(Feedback)
admin.site.register(Item)
admin.site.register(Reminder)