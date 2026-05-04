from django.db import models

# Static landing page currently uses hardcoded context in views.py.
# Optional future structure:
#
# class PortfolioSection(models.Model):
#     slug = models.SlugField(unique=True)
#     title = models.CharField(max_length=120)
#     subtitle = models.CharField(max_length=255, blank=True)
#
# class PortfolioProject(models.Model):
#     section = models.ForeignKey(PortfolioSection, on_delete=models.CASCADE, related_name="projects")
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     gif_url = models.URLField(blank=True)
