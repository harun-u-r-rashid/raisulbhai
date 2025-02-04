from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class YouTubeLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title

class HealthPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    descriptionTwo = models.TextField()
    reason = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    package = models.ForeignKey(HealthPackage, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.package.name}"
