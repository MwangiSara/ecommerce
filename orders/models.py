from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# customers
class CustomerManager(BaseUserManager):
    """Manager for custom Customer model."""
    
    def create_user(self, email, username, password=None, **extra_fields):
        """Create and save a regular customer with an email and username."""
        if not email:
            raise ValueError("Please set a valid email")
        if not username:
            raise ValueError("Please set a valid username")
        
        email = self.normalize_email(email)
        customer = self.model(email=email, username=username, **extra_fields)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and save a superuser with default settings."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Must be staff.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("must be superuser")
        
        return self.create_user(email, username, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    """Custom user model where email and username are required."""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
# orders
User = get_user_model()

class BaseModel(models.Model):
    """Manager for custom order model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 
        ordering = ['-created_at']
        # won’t be created as its own database table.



class Item(BaseModel):
    """individual items that can be ordered"""
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


class Order(BaseModel):
    """actual order placed by a customer"""
    PAYMENT_METHOD = (("CARD", "card"),("CASH", "Cash"),("MPESA", "mpesa"))

    customer = models.ForeignKey(User, on_delete=models.CASCADE) # to ensure if the user is deleted, all their associated orders will be deleted too.
    payment_method = models.CharField(
        max_length=25, choices=PAYMENT_METHOD, default=PAYMENT_METHOD[1][0]
    ) # default payment is cash


    def __str__(self):
        return f"Order by {self.customer.username}"


class OrderDetail(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(editable=False) # can't be manually changed from admin or forms

    def save(self, *args, **kwargs):
        """overrides the default save() method"""
        self.total = self.quantity * self.item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item.name