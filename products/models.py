from django.db import models

class Menu(models.Model):
    menu_name = models.CharField(max_length=45)

class Categories(models.Model):
    category_name = models.CharField(max_length=45)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Drinks(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()

class Allergy(models.Model):
    name = models.CharField(max_length=45)

class Allergy_drinks(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    
class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fl_oz = models.CharField(max_length=45)

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    
class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)






