# Generated by Django 4.2.2 on 2023-06-16 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profession', models.TextField()),
                ('image_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skills')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=100)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.services')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('summary_name', models.CharField(max_length=255)),
                ('summary_description', models.TextField()),
                ('summary_address', models.CharField(max_length=255)),
                ('summary_phone', models.CharField(max_length=15)),
                ('summary_email', models.EmailField(max_length=254)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portfolio')),
                ('title', models.CharField(max_length=100)),
                ('project_url', models.URLField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=200)),
                ('responsibilities', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('map_url', models.URLField(max_length=500)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField()),
                ('image_path', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('about_me', models.TextField()),
                ('birthday', models.DateField()),
                ('website', models.URLField()),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('freelance_status', models.CharField(max_length=200)),
                ('additional_info', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.home')),
            ],
        ),
    ]
