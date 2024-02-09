from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Avaliable times for a reservation
RESERVATION_TIME= (
    ("12pm", "12:00pm - 1.25pm"),
    ("2pm", "2:00pm - 3:45pm"),
    ("4pm", "4:00pm - 5:45pm"),
    ("6pm", "6:00pm - 7:45pm"),
    ("8pm", "8:00pm - 9:45pm"),
    
)


TABLE_SEATS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
)


# Create your models here.
class Reservation(models.Model):
    """ Model to create reservation """
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50)
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=10, choices=RESERVATION_TIME)
    company_size = models.IntegerField(default=1, 
            validators=[
            MinValueValidator(1)
        ])
    
    class Meta:
        """ Ordering reservations based on date and time """
        ordering = ['reservation_date', 'reservation_time']

    def __str__(self):
        return f'{self.guest_name} - {self.reservation_date} - {self.reservation_time}'


class Table(models.Model):
    table_id = models.IntegerField()