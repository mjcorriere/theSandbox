from collections import namedtuple

class Loan(object):

	def __init__(self, principal, term, APR):

		self.principal 	= float(principal)
		self.term		= float(term)
		self.APR		= float(APR)

		self.monthlyAPR	= APR / 12.0 / 100.0

		self.payment	= self.monthlyAPR * self.principal * \
							(1 + self.monthlyAPR)**self.term \
							/ ( (1 + self.monthlyAPR)**self.term - 1)

class ScheduleRow(namedtuple('ScheduleRow', 'balance pmtP pmtI')):
	__slots__ = ()

	def __str__(self):
		return 'Balance: ' 			+ str(self.balance) + \
				' PmtPrincipal: ' 	+ str(self.pmtP) + \
				' PmtInterest: ' 	+ str(self.pmtI)

smLoan = Loan(18000, 150, 6.2)
addlPayment = 100.0

def calc_schedule(loan, addlPayment=0):

	newBalance = pmtInterest = pmtPrincipal = totalInterest = 0
	schedule = [ScheduleRow(loan.principal, 0, 0)]

	while True:

		newBalance 		= schedule[-1].balance \
							- schedule[-1].pmtP \
							- addlPayment

		if newBalance < 0:
			break

		pmtInterest		= newBalance * loan.monthlyAPR
		pmtPrincipal	= loan.payment - pmtInterest

		schedule.append(ScheduleRow(newBalance, pmtPrincipal, pmtInterest))

	numPayments = len(schedule) - 1

	for row in schedule:
		totalInterest += row.pmtI

	return numPayments, schedule, totalInterest