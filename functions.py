
import csv

def csvwrite(listOfDic):

    keys = listOfDic[0].keys()
    #print keys
    with open('cars list.xls', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(listOfDic)
