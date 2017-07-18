import xml.etree.ElementTree as ET
from time import strftime
import datetime as dt
import dateutil.parser, dateutil.relativedelta
import random
from googlefinance import getQuotes
import json

#Variables
datesArray = []
balanceArray = []
# Open File to be modified
tree = ET.parse('master_invest_1.xml')
root = tree

# Parser to convert date from ISOFormat to Date Object
# This allows us to manipulate the date range.
def getDateTimeFromISO8601String(i):
	d = dateutil.parser.parse(i)
	return d
'''
 Compare current day with youngest(most recent) transaction date.
 Calculate the difference between the two days and update all other transactions
 exactly that many days.
'''
def oldDate(xmlFile):
	transactions = tree.iter('transaction')
	for transaction in transactions:
		transDate = transaction.find('date').text
		#print(transDate)
		transactionDate = getDateTimeFromISO8601String(transDate)
		#print(transactionDate)
		datesArray.append(transactionDate)
		#print(datesArray)
		newArray = datesArray
	#print(newArray)
	#dateArray = list(newArray)
	#print(dateArray)
	return newArray

def newDate(newArray):
	newDateArray = []
	for date in newArray:
		#print(date)
		youngest_date = max(newArray)
		#print(youngest_date)
		todayDate = dt.datetime.now()
		dateDiff = abs((todayDate - youngest_date).days)
		#print(dateDiff)
		newDate = date + dateutil.relativedelta.relativedelta(days=dateDiff)
		#print(newDate)
		date = str(newDate.isoformat())
		newDateArray.append(date)
	#print(newDateArray)
	return newDateArray

def updateXML(xmlFile):

	originalDatesArr = oldDate(xmlFile)
	#print(originalDatesArr)
	adjustedDatesArr = newDate(originalDatesArr)
	#print(adjustedDatesArr)
	#transactions = xmlFile.iter('transDate')
	#for transaction in transactions:
	transDates = xmlFile.findall('.//date')
	for num in range(0, len(transDates)):
		#print(transDates[0])
		#transDate = transaction.find('transDate')
		#print("Original Value " + str(transDates[num].text))
		#print("New Value " + str(adjustedDatesArr[num]))
		transDates[num].text = adjustedDatesArr[num]
	#print("Final Value " + str(transDates[num].text))


	#Write back to a file

	print("Generating Investment XML...")

# now = datetime.now()
#     actual_time = str(now.strftime("%Y-%m-%d"))
#     xmlFile.write(str(actual_time) + "_checking_1.xml", xml_declaration=True)


	#print("Generating Investment XML...")


	return transDates

def getStockPrice(xmlFile):
	holdings = tree.iter('holding')
	for holding in holdings:
		# price = holding.find('price').text
		price = float(holding.find('price').text)
		# print(price)
		symbol = holding.find('symbol').text
		tickerData = json.dumps(getQuotes(symbol), indent=2)
		resp_dict = json.loads(tickerData)
		lastPrice = resp_dict[0]['LastTradePrice']
		# print(lastPrice)
	return lastPrice

def updateStockPrice(lastPrice):
	holdings = tree.iter('holding')
	for holding in holdings:
		new_price = getStockPrice(lastPrice)
		print(new_price)
		for price in tree.iter('price'):
			#print(price)
			price = str(new_price)
			# print(price)
	return None


def balanceSumModule(xmlFile):
	transactions = tree.iter('holding')
	for value in transactions:
		getStockPrice(xmlFile)
		quantityPrice = lastPrice
		print(quantityPrice)
		print(quantity, symbol, quantityPrice)
		individual_balance = quantity * float(quantityPrice)
		print(individual_balance)
		balanceArray.append(individual_balance)
		total_balance = balanceArray
		final_balance = str(sum(total_balance))
		print("Total Balance:" + str(final_balance))


	#Update balance
	for node in tree.iter('balance'):
		balType = node.attrib.get('balType')
		if balType == 'totalBalance':
			current_amount = node.find('curAmt')
			current_amount.text = str(final_balance)
		return value.text, current_amount, individual_balance

# # Console TESTING Module #
# def testModule(dayDiff, youngest, today):
#     print ("\nToday's Date: " + str(today) + "\n")
#     print ("Most Recent Transaction Date: " + str(youngest) + "\n")
#     print ("Day Difference: " + str(dayDiff) + "\n")
#     return (dayDiff, youngest, today)

getStockPrice(tree)
updateStockPrice(tree)
updateXML(tree)
# balanceSumModule(tree)

# Write back to a file
now = dt.datetime.now()
actual_time = str(now.strftime("%Y-%m-%d-%M"))
tree.write(str(actual_time) + "_investment_1.xml", xml_declaration=True)