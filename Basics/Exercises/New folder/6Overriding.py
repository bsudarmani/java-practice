class Bank:
    def get_interest_rate(self):
        return 0.0

    def get_bank_name(self):
        return "Unknown Bank"

class SBI(Bank):
    def get_interest_rate(self):
        return 5.4

    def get_bank_name(self):
        return "State Bank of India (SBI)"

class ICICI(Bank):
    def get_interest_rate(self):
        return 6.8

    def get_bank_name(self):
        return "ICICI Bank"

bank = SBI()
print(f"{bank.get_bank_name()} - Interest Rate: {bank.get_interest_rate()}%")

bank = ICICI()
print(f"{bank.get_bank_name()} - Interest Rate: {bank.get_interest_rate()}%")
