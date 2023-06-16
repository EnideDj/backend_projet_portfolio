import django
django.setup()

from app.seed import seed_data

if __name__ == '__main__':
    seed_data()
