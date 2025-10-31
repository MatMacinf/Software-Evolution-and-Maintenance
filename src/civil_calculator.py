from .base_calculator import BaseTaxCalculator
from . import constans

#defining method of calculating tax for civil contract
class CivilContractCalculator(BaseTaxCalculator):
    def __init__(self, income: float):
        super().__init__(income)
        self.contract_name = "CIVIL CONTRACT"

    def _calculate_tax(self):
        self.deductible = self.income_after_contributions * 0.20
        self.taxable_income = round(self.income_after_contributions - self.deductible)
        self.advance_tax_18 = self.taxable_income * constans.ADVANCE_TAX_RATE
        self.advance_tax = self.advance_tax_18 - self.health_7_75
        self.advance_tax_rounded = round(self.advance_tax)