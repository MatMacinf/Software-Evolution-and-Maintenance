from .hashmap import get_calculator

#more readable name of variables for clarity, added validation check for income, validation of contract type done in hashmap, extract all redundant operations and calculations
#and put them in one template for reusability, split to more files and classes to handle responsibilites more safety and improve readability opf the code, using hashmap and template
#make it easier to add new types just by using exisitng solutions.
def main():
    while True:
        try:
            income = float(input("Enter income: "))
            if income <= 0: # Ensuring valid input value
                print("Income must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")  # Catching wrong type

    while True:
        contract_type = input("Contract Type: (E)mployment, (C)ivil: ").strip().upper()
        try:
            calculator = get_calculator(contract_type, income) #calling hashmap to check calculator and define correct tax calculation method
            break
        except ValueError as e:
            print(e)


    calculator.calculate()  #calling calculator class with choosed tax method defined
    calculator.summary()    #calling method summary to print

if __name__ == '__main__':
    main()