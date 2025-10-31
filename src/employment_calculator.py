from .base_calculator import BaseTaxCalculator
from . import constans

#defining method of calculating tax for Employement
class EmploymentCalculator(BaseTaxCalculator):
    def __init__(self, income:float):
        super().__init__(income)
        self.contract_name = "EMPLOYMENT"

    def _calculate_tax(self):
        self.deductible = constans.EMPLOYMENT_DEDUCTIBLE
        self.taxable_income = round(self.income_after_contributions - self.deductible)
        self.advance_tax_18 = self.taxable_income * constans.ADVANCE_TAX_RATE
        tax_after_free = self.advance_tax_18 - constans.TAX_FREE_AMOUNT
        self.advance_tax = tax_after_free - self.health_7_75
        self.advance_tax_rounded = round(self.advance_tax)