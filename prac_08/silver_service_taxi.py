from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.00):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * super().price_per_km

    def __str__(self):
        return "{} plus flagfall of ${:.2f} and fanciness of {}".format(
            super().__str__(), self.flagfall, self.fanciness)

    def get_fare(self):
        return self.flagfall + super().get_fare()
