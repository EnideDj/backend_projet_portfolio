from django import forms
from .models import About, Home, Resume, Education, Experience, Portfolio, PortfolioItem, Services, ServicesItem, Contact, Skills, SkillsItem

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__' 

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__' 

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        
class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = '__all__'
        
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class ServicesItemForm(forms.ModelForm):
    class Meta:
        model = ServicesItem
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class SkillsItemForm(forms.ModelForm):
    class Meta:
        model = SkillsItem
        fields = '__all__'
        