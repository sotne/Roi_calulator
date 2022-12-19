class Calculate:


    def __init__(self):
        self.income = ()
        self.expense = ()


    def income(self):
        self.rental_income = rental_income
        rental_income = float(input('how much do you make in montly rental income?'))
        other_income = input('do you have any other forms of income?  laundry, storage, misc')
        if other_income == 'laundry':
            laundry = float(input('how much is it?'))
        if other_income =='storage':
            storage = float(input('how much is it?'))
        if other_income =='misc':
            misc = float(input('how much is it?'))
        else:
           print('you have no extra sources of income')

    total_monthly_income = sum([rental_income][laundry][storage][misc])
    

    def expenses(self):
        self.taxes = taxes
        taxes = float(input('how much do you pay in monthly taxes?'))
        self.insurance = insurance
        insurance = float(input('how much do you pay a month in insurance?'))
        self.mortgage = mortgage
        mortgage =float(input('how much do you pay a month for mortgage?'))
        
        
        utilities = input('what utilities will you be paying for? water/sewer, garbage, electric, gas')
        if utilities == 'water':
            water = float(input('how much is it?'))

        if utilities == 'sewer':
            sewer = float(input('how much is it?'))

        if utilities == 'garbage':
            garbage = float(input('how much is it?'))

        if utilities == 'electric':
            electric = float(input('how much is it?'))
        if utilities == 'gas':
            gas = float(input('how much is it?'))
       
       
        extra_expenses = input('do you set money aside for vacancy, repairs, capex, or prop. managers?')
        if extra_expenses == 'vacancy':
            vacancy = float(input('how much is it?'))
        if extra_expenses == 'repairs':
            repairs = float(input('how much is it?'))
        if extra_expenses == 'capex':
            capex = float(input('how much is it?'))
        if extra_expenses == 'property_managment':
            property_managment = float(input('how much is it?'))
    
    total_monthly_expenses = sum([taxes][insurance][mortgage][water][sewer][garbage][electric][gas][vacancy][repairs][capex][property_managment])
    
    
    def cash_flow(self):
        total_monthly = self.income - self.expenses
        total_annual = total_monthly * 12    
    
    def cncreturn(self):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab = rehab
        self.misc = misc

        total_investment = sum([down_payment][closing_costs][rehab][misc])

        return_percent = ([total_annual] / [total_investment]) * 100