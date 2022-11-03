class Money:
    def __init__(self, cili, pennies, currency):
        self.currency = currency
        self.cili = cili
        self.pennies = pennies
        self.curs = {"UAH": {"UAH": 1, "DOL": 42, "UER": 41}, "DOL": {"UAH": 0.025, "DOL": 1, "UER": 0.025},
                     "EUR": {"UAH": 0.24, "DOL": 0.98, "UER": 1}}

    def __repr__(self):
        return f'{self.cili}. {self.pennies}  {self.currency}'

    def sell(self, product):
        money_sum = self.cili * 100 + self.pennies
        product_sum = (product.cili * self.curs.get(self.currency).get(product.currency)) * 100 + (product.pennies * self.curs.get(self.currency).get(product.currency))

        if money_sum > product_sum:
            money_sum = money_sum - product_sum
            self.cili = int(money_sum/100)
            self.pennies = int(str(int(money_sum))[-2::])     
            viz_pennies = str(int(money_sum))[-2::]                         
        else:
            return "You don't have enough money to make a purchase"
        return f'З вас списано: {product}\nЗалишок: {self.cili}.{viz_pennies} {self.currency}'


    def change_UAH(self, new_u):
        self.UAH = new_u
        return "Saved"

    def change_pennies(self, new_p):
        self.pennies = new_p
        return "Saved"


class Product(Money):
    pass