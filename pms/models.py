from django.db import models

# Create your models here.

class GrexterBase(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Building(GrexterBase):
    address = models.TextField(null=True, blank=True)
    landmark_1 = models.CharField(max_length=200, null=True, blank=True)
    landmark_2 = models.CharField(max_length=200, null=True, blank=True)
    landmark_3 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ('name', 'address')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'landmark_1': self.landmark_1,
            'landmark_2': self.landmark_2,
            'landmark_3': self.landmark_3
        }

class Room(GrexterBase):
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.SET_NULL)
    flat_number = models.CharField(max_length=50, null=True, blank=True)
    sqft_area = models.PositiveIntegerField(default=0)
    rent = models.PositiveIntegerField(default=0)
    FLAT_CHOICES = (
        ('1BHK', '1 BHK'),
        ('2BHK', '2 BHK'),
        ('3BHK', '3 BHK'),
        ('Studio', 'Studio')
    )
    flat_type = models.CharField(max_length=100, null=True, blank=True, choices=FLAT_CHOICES)
    bathrooms = models.PositiveIntegerField(default=0)
    ec_acc_number = models.CharField(max_length=100, null=True, blank=True)

    def to_dict(self):
        return {
            'id':self.id,
            'building': self.building.name,
            'flat_number': self.flat_number,
            'sqft_area': self.sqft_area,
            'rent': self.rent,
            'flat_type': self.flat_type,
            'bathrooms': self.bathrooms,
            'ec_acc_number': self.ec_acc_number
        }

    class Meta:
        unique_together = ('building', 'flat_number')

