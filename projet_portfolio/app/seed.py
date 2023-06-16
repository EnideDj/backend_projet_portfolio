from .models import Home, About, Resume, Experience, Summary, Education, Services, ServicesItem, Contact, Portfolio, PortfolioItem, Skills, SkillsItem
from django.utils import timezone
import random
from faker import Faker
fake = Faker()

def seed_data():
    for i in range(1, 25):
        if i == 1:  
            home = Home.objects.create(
                name='Alex Smith',
                profession='Designer, Developer, Freelancer, Photographer',
                image='img/hero-bg-1.jpg',
            )

            About.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
                image='img/profile-img-1.jpg',
                job_title='UI/UX Designer & Web Developer.',
                about_me='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                birthday=timezone.datetime(year=1995, month=5, day=1),
                website='www.example.com',
                phone='+123 456 7890',
                city='New York, USA',
                age=30,
                degree='Master',
                email='email@example.com',
                freelance_status='Available',
                additional_info='Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.'
            )
            resume = Resume.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
                
            )
            Summary.objects.create(
                home=home,
                resume=resume,
                name='Alex Smith',
                description='Innovative and deadline-driven Graphic Designer with 3+ years of experience designing and developing user-centered digital/print marketing material from initial concept to final, polished deliverable.',
                address='Portland par 127,Orlando, FL',
                phone='(123) 456-7891',
                email='alice.barkley@example.com',
            )
            Education.objects.create(
                home=home,
                resume=resume,
                degree='Master of Fine Arts &amp; Graphic Design',
                years='2015 - 2016',
                school='Rochester Institute of Technology, Rochester, NY',
                details='Qui deserunt veniam. Et sed aliquam labore tempore sed quisquam iusto autem sit. Ea vero voluptatum qui ut dignissimos deleniti nerada porti sand markend',
            )
            Education.objects.create(
                home=home,
                resume=resume,
                degree='Bachelor of Fine Arts &amp; Graphic Design',
                years='2010 - 2014',
                school='Rochester Institute of Technology, Rochester, NY',
                details='Quia nobis sequi est occaecati aut. Repudiandae et iusto quae reiciendis et quis Eius vel ratione eius unde vitae rerum voluptates asperiores voluptatem Earum molestiae consequatur neque etlon sader mart dila',
                
            )
            Experience.objects.create(
                home=home,
                resume=resume,
                title='Senior graphic design specialist',
                years='2019 - Present',
                company='Experion, New York, NY',
                responsibilities='Lead in the design, development, and implementation of the graphic, layout, and production communication materials. Delegate tasks to the 7 members of the design team and provide counsel on all aspects of the project. Supervise the assessment of all graphic materials in order to ensure quality and accuracy of the design. Oversee the efficient use of production project budgets ranging from $2,000 - $25,000',
            )
            Experience.objects.create(
                home=home,
                resume=resume,
                title='Graphic Design Specialist',
                years='2014 - 2019',
                company='Creative Agency, New York, NY',
                responsibilities='Implemented new design trends and strategies to enhance the product design for customers. Collaborated with project managers to deliver products within deadlines and budget.'
            )


            portfolio = Portfolio.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'
            )
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='App',
                image='img/portfolio/portfolio-1.jpg',
                title='App 1',
                url='portfolio_details'
            )

            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Web',
                image='img/portfolio/portfolio-2.jpg',
                title='Web 3',
                url='portfolio_details'
            )
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='App',
                image='img/portfolio/portfolio-3.jpg',
                title='App 2',
                url='portfolio_details'
            )
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Card',
                image='img/portfolio/portfolio-4.jpg',
                title='Card 2',
                url='portfolio_details'
            )
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Web',
                image='img/portfolio/portfolio-5.jpg',
                title='Web 2',
                url='portfolio_details'
            )
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='App',
                image='img/portfolio/portfolio-6.jpg',
                title='App 3',
                url='portfolio_details'
            ) 
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Card',
                image='img/portfolio/portfolio-7.jpg',
                title='Card 1',
                url='portfolio_details'
            ) 
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Card',
                image='img/portfolio/portfolio-8.jpg',
                title='Card 3',
                url='portfolio_details'
            ) 
            PortfolioItem.objects.create(
                home=home,
                portfolio=portfolio,
                category='Web',
                image='img/portfolio/portfolio-9.jpg',
                title='Web 3',
                url='portfolio_details'
            )
            
            services= Services.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'
            )
            
            ServicesItem.objects.create(
                home=home,
                name='Lorem Ipsum',
                description='Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident',
                icon='bi bi-briefcase',
                services=services,
            )
            ServicesItem.objects.create(
                home=home,
                name='Dolor Sitema',
                description='Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata',
                icon='bi bi-card-checklist',
                services=services,
            )
            ServicesItem.objects.create(
                home=home,
                name='Sed ut perspiciatis',
                description='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
                icon='bi bi-bar-chart',
                services=services,
            )
            ServicesItem.objects.create(
                home=home,
                name='Magni Dolores',
                description='Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
                icon='bi bi-binoculars',
                services=services,
            )
            ServicesItem.objects.create(
                home=home,
                name='Nemo Enim',
                description='At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque',
                icon='bi bi-brightness-high',
                services=services,
            )
            ServicesItem.objects.create(
                home=home,
                name='Eiusmod Tempor',
                description='Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi',
                icon='bi bi-calendar4-week',
                services=services,
            )
                
                
            Contact.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
                location='A108 Adam Street, New York, NY 535022',
                email='contact@example.com',
                phone='+1 5589 55488 55s',
                map_url='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12097.433213460943!2d-74.0062269!3d40.7101282!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb89d1fe6bc499443!2sDowntown+Conference+Center!5e0!3m2!1smk!2sbg!4v1539943755621'
            )
            skills = Skills.objects.create(
                home=home,
                description='Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='HTML',
                level='100'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='CSS',
                level='90'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='JavaScript',
                level='75'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='PHP',
                level='80'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='WORDPRESS/CMS',
                level='90'
            )
            SkillsItem.objects.create(
                home=home,
                skills = skills,
                name='Photoshop',
                level='55'
            )

            print('Default home info seeded!')

        else:  # Génération de données aléatoires pour tous les autres objets Home
            home = Home.objects.create(
                name=fake.name(),
                profession=', '.join([fake.job() for _ in range(3)]),
                image=f'img/hero-bg-{i}.jpg',
            )

            About.objects.create(
                home=home,
                description=fake.text(),
                image=f'img/profile-img-{i}.jpg',
                job_title=fake.job(),
                about_me=fake.text(),
                birthday=fake.date_of_birth(minimum_age=22, maximum_age=60),
                website=fake.url(),
                phone=fake.phone_number()[:15],
                city=fake.city(),
                age=random.randint(22, 60),
                degree=fake.job(),
                email=fake.email(),
                freelance_status=fake.word(ext_word_list=["Available", "Unavailable"]),
                additional_info=fake.text()
            )
            
            resume = Resume.objects.create(
                home=home,
                description=fake.sentence(),
            )
            for _ in range(1):
                Summary.objects.create(
                    home=home,
                    resume=resume, 
                    name=fake.name(),
                    description=fake.sentence(),
                    address=fake.address(),
                    phone=fake.phone_number()[:15],
                    email=fake.email(),
                )
            
            for _ in range(2):
                Education.objects.create(
                    home=home,
                    resume=resume, 
                    degree=fake.word(),
                    years=f"{fake.year()} - {fake.year()}",
                    school=fake.company(),
                    details=fake.text()
                )
            for _ in range(2):
                Experience.objects.create(
                    home=home,
                    resume=resume,  
                    title=fake.job(),
                    years=f"{fake.year()} - {fake.year()}",
                    company=fake.company(),
                    responsibilities=fake.text()
                )
            
            portfolio = Portfolio.objects.create(
                home=home,
                description=fake.sentence()
            )
            image_counter = 0

            for j in range(1, 10):
                image_counter += 1
                categories = ["App", "Card", "Web"]
                images = [f'img/portfolio/portfolio-{image_counter}.jpg' ]

                PortfolioItem.objects.create(
                    category=random.choice(categories),
                    image=random.choice(images),
                    title=fake.sentence(nb_words=3),
                    url='portfolio_details',
                    portfolio=portfolio,
                    home=home
                )

            services = Services.objects.create(
                home=home,
                description=fake.sentence()
            )
            for _ in range(6):
                ServicesItem.objects.create(
                    home=home,
                    name=fake.word(),
                    description=fake.sentence(),
                    icon=fake.file_path(),
                    services=services
                )

            Contact.objects.create(
                home=home,
                description=fake.sentence(),
                location=fake.address(),
                email=fake.email(),
                phone=fake.phone_number()[:15],
                map_url=fake.url()
            )
            skills = Skills.objects.create(
                home=home,
                description=fake.sentence()
            )
            for _ in range(6):
                SkillsItem.objects.create(
                    home=home,
                    skills = skills,
                    name=fake.word(),
                    level=random.randint(1, 100)
                )

            print(f'Home info {i} seeded!')
