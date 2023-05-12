import csv

def read(path, wineName, caseSize):
    with open(path, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        tags = []
        #i = 0
        for row in csvReader:
            # print(', '.join(row))
            # customerID = row[0]
            # form dictionary from transaction
            tx = {'wine': wineName, 'custID': row[1], 'orderID': row[0], 'last': row[2], 'first': row[3], 'qty': row[7]}
            tags = appendTx(tx, caseSize, tags)
            #print(tags[i])
            #i+=1
    csvfile.close()
    return tags





# Helpers
def appendTx(dict, caseSize, tags):
    suffix = 0
    while int(dict['qty']) > caseSize:
        new_OrderID = dict['orderID'] + '_' + str(suffix)
        suffix += 1
        new_dict = {'wine': dict['wine'], 'custID': dict['custID'],  'orderID': new_OrderID, 'last': dict['last'], 'first': dict['first'],
                    'qty': str(caseSize)}
        dict['qty'] = str(int(dict['qty']) - caseSize)
        tags.append(new_dict)
    tags.append(dict)
    return tags


