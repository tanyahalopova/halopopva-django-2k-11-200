from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kind_of_sport',
            new_name='KindOfSport',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='kind_of_sport',
            new_name='kindOfSport',
        ),
    ]
