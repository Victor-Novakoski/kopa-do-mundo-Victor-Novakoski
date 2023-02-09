from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(null=True, default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(null=True)

    def __repr__(self):
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"

    # def clean(self):
    #     cup_years = list(range(1930, datetime.now().year, 4))
    #     first_cup_t = list(range(self.first_cup, datetime.now().year, 4))
    #     print(first_cup_t)
    #     cup_years.remove(1942)
    #     cup_years.remove(1946)

    #     # If date is not in cup years
    #     if not (self.first_cup.year in cup_years):
    #         raise ValidationError(
    #             ("there was no world cup this year"),
    #         )
    #     # If negative titles
    #     if self.titles < 0:
    #         raise ValidationError(
    #             ("titles cannot be negative"),
    #         )
    #     # If more title than disputed cups
    #     if self.titles > len(cup_years):
    #         raise ValidationError(
    #             ("impossible to have more titles than disputed cups"),
    #         )

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)
