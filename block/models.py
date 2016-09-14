from django.db import models


class Block(models.Model):
	name = models.CharField(u"站点名称", max_length=100)
	name = models.CharField(u"站点链接", max_length=100)
