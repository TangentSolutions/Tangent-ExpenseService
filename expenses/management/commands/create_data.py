from django.core.management.base import BaseCommand, CommandError
from expenses.tests.data import create_claims_with_photos

class Command(BaseCommand):
    help = 'Process all triggers that need processing'

    def handle(self, *args, **options):
        create_claims_with_photos(num_photos=5)