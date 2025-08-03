from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)


class OrderPizza(models.Model):
    size_choice = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    buying_at = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=10, choices=size_choice, default='small')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


# def __str__(self):
#     return f"Order {self.id} - {self.user.username}"

    # def save(self, *args, **kwargs):
    #     # Auto-calculate total price based on size and quantity
    #     if self.size == 'small':
    #         price = self.pizza.small_price
    #     elif self.size == 'medium':
    #         price = self.pizza.medium_price
    #     else:
    #         price = self.pizza.large_price
    #
    #     self.total_price = price * self.quantity
    #     super().save(*args, **kwargs)