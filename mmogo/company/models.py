from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from mmogo.core.category.models import Category, Tag
from mmogo.core.constants import DEFAULT_STATUS

class Company(models.Model):
	title = models.CharField(
		max_length=200,
		help_text=""
	)
	slug = models.SlugField()
	subtitle = models.CharField(
		max_length=200, 
		blank=True, 
		null=True, 
		help_text=""
	)
	description = models.TextField(
		blank=True, 
		null=True
	)
	category = models.ManyToManyField(
		Category, 
		blank=True, 
		null=True, 
		help_text=""
	)
	tags = models.ManyToManyField(
		Tag, 
		blank=True, 
		null=True, 
		help_text=""
	)
	image = models.ImageField(uploads='company/')
	sites = models.ManyToManyField(
		Sites,
		blank=True,
		null=True,
		help_text=""
	)
	owner = models.ForeignKeyField(
		settings.AUTH_USER_MODEL, 
		related_name='%(app_label)s_%(class)s_user',
		editable=False
	)
	created_at = models.DateTimeField(
		auto_now_add=True,
		editable=False
	)
	updated_at = models.DateTimeField(
		auto_now=True,
		editable=False
	)
	status = models.IntergerField(default=constants.DEFAULT_STATUS)
	can_comment = models.BooleanField(default=False)


	def save(self, *args, **kwargs):
		if self.site is None:
			self.sites = Site.objects.get_current()
		self.slug = slugify(self.title)
		super(Company, self).save(*args, **kwargs)

	class Meta:
		abstract = True

	def __str__(self):
		if self.subtitle:
			return %s + ' - ' + %s % (self.title, self.subtitle)
		else:
			return %s % (self.title)
