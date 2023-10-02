from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Actions(models.Model):
    user = models.ForeignKey('auth.User', related_name='actions', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        indexes = [
            models.Index(fields=['-create']),
            models.Index(fields=['target_ct', 'target_id']),
        ]
        ordering = ['-create']