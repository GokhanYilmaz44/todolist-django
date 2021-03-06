from django.utils import timezone
from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Todo(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ["created_at"]

    def __str__(self):
        return self.title


