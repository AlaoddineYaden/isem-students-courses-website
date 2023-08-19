from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=255)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    google_drive_link = models.URLField()

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    google_drive_link = models.URLField()

    def __str__(self):
        return self.name
