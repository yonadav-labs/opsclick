from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from mezzanine.blog.models import BlogPost


class BlogSitemap(Sitemap):
 	changefreq = 'daily'
 	priority = 0.5

 	def items(self):
  		return BlogPost.objects.all()


class StaticPagesSitemap(Sitemap):
 	changefreq = 'daily'
 	priority = 0.5

 	def items(self):
  		return ['home', 'platform', 'services', 'university', 'videos', 'news', 'learn-more']

 	def location(self, item):
  		return reverse(item) 	