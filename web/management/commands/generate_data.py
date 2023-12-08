import random
from random import randint

from django.core.management import BaseCommand

from web.models import Inventory, KindOfSport, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.first()
        kinds_of_sport = KindOfSport.objects.filter(user=user)

        for i in range(50):
            sport = random.choice(kinds_of_sport)
            inventory = Inventory.objects.create(
                title=f'Inventory {i}',
                kindOfSport=sport,
                rating=randint(1, 5)
            )
            inventory.user.add(user)