from django.db import models
from django.utils.timezone import now

CATEGORY_CHOICES = [
    (125, "125gm"),
    (135, "135gm"),
    (150, "150gm"),
    (160, "160gm"),
    (170, "170gm"),
    (190, "190gm"),
    (200, "200gm"),
    (250, "250gm"),
]

class FibreSheetJali(models.Model):
    color = models.CharField(max_length=10, choices=[("green", "Green 🟩"), ("white", "White ⬜"), ("blue", "Blue 🟦")])
    size = models.FloatField()
    length = models.IntegerField(choices=[(50, "50ft"), (100, "100ft")])
    weight = models.FloatField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=125)  # **Make it manually editable**
    type = models.CharField(max_length=20, choices=[("chura", "Chura"), ("stitch mat", "Stitch Mat"), ("pure mat", "Pure Mat")], default="chura")
    availability = models.CharField(max_length=20, choices=[("available", "Available ✅"), ("sold out", "Sold Out ❌")])
    date_added = models.DateField(default=now)  # Automatically set when added
    date_updated = models.DateField(auto_now=True)  # Automatically set when updated

    def __str__(self):
        return f"{self.color} - {self.size}ft - {self.weight}kg"

    class Meta:
        verbose_name = "Fibre Sheet Jali"
        verbose_name_plural = "Fibre Sheet Jali"

class FibreSheetCloth(models.Model):
    design = models.CharField(max_length=10, choices=[("green", "Green 🟩"), ("white", "White ⬜"), ("blue", "Blue 🟦")])
    size = models.FloatField()
    length = models.IntegerField(choices=[(50, "50ft"), (100, "100ft")])
    weight = models.FloatField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=125)  # **Make it manually editable**
    type = models.CharField(max_length=20, choices=[("chura", "Chura"), ("stitch mat", "Stitch Mat"), ("pure mat", "Pure Mat")], default="chura")
    availability = models.CharField(max_length=20, choices=[("available", "Available ✅"), ("sold out", "Sold Out ❌")])
    date_added = models.DateField(default=now)  # Automatically set when added
    date_updated = models.DateField(auto_now=True)  # Automatically set when updated

    def __str__(self):
        return f"{self.color} - {self.size}ft - {self.weight}kg"

    class Meta:
        verbose_name = "Fibre Sheet Cloth"
        verbose_name_plural = "Fibre Sheet Cloth"
