import re

with open('doc_test.txt', 'r') as text:
    #RE SEARCH
    for textline in text:
        checknum = re.search('([A-z]{1,}\s){2}[A-z]{1,}', textline)
        if checknum:
            print('Search with re.search FIO: ', checknum.group())
    
    #RE MATCH
        checknum = re.match('\d{4}\s\d{6}\s', textline)
        if checknum:
            print('Search with re.match Number of a passport: ', checknum.group())