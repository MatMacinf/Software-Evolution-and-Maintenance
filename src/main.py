# from . import constans
#
# class TaxCalculator(object):
#     #income = 0
#     #contract_type = ""
#     # social security contributions
#     #pension_contrib = 0             # 9.76% of the income
#     #disability_contrib = 0          # 1.5% of the income
#     #sickness_contrib = 0            # 2.45% of the income
#
#     #deductible_expenses = 111.25
#     #health_contrib_9 = 0            # 9% of the income
#     #health_contrib_7_75 = 0         # 7.75% of the income
#     #advance_tax_18 = 0              # advance tax = 18%
#     #tax_free_amount = 46.33         # tax-free income 46.33 PLN
#     #advance_tax = 0
#     #advance_tax_rounded = 0
#
#     @staticmethod
#     def main():
#
#         TaxCalculator.input_income()
#         TaxCalculator.choose_contract_type()
#
#         print(TaxCalculator.contract_type)
#
#         # income_after_contrib = TaxCalculator.calculate_contributions(TaxCalculator.income)
#         # print("Income:", TaxCalculator.income)
#         # print("Pension contribution: " + "{0:.2f}".format(TaxCalculator.pension_contrib))
#         # print("Disability contribution: " + "{0:.2f}".format(TaxCalculator.disability_contrib))
#         # print("Sickness contribution: " + "{0:.2f}".format(TaxCalculator.sickness_contrib))
#         # print("Income base for health contribution:", income_after_contrib)
#
#         # TaxCalculator.calculate_health_contrib(income_after_contrib)
#         # print("Health contribution: 9% = " \
#         #       + "{0:.2f}".format(TaxCalculator.health_contrib_9) +
#         #       " 7.75% = " + "{0:.2f}".format(TaxCalculator.health_contrib_7_75))
#
#         if TaxCalculator.contract_type == "EMPLOYMENT":
#
#             print("Tax deductible expenses:", TaxCalculator.deductible_expenses)
#             # taxable_income = income_after_contrib - TaxCalculator.deductible_expenses
#             # taxable_income_rounded = float("{0:.0f}".format(taxable_income))
#             # print("Taxable income:", taxable_income, "rounded:", "{0:.0f}".format(taxable_income_rounded))
#
#             # TaxCalculator.calculate_advance_tax_18(taxable_income_rounded)
#             # print("Advance tax 18% =", TaxCalculator.advance_tax_18)
#             # print("Tax-free amount =", TaxCalculator.tax_free_amount)
#
#             # tax_after_reduction = TaxCalculator.advance_tax_18 - TaxCalculator.tax_free_amount
#             # print("Reduced tax = " + "{0:.2f}".format(tax_after_reduction))
#
#             # TaxCalculator.calculate_final_advance_tax()
#             # TaxCalculator.advance_tax_rounded = float("{0:.0f}".format(TaxCalculator.advance_tax))
#             # print("Advance paid tax = " + "{0:.2f}".format(TaxCalculator.advance_tax) +
#             #       " rounded " + "{0:.0f}".format(TaxCalculator.advance_tax_rounded))
#             #
#             # net_income = TaxCalculator.income - (
#             #     (TaxCalculator.pension_contrib + TaxCalculator.disability_contrib + TaxCalculator.sickness_contrib) +
#             #     TaxCalculator.health_contrib_9 + TaxCalculator.advance_tax_rounded
#             # )
#             #
#             # print()
#             # print("Net income = " + "{0:.2f}".format(net_income))
#
#         # elif TaxCalculator.contract_type == "CIVIL CONTRACT":
#         #     print("Income:", TaxCalculator.income)
#         #
#         #     TaxCalculator.tax_free_amount = 0
#         #     TaxCalculator.deductible_expenses = (income_after_contrib * 20) / 100
#         #     print("Tax deductible expenses:", TaxCalculator.deductible_expenses)
#
#             # taxable_income = income_after_contrib - TaxCalculator.deductible_expenses
#             # taxable_income_rounded = float("{0:.0f}".format(taxable_income))
#             # print("Taxable income:", taxable_income, "rounded:", "{0:.0f}".format(taxable_income_rounded))
#
#             # TaxCalculator.calculate_advance_tax_18(taxable_income_rounded)
#             # print("Advance tax 18% =", TaxCalculator.advance_tax_18)
#             # print("Already paid tax = " + "{0:.2f}".format(TaxCalculator.advance_tax_18))
#
#             # TaxCalculator.calculate_final_advance_tax()
#             # TaxCalculator.advance_tax_rounded = float("{0:.0f}".format(TaxCalculator.advance_tax))
#             # print("Advance tax = " + "{0:.2f}".format(TaxCalculator.advance_tax) +
#             #       " rounded " + "{0:.0f}".format(TaxCalculator.advance_tax_rounded))
#
#             # net_income = TaxCalculator.income - (
#             #     (TaxCalculator.pension_contrib + TaxCalculator.disability_contrib + TaxCalculator.sickness_contrib) +
#             #     TaxCalculator.health_contrib_9 + TaxCalculator.advance_tax_rounded
#             # )
#             #
#             # print()
#             # print("Net income = " + "{0:.2f}".format(net_income))
#
#         else:
#             print("Unknown contract type!")
#
#     @staticmethod
#     def calculate_final_advance_tax():
#         TaxCalculator.advance_tax = (
#             TaxCalculator.advance_tax_18 -
#             TaxCalculator.health_contrib_7_75 -
#             TaxCalculator.tax_free_amount
#         )
#
#     # @staticmethod
#     # def calculate_advance_tax_18(income):
#     #     TaxCalculator.advance_tax_18 = (income * 18) / 100
#
#     # @staticmethod
#     # def calculate_contributions(income):
#     #     TaxCalculator.pension_contrib = (income * 9.76) / 100
#     #     TaxCalculator.disability_contrib = (income * 1.5) / 100
#     #     TaxCalculator.sickness_contrib = (income * 2.45) / 100
#     #     return income - (
#     #         TaxCalculator.pension_contrib +
#     #         TaxCalculator.disability_contrib +
#     #         TaxCalculator.sickness_contrib
#     #     )
#
#     # @staticmethod
#     # def calculate_health_contrib(income):
#     #     TaxCalculator.health_contrib_9 = (income * 9) / 100
#     #     TaxCalculator.health_contrib_7_75 = (income * 7.75) / 100
#
#     @staticmethod
#     def choose_contract_type():
#         while True:
#             contract_type = input("Contract Type: (E)mployment, (C)ivil: ").strip().upper()
#             if not contract_type:
#                 print("Please enter a value.")
#                 continue
#             if contract_type[0] == "E":
#                 TaxCalculator.contract_type = "EMPLOYMENT"
#                 break
#             elif contract_type[0] == "C":
#                 TaxCalculator.contract_type = "CIVIL CONTRACT"
#                 break
#             else:
#                 print("Please enter 'E' for Employment or 'C' for Civil Contract.")
#
#     @staticmethod
#     def input_income():
#         while True:
#             income = float(input("Enter income: "))
#             if not income:
#                 print("Please enter a value.")
#                 continue
#             if income <= 0:
#                 print("Income must be greater than 0.")
#                 continue
#             TaxCalculator.income = income
#             break
#
#
# if __name__ == '__main__':
#     TaxCalculator.main()
