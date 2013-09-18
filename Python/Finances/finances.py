# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:16:44 2013

@author: NotMark
"""




incomeBiweekly = 1526.93
incomeMonthly = 2 * incomeBiweekly

inSavings = 13445

chasePayoff = 9950

carInsPremium = 2451

reducedCarInsPremium = carInsPremium / 1.6

carIns = carInsPremium / 12.0
reducedCarIns = reducedCarInsPremium / 12.0

hardBills = {'Student Loans': 798.30, 'Rent and Utilities': 725, \
                'Car': 233, 'Car insurance': 209.25}
                
softBills = {'Gas': 120, 'Cell phone': 42.50}

#DD: Calculated from Mint.com records
#Lunch: Assumed $7 lunch / workday * 20 workdays
#Dinner: Assumed $7 dinner * 30 dinners / mo

food = {'Dunkin donuts': 80, 'Lunch': 140, 'Dinner': 210}

hardBillsSum = sum(hardBills.values())
softBillsSum = sum(softBills.values())
foodSum      = sum(food.values())

outcomeSum = hardBillsSum + softBillsSum

print 'Remaining (sans food): $', incomeMonthly - outcomeSum
print 'Include food: $', incomeMonthly - outcomeSum - foodSum