class Bill:

    def __init__(self, amount, period):
        """
        Object that contains data about a bill, such as total amount and period of the bill
        :param amount: total amount
        :param period: total days lived in the house
        """
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight  = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight,2)


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass



bill = Bill(120, period="May 2022")
deep = Flatmate("Deep", 20)
akshay = Flatmate("Akshay", 25)


print("Total Bill Amount: ", bill.amount)
print("Deep pays: ", deep.pays(bill, flatmate2=akshay))
print("Akshay pays: ", akshay.pays(bill, flatmate2=deep))