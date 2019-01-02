from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


NO_CHILDREN_CHOICE = [(i, i) for i in range(11)]
EDUCATION_CHOICE = (('Less than High School', 'Less than High School'),
                    ('High School', 'High School'),
                    ('Bachelors', 'Bachelors'),
                    ('Masters', 'Masters'),
                    ('PhD', 'PhD'))
OCCUPATION_CHOICE = (('Manager', 'Manager'),
                     ('Doctor', 'Doctor'),
                     ('Student', 'Student'),
                     ('Blue Collar', 'Blue Collar'),
                     ('Lawyer', 'Lawyer'),
                     ('Clerical', 'Clerical'),
                     ('Professional', 'Professional'),
                     ('Home', 'Home'))
CARTYPE_CHOICE = (('Van', 'Van'),
                  ('Panel Truck', 'Panel Truck'),
                  ('Minivan', 'Minivan'),
                  ('Sports', 'Sports'),
                  ('SUV', 'SUV'),
                  ('Pickup', 'Pickup'))


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    company = models.ForeignKey('CompanyProfile', on_delete=models.CASCADE)
    name = models.CharField('Customer Name', max_length=100)
    dob = models.DateField()
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    no_children = models.IntegerField(choices=NO_CHILDREN_CHOICE)
    no_children_drive = models.IntegerField(choices=NO_CHILDREN_CHOICE)
    income = models.FloatField(default=0)
    parents_alive = models.BooleanField(default=False)
    home_estimate = models.FloatField(default=0)
    marriage_status = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    education = models.CharField(choices=EDUCATION_CHOICE, max_length=100)
    occupation = models.CharField(choices=OCCUPATION_CHOICE, max_length=100)
    avg_travel_time = models.IntegerField(default=0)
    car_use = models.BooleanField(default=False)
    car_type = models.CharField(choices=CARTYPE_CHOICE, max_length=100)
    car_color_red = models.BooleanField(default=False)
    car_age = models.IntegerField(default=0)
    urbanicity = models.BooleanField(default=False)
    insured_value = models.FloatField(default=0)
    prev_insurance_amt = models.FloatField(default=0)
    prev_insurance_no = models.IntegerField(default=0)
    prev_claim_revoked = models.BooleanField(default=False)
    risk = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
