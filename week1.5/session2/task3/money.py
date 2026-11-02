# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if not isinstance(pounds, int):
            raise TypeError("Pounds is not an integer")
        if not isinstance(pence, int):
            raise TypeError("Pence is not an integer")
        if not -1 < pence < 100:
            raise ValueError("Pence is out of the range 0-100")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return f"£{self.pounds}.{self.pence}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other, Money):
            raise TypeError("other is not a Money object")
        moneySum = str(float(f"{self.pounds}.{self.pence}") + float(f"{other.pounds}.{other.pence}")) # creates a string of sum of Moneys
        
        pound = ""
        penny = ""
        for char in moneySum:
            if char == '.':
                pound = int(pound)
                break
            pound += char
        
        for i in range(len(moneySum)):
            try:
                penny += moneySum[i+(len(str(pound)))+1] # iterates using i, offset by the pound section and then a decimal character
            except:
                penny = int(penny)
                break

        money = Money(pound, penny)
        return money

m = Money(1, 50)
n = Money(2, 50)
print(m+n)