from django.db import models

class CaregiverType(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='caregiver_types/', null=True, blank=True)

    def __str__(self):
        return self.name

class CaregiverPackage(models.Model):
    caregiver_type = models.ForeignKey(CaregiverType, related_name="packages", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CaregiverPackageList(models.Model):
    image = models.ImageField(upload_to='package_lists/', null=True, blank=True)
    name = models.CharField(max_length=255)
    caregiver_package = models.ForeignKey(CaregiverPackage, related_name="package_lists", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
