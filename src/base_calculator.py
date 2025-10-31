from . import constans
#Base calculator template easier to understand and don't need to be changed with more calculators added
class BaseTaxCalculator:
    def __init__(self, income: float):
        #defining all contributions, values
        self.income = income
        self.pension = 0
        self.disability = 0
        self.sickness = 0
        self.health_7_75 = 0
        self.health_9 = 0
        self.advance_tax_18 = 0
        self.income_after_contributions = 0
        self.advance_tax = 0
        self.advance_tax_rounded = 0
        self.net_income = 0
        self.deductible = 0
        self.taxable_income = 0
        self.contract_name = "BASE"

    #calculate contributions in correct order
    def calculate(self):
        self._calculate_social_contributions()
        self.income_after_contributions = self._income_after_contributions()
        self._calculate_health()
        self._calculate_tax()
        self._calculate_net_income()
        return self.net_income

    # calculate each step of tax steps
    def _calculate_social_contributions(self):
        self.pension = self.income * constans.PENSION_CONTRIB
        self.disability = self.income * constans.DISABILITY_CONTRIB
        self.sickness = self.income * constans.SICKNESS_CONTRIB

    def _income_after_contributions(self):
        return self.income - (self.pension + self.disability + self.sickness)

    def _calculate_health(self):
        self.health_9 = self.income_after_contributions * constans.HEALTH_CONTRIB_9
        self.health_7_75 = self.income_after_contributions * constans.HEALTH_CONTRIB_7_75

    #method that is defined in classes using this class as a template
    def _calculate_tax(self):
        raise NotImplemented

    def _calculate_net_income(self):
        self.net_income = self.income -(
            self.pension +
            self.disability +
            self.sickness +
            self.health_9 +
            self.advance_tax_rounded
        )

    #prints summary in readable format
    def summary(self):
        data = {
            "Contract type": self.contract_name,
            "Income": f"{self.income:.2f} PLN",
            "Pension contribution " : f"{self.pension:.2f} PLN",
            "Disability contribution ": f"{self.disability:.2f} PLN",
            "Sickness contribution ": f"{self.sickness:.2f} PLN",
            "Income base for health contribution ": f"{self.income_after_contributions:.2f} PLN",
            "Health contribution 9% ": f"{self.health_9:.2f} PLN",
            "Health contribution 7.75% ": f"{self.health_7_75:.2f} PLN",
            "Tax deductible expenses ": f"{self.deductible:.2f} PLN",
            "Taxable income ": f"{self.taxable_income:.2f} PLN",
            "Advance tax 18%": f"{self.advance_tax_18:.2f} PLN",
            "Final advance tax": f"{self.advance_tax_rounded:.2f} PLN",
            "Net income": f"{self.net_income:.2f} PLN",
        }

        print("\n--- Detailed Summary ---")
        for key, value in data.items():
            print(f"{key:<35}: {value}")