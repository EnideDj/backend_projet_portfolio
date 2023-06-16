from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=200)
    profession = models.TextField()
    image = models.CharField(max_length=200)

class About(models.Model):
    home = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='about')
    description = models.TextField()
    image = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    about_me = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=200)
    additional_info = models.TextField()

class Resume(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='resume')
    description = models.TextField()
    
class Summary(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='summary')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='summary')
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
class Education(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='education')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    details = models.TextField()
    
class Experience(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='experience')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    responsibilities = models.TextField()

class Portfolio(models.Model):
    home = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='portfolio')
    description = models.TextField()

class PortfolioItem(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='portfolioItem')
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio')
    title = models.CharField(max_length=100)
    url = models.URLField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolioItem')

class Services(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='services')
    description = models.TextField()
    
class ServicesItem(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='servicesItem')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='servicesItem')
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    
class Contact(models.Model):
    home = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='home')

    description = models.TextField()
    location = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    map_url = models.URLField(max_length=500)


class Skills(models.Model):
    home = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='skills')
    description = models.TextField()
    
class SkillsItem(models.Model):
    home = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='skillsItem')
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='skillsItem') 
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
