from time import gmtime, strftime
from datetime import datetime, timedelta
import dateutil.parser, dateutil.relativedelta
import xml.etree.ElementTree as ET
import random



# Open File to be modified
tree = ET.parse('user.xml')
root = tree


#add Transactions

# Parser to convert date from ISOFormat to Date Object
# This allows us to manipulate the date range.
def getDateTimeFromISO8601String(i):
	d = dateutil.parser.parse(i)
	return d

# Checks date and updates if outside 90 day range
def dateUpdater(xmlFile):
	for dates in root.iter('transDate'):
		todayDate = datetime.now()
		beginDate = todayDate + dateutil.relativedelta.relativedelta(months=-3)
		originalDate = dates.text
		transactionDate = getDateTimeFromISO8601String(originalDate)

		if (transactionDate > beginDate and transactionDate < todayDate):
			dates.text = str(transactionDate.isoformat())
		else:
			updatedDate = todayDate + dateutil.relativedelta.relativedelta(months=-1)
			dates.text = str(updatedDate.isoformat())
	return dates


# Randomizer for account Name
def accountName(xmlFile):
  for accountNames in root.iter('accountName'):
    accountName = ["Chase Checking","Wells Fargo Checking", "Merrill Lynch"]
    new_accountName = random.choice(accountName)
    accountNames.text = str(new_accountName)
  return accountNames

# Randomly chooses credit of debit between each transaction
def baseTypeRandomizer(xmlFile):
  for i in root.iter('transaction'):
    baseType = ["credit","debit"]
    i.attrib["baseType"] = random.choice(baseType)
  return i.text

# Randomizer for balance
def balanceUpdater(xmlFile):
  for balance in root.iter('curAmt'):
    new_balance = round(random.uniform(2000.0, 100000.0), 2)
    balance.text = str(new_balance)
    #print('Balance Amount Updated')
  return balance

# Randomize amounts for each transaction
def transactionAmountUpdater(xmlFile):
  # Updates amounts on each transaction
  for amt in root.iter('amount'):
    amount = round(random.uniform(1.0, 10000.0), 2)
    amt.text = str(amount)
  return amount

#add Transactions
#def addTransactions(xmlFile):






balanceUpdater(tree)
transactionAmountUpdater(tree)
baseTypeRandomizer(tree)
accountName(tree)
dateUpdater(tree)
#addTransactions(tree)
#print(dateUpdater(tree).text)


# Write back to a file
now = datetime.now()
actual_time = str(now.strftime("%Y-%m-%d-%H-%M-%S"))
tree.write("Dag Account - " + str(actual_time) + ".xml", xml_declaration=True)
