from .employment_calculator import EmploymentCalculator
from .civil_calculator import CivilContractCalculator

#Hashmapping contract types for easier way to add more calculators, only need new class using template and add here
CONTRACT_CALCULATORS = {
    "E": EmploymentCalculator,
    "C": CivilContractCalculator
}

def get_calculator(contract_type: str, income: float):
    contract_type = contract_type.strip().upper()
    if contract_type not in CONTRACT_CALCULATORS:
        raise ValueError("Invalid contract type.")
    return CONTRACT_CALCULATORS[contract_type](income)