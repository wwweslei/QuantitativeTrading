from django.core.management.base import BaseCommand

from finance.research import di, direct_treasure, etf, fii, index_b3, sgs, stock


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
            self.stdout.write(self.style.SUCCESS("Saving etf data"))
            etf.save()
        elif cod == "index":
            self.stdout.write(self.style.SUCCESS("Saving index data"))
            index_b3.save()
        elif cod == "treasure":
            self.stdout.write(self.style.SUCCESS("Saving treasure data"))
            direct_treasure.save()
        elif cod == "fii":
            self.stdout.write(self.style.SUCCESS("Saving fii data"))
            fii.save()
        elif cod == "stock":
            self.stdout.write(self.style.SUCCESS("Saving stock data"))
            stock.save_list()
            stock.save()
        elif cod == "sgs":
            self.stdout.write(self.style.SUCCESS("Saving sgs data"))
            sgs.save()
        elif cod == "di":
            self.stdout.write(self.style.SUCCESS("Saving di data"))
            di.save()
        elif cod == "all":
            self.stdout.write(self.style.SUCCESS("Saving all data"))
            etf.save()
            index_b3.save()
            direct_treasure.save()
            fii.save()
            sgs.save()
            stock.save()
        else:
            self.stdout.write(self.style.ERROR("Invalid cod"))
        self.stdout.write(self.style.SUCCESS("Successfully saved data"))
