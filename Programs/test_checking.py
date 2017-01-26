from time import gmtime, strftime
from datetime import datetime, timedelta, date as dt
import dateutil.parser, dateutil.relativedelta
import xml.etree.ElementTree as ET
import random

# Global Variables
global updatedDate

# Open File to be modified
tree = ET.parse('MAV_Case3.xml')
datesArray = []



# Parser to convert date from ISOFormat to Date Object
# This allows us to manipulate the date range.
def getDateTimeFromISO8601String(i):
  d = dateutil.parser.parse(i)
  return d

def oldPostDate(xmlFile):
    transactions = tree.iter('transaction')
    for transaction in transactions:
        postDate = transaction.find('postDate').text
        #print(postDate)
        transactionDate = getDateTimeFromISO8601String(postDate)
        #print(transactionDate)
        datesArray.append(transactionDate)
        #print(datesArray)
        newArray = datesArray
        #print(newArray)
        #dateArray = list(newArray)
    #print(dateArray)
    return newArray

def oldTransDate(xmlFile):
    transactions = tree.iter('transaction')
    for transaction in transactions:
        transDate = transaction.find('transDate').text
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

def newPostDate(newArray):
    newDateArray = []
    for date in newArray:
        #print(date)
        youngest_date = max(newArray)
        #print(youngest_date)
        todayDate = datetime.now()
        dateDiff = abs((todayDate - youngest_date).days)
        #print(dateDiff)
        newDate = date + dateutil.relativedelta.relativedelta(days=dateDiff)
        #print(newDate)
        date = str(newDate.isoformat())
        newDateArray.append(date)
        #print(newDateArray)
    return newDateArray

def newTransDate(newArray):
    newDateArray = []
    for date in newArray:
        #print(date)
        youngest_date = max(newArray)
        #print(youngest_date)
        todayDate = datetime.now()
        dateDiff = abs((todayDate - youngest_date).days)
        #print(dateDiff)
        newDate = date + dateutil.relativedelta.relativedelta(days=dateDiff)
        #print(newDate)
        date = str(newDate.isoformat())
        newDateArray.append(date)
        #print(newDateArray)
    return newDateArray

def updateXML(xmlFile):
    #print(newDateArray)
    #print(tree.findall('.//transDate')[0].text) 
    # for dateObj in tree.findall('.//transDate'): # for date in XMLtransDates   
    #     print(dateObj.text)
    #     dateObj.text = newDateArray[dateObj]
    #     print(dateObj)
    #     break
    #print(xmlFile)
    originalTransDatesArr = oldTransDate(xmlFile)
    #print(originalTransDatesArr)
    adjustedTransDatesArr = newTransDate(originalTransDatesArr)
    

    #print(adjustedTransDatesArr)
    #transactions = xmlFile.iter('transDate')
    #for transaction in transactions:
    try:
        originalPostDatesArr = oldPostDate(xmlFile)
        adjustedPostDatesArr = newPostDate(originalPostDatesArr)
    except:
        print("Error")

    for num in range(0, len(originalTransDatesArr)):
        #print(transDates[0])
        #transDate = transaction.find('transDate')
        #print("Original Value " + str(transDates[num].text))
        #print("New Value " + str(adjustedDatesArr[num]))
        print(originalTransDatesArr)
        originalTransDatesArr[num] = adjustedTransDatesArr[num]

        #print("Final Value " + str(transDates[num].text))
        

    



    #Write back to a file
    print("XMl Generated")
    now = datetime.now()
    actual_time = str(now.strftime("%Y-%m-%d-%H-%M-%S"))
    xmlFile.write("Dag Account - " + str(actual_time) + ".xml", xml_declaration=True)

    return None
#tree.write("Dag Account - " + str(actual_time) + ".xml", xml_declaration=True)
#newDateArray[oldDate]
#print(newDateArray)
#Replace Old Date value with new Date Value
#tree[oldDate] = newDateArray[oldDate]

#Update XMLFile
updateXML(tree)



# for date in newDateArray: 
#     updatedDate = date # newDateArray[0]
    
#     node.text = updatedDate # newDateArray[0]

# print(updatedDate) # newDateArray.last()

# for node in tree.findall('.//transDate'):      
#     node.text = date # Please note it has to be str '2015', not int like 2015
#     #print(node.text)
#return None


#postTest(tree)
#balanceUpdater(tree)
#transactionAmountUpdater(tree)
#baseTypeRandomizer(tree)
#accountName(tree)
# postDateUpdater(tree)
#transDateUpdater(tree)
#print("XML File Created")
#print(newArray)
#updateXML(newDate(oldDate(tree)))
#newDate(oldDate(tree))
#oldDate(newDate(tree))

#finalDates = transUpdater(dateGetter(tree))
#dateGetter(dateArray)


#return

# for num in range(0, len(tree.findall('.//transDate'))):
#     print(num)
#     print(tree.findall('.//transDate')[num].text)
#     tree.findall('.//transDate')[num].text = newDateArray[num]
#     print(tree.findall('.//transDate')[num].text)


