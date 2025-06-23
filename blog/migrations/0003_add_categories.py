# blog/migrations/0003_add_categories.py
from django.db import migrations

def add_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    categories = [
        'Health',
        'Technology',
        'Lifestyle',
        'Education',
        'Travel',
        'Food',
        'Sports',
        'Finance',
        'Entertainment',
        'News'
    ]
    for category in categories:
        Category.objects.create(name=category)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240518_1116'),  # Ensure this matches the previous migration if there was any
    ]

    operations = [
        migrations.RunPython(add_categories),
    ]
