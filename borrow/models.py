from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.

class Borrow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date= models.DateField(auto_now_add=True)
    balance_after_borrow= models.DecimalField(max_digits=12, decimal_places=2)
    is_returned= models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username}-{self.book.title}'