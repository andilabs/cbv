from django.db import models


class Code(models.Model):
    name = models.CharField(max_length=6)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    code = models.ForeignKey(Code, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)