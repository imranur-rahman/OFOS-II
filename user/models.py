from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    instance.cart.save()


class CartItem(models.Model):
    food_id = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    # password = models.CharField(max_length=30)
    # an object for cart for the user is needed here, to be added to base.html cart field

    def __str__(self):
        return self.email.__str__()


class Area(models.Model):
    # thana actually
    name = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    postal_code = models.PositiveIntegerField()

    def __str__(self):
        return self.name.__str__()


class Rating(models.Model):
    number_of_users_rated = models.IntegerField()
    sum_of_rating = models.IntegerField()
    average = models.FloatField(default=0.0)


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.__str__() + ', ' + self.area.name.__str__()


class Food(models.Model):
    CUISINES = (
        ('MF', 'Mexican Food'),
        ('IC', 'Italian Cuisine'),
        ('IF', 'Indian Food'),
        ('CF', 'Cajun Food'),
        ('SF', 'Soul Food'),
        ('TF', 'Thai Food'),
        ('GF', 'Greek Cuisine'),
        ('CHF', 'Chinese Food'),
        ('LC', 'Lebanese Cuisine'),
        ('JC', 'Japanese Cuisine'),
        ('AF', 'American Food'),
        ('MF', 'Moroccan Food'),
        ('MC', 'Mediterranean Cuisine'),
        ('FF', 'French Food'),
        ('SC', 'Spanish Cuisine'),
        ('GF', 'German Food'),
        ('KF', 'Korean Food'),
        ('VF', 'Vietnamese Food'),
        ('TC', 'Turkish Cuisine'),
        ('CRF', 'Caribbean Food'),
    )

    name = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    time_needed = models.DurationField()
    category = models.CharField(max_length=3, choices=CUISINES)
    rating = models.ForeignKey(Rating)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)

    def __str__(self):
        return '{}  {}  {}'.format(self.name, self.restaurant.name, self.time_needed.__str__())
