# Accessing Values in Lists
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1,2,3,4,5,6,7]
# 
# print("list[0]", list1[0], list1[2])
# print("list2[1:5]", list2[1:5])

import csv
with open('some.csv', 'wt') as f:
    writer = csv.writer(f)
    listofrows = [['Spam'] * 5 + ['Baked Beans'],['Spam', 'Lovely Spam', 'Wonderful Spam']]
    writer.writerow(listofrows)
#     writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    
print('done')