from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    category=models.ManyToManyField(Category)
    borrowing_price=models.DecimalField(max_digits=12,decimal_places=2)
    image=models.ImageField(upload_to='books/media/uploads')

    def __str__(self) -> str:
        return self.title
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    review=models.TextField()
    review_date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username}-{self.book.title}'