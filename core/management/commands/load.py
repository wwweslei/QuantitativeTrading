from django.core.management.base import BaseCommand
from core.finance.download_market_data import run_all


class Command(BaseCommand):
    help = "Insert all data from yahoo finance"

    def handle(self, *args, **kwargs):
        run_all()
        self.stdout.write("Update")
