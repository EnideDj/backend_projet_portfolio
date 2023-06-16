from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Home, About, Resume, Services, ServicesItem, Contact, Portfolio, PortfolioItem, Skills, SkillsItem, Education, Experience
from .forms import HomeForm, AboutForm, ResumeForm, EducationForm, ExperienceForm, ServicesForm, ServicesItemForm, ContactForm, PortfolioForm, PortfolioItemForm, SkillsForm, SkillsItemForm


# Create your views here.
def index(request):
    home_info = Home.objects.first()
    home_form = HomeForm(instance=home_info)

    about_info = About.objects.first()
    about_form = AboutForm(instance=about_info)

    resume_info = Resume.objects.first()
    resume_form = ResumeForm(instance=resume_info)

    contact_info = Contact.objects.first()
    contact_form = ContactForm(instance=contact_info)

    services_info = Services.objects.first()
    services_form = ServicesForm(instance=services_info)
    services_item = ServicesItem.objects.filter(services=services_info)

    portfolio_info = Portfolio.objects.first()
    portfolio_form = PortfolioForm(instance=portfolio_info)
    portfolio_item = PortfolioItem.objects.filter(portfolio=portfolio_info).order_by('id')

    skills_info = Skills.objects.first()
    skills_form = SkillsForm(instance=skills_info)
    skills_item = SkillsItem.objects.filter(skills=skills_info)
    
    experience_info = Experience.objects.filter(resume=resume_info)
    education_info = Education.objects.filter(resume=resume_info)

    context = {
        'home_info': home_info,
        'home_form': home_form,
        
        'about_info': about_info,
        'about_form': about_form,
        
        'resume_info': resume_info,
        'resume_form': resume_form,
        'experience_info': experience_info,
        'education_info': education_info,
        
        'contact_info': contact_info,
        'contact_form': contact_form,
        
        'services_info': services_info,
        'services_form': services_form,
        'services_item': services_item,
        
        'portfolio_info': portfolio_info,
        'portfolio_form': portfolio_form,
        'portfolio_item': portfolio_item,
        
        'skills_info': skills_info,
        'skills_form': skills_form,
        'skills_item': skills_item,
        
        'user': request.user,
    }

    return render(request, 'app/body/main/main.html', context)

def portfolio_test(request):
    portfolio_info = Portfolio.objects.first()
    portfolio_item = PortfolioItem.objects.filter(portfolio=portfolio_info).order_by('id')

    context = {
        'portfolio_info': portfolio_info,
        'portfolio_item': portfolio_item,
    }

    return render(request, 'app/body/main/portfolio_detail.html', context)

def logout(request):
    home_info = Home.objects.first()
    about_info = About.objects.first()
    return render(request, 'registration/logged_out.html', {'home_info': home_info, 'about_info': about_info})


@login_required
def profile(request):
    home_info = Home.objects.first()
    about_info = About.objects.first()
    context = {
        'home_info': home_info,
        'about_info': about_info,
    }
    return render(request, 'backoffice/profile.html', context)


def homebis(request):
    return render(request, 'app/body/main/home.html')


def aboutbis(request):
    return render(request, 'app/body/main/about.html')


def contactbis(request):
    return render(request, 'app/body/main/contact.html')


def resumebis(request):
    return render(request, 'app/body/main/resume.html')


def portfoliobis(request):
    return render(request, 'app/body/main/portfolio.html')


def servicesbis(request):
    return render(request, 'app/body/main/services.html')


# ----------BACKEND----------
# ----------Home----------
def home(request):
    home_info = Home.objects.first()
    about_info = About.objects.first()
    if request.method == 'POST':
        form = HomeForm(request.POST, instance=home_info)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeForm(instance=home_info)
    return render(request, 'backoffice/main/home.html', {'home_form': form, 'home_info': home_info, 'about_info': about_info})


# ----------ABOUT----------
def about(request):
    home_info = Home.objects.first()
    about_info = About.objects.first()
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about_info)
        if form.is_valid():
            form.save()
            return redirect('about')  
    else:
        form = AboutForm(instance=about_info)
    return render(request, 'backoffice/main/about.html', {'about_form': form, 'about_info': about_info, 'home_info': home_info})


# ----------RESUME----------
def resume(request):
    resume_info = Resume.objects.first()
    home_info = Home.objects.first()
    about_info = About.objects.first()
    
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST, instance=resume_info)
        education_form = EducationForm(request.POST, prefix='education', instance=resume_info.education)
        experience_form = ExperienceForm(request.POST, prefix='experience', instance=resume_info)
        
        if resume_form.is_valid() and education_form.is_valid() and experience_form.is_valid():
            resume_form.save()
            education_form.save()
            experience_form.save()
            return redirect('resume')
    else:
        resume_form = ResumeForm(instance=resume_info)
        education_form = EducationForm()
        experience_form = ExperienceForm()
    
    context = {
        'resume_form': resume_form,
        'education_form': education_form,
        'experience_form': experience_form,
        'about_info': about_info,
        'home_info': home_info,
        'resume_info': resume_info,
    }
    
    return render(request, 'backoffice/main/resume.html', context)

# ----------PORTFOLIO----------
def portfolio(request):
    home_info = Home.objects.first()
    portfolio_info = Portfolio.objects.first()

    if request.method == 'POST':
        portfolio_form = PortfolioForm(request.POST, instance=portfolio_info)
        portfolio_item_form = PortfolioItemForm(request.POST, request.FILES)

        if portfolio_form.is_valid() and portfolio_item_form.is_valid():
            portfolio = portfolio_form.save()
            portfolio_item = portfolio_item_form.save(commit=False)  
            portfolio_item.home = home_info  
            portfolio_item.portfolio = portfolio  
            portfolio_item.save()  # Now save it

            return redirect('portfolio_detail')
    else:
        portfolio_form = PortfolioForm(instance=portfolio_info)
        portfolio_item_form = PortfolioItemForm()

    context = {
        'portfolio_form': portfolio_form,
        'portfolio_item_form': portfolio_item_form,
    }
    return render(request, 'backoffice/main/portfolio.html', context)

# ----------SERVICES----------
def services(request):
    services_info = Services.objects.first()
    home_info = Home.objects.first()
    about_info = About.objects.first()
    
    if request.method == 'POST':
        services_form = ServicesForm(request.POST, instance=services_info)
        services_item_form = ServicesItemForm(request.POST, request.FILES)

        if services_form.is_valid() and services_item_form.is_valid():
            services = services_form.save()
            services_item = services_item_form.save(commit=False)  
            services_item.home = home_info  
            services_item.portfolio = services  
            services_item.save()  # Now save it

    else:
        services_form = PortfolioForm(instance=services_info)
        services_item_form = PortfolioItemForm()

    context = {
        'services_form': services_form,
        'services_item': services_item_form,
        'services_item_form': services_item_form,
        'about_info': about_info,
        'home_info': home_info,
    }
    return render(request, 'backoffice/main/services.html', context)


# ----------CONTACT----------
def contact(request):
    contact_info = Contact.objects.first()
    home_info = Home.objects.first()
    about_info = About.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm(instance=contact_info)
    return render(request, 'backoffice/main/contact.html',
        {'contact_form': form, 'about_info': about_info, 'home_info': home_info})

# ----------SKILLS----------
def skills(request):
    skills_info = Skills.objects.first()
    home_info = Home.objects.first()
    about_info = About.objects.first()
    
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST, instance=skills_info)
        skills_item_form = SkillsItemForm(request.POST, request.FILES)

        if skills_form.is_valid() and skills_item_form.is_valid():
            skills = skills_form.save()
            skills_item = skills_item_form.save(commit=False)  
            skills_item.home = home_info  
            skills_item.portfolio = skills  
            skills_item.save()  # Now save it

    else:
        skills_form = PortfolioForm(instance=skills_info)
        skills_item_form = PortfolioItemForm()

    context = {
        'skills_form': skills_form,
        'skills_item': skills_item_form,
        'skills_item_form': skills_item_form,
        'about_info': about_info,
        'home_info': home_info,
    }
    return render(request, 'backoffice/main/skills.html', context)

