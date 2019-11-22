import pandas as pd
import math
from config import DIFFERENCE_THRESHOLD
# TODO add asserts


def check_balances(balances, expected_emission, distribution_type):
    balances_sum = balances.sum()
    difference = math.fabs(balances_sum - expected_emission)
    relative_difference = difference / balances_sum
    assert relative_difference < DIFFERENCE_THRESHOLD, "Difference for {} is {}% ({} CYB), i.e. more than {}%".format(
        distribution_type, 
        relative_difference * 100,
        int(difference),
        DIFFERENCE_THRESHOLD * 100
    )


class Processor:
    def __init__(self, *args, **kwargs):
        self.expected_emission = float(kwargs['expected_emission'])
        self.distribution_type = kwargs["distribution_type"]

    def load_df(self):
        pass

    def convert_balances(self):
        self.df["cyb_balance"] = self.df["balance"]

    def check_balances(self):
        check_balances(self.df["cyb_balance"], self.expected_emission, self.distribution_type)

    def process(self):
        self.load_df()
        self.convert_balances()
        self.check_balances()
        return self.df


class CSVProcessor(Processor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = kwargs["path"]

    def load_df(self):
        self.df = pd.read_csv(self.path)
        if "address" not in self.df.columns:
            self.df = pd.read_csv(self.path, names=["address", "balance"])


class JSONProcessor(Processor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_json = kwargs["total_json"]

    def load_df(self):
        manual_json = self.total_json[self.distribution_type]
        self.df = pd.DataFrame([{
            "address": key,
            "balance": float(value)
        } for key, value in manual_json.items()])


class AbsoluteCSVProcessor(CSVProcessor):
    pass
    

class RelativeCSVProcessor(CSVProcessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emission = float(kwargs["emission"])

    def convert_balances(self):
        sqrt_balance = self.df["balance"].pow(0.5)
        percentage = sqrt_balance / sqrt_balance.sum()
        self.df["cyb_balance"] = self.emission * percentage
