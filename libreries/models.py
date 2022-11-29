from django.db import models

# Create your models here.


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='titulo')
    image = models.ImageField(
        upload_to='images', verbose_name='imagen', null=True)
    description = models.TextField(verbose_name='descripcion', null=True)

    def __str__(self):
        row = "title:" + self.title + " - " + "description:" + self.description
        return row

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
