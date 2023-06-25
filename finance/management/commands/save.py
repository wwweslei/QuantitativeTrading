from django.core.management.base import BaseCommand

from finance.research import direct_treasure, etf, fii, index_b3, stock


class Command(BaseCommand):
    help = "persist etf data in database"

    def add_arguments(self, parser):
        parser.add_argument(
            "type",
            type=str,
            help="""download etf data [etf, index, treasure, fii, all]""",
        )

    def handle(self, *args, **kwargs):
        type = kwargs["type"]
        if type == "etf":
            etf.save()
        elif type == "index":
            index_b3.save()
        elif type == "treasure":
            direct_treasure.save()
        elif type == "fii":
            fii.save()
        elif type == "stock":
            stock.save()
        elif type == "all":
            etf.save()
            index_b3.save()
            direct_treasure.save()
            fii.save()
        else:
            self.stdout.write(self.style.ERROR("Invalid type"))
        self.stdout.write(self.style.SUCCESS("Successfully saved data"))
