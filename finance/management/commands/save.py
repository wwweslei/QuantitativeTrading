from django.core.management.base import BaseCommand

from finance.research import etf, fii, stock, index_b3, direct_treasure


class Command(BaseCommand):
    help = "persist etf data in database"

    def add_arguments(self, parser):
        parser.add_argument(
            "cod",
            type=str,
            help="""download etf data [etf, index, treasure, fii, all]""",
        )

    def handle(self, *args, **kwargs):
        cod = kwargs["cod"]
        if cod == "etf":
            etf.save()
        elif cod == "index":
            index_b3.save()
        elif cod == "treasure":
            direct_treasure.save()
        elif cod == "fii":
            fii.save()
        elif cod == "stock":
            stock.save()
            stock.save_all_tickers()
        elif cod == "all":
            etf.save()
            index_b3.save()
            direct_treasure.save()
            fii.save()
        else:
            self.stdout.write(self.style.ERROR("Invalid cod"))
        self.stdout.write(self.style.SUCCESS("Successfully saved data"))
