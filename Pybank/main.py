import os 
import csv 

totalrow = 0
months = []
revenue = []
totalrev = 0 
average = [] 
combined_data = []

csvpath = os.path.join('Resources', 'budget_data_2.csv')

# Open csv file
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #print (csvreader)
    #Excluding Headers
    firstRow = True
    next(csvreader, None)
    # Loop through each line
    for line in csvfile.readlines():
        array = line.split(',')

        # Assign column[0] to Months and column[1] to Reveue
        revenue = int(array[1])
        months = array[0]
        
        combined_data.append(months)
        #print(combined_data)
        # Count the number of Months
        totalrow = totalrow + 1
        # Sum up the Revenues
        totalrev += revenue 
        # Revenue Change
        if firstRow:
            old_array = array
            firstRow = False
        else:
            percent_change = (int(array[1]) - int(old_array[1])) #/ int(old_array[1])
            old_array = array
            average.append(percent_change)


        
 # Find max and min Value in Revenue change        
max_value = max(average)
min_value = min(average)
#print(max_value)
#print(min_value)
indexmax = average.index(max_value)
#print(indexmax)
index_months =  indexmax + 1
#print(index_months)
monthmax = (combined_data[index_months])
#print(combined_data[index_months])
#print(monthmax)
indexmin = average.index(min_value)
indexmin_months = indexmin + 1
monthmin = (combined_data[indexmin_months])
#print(combined_data[indexmin_months])
#print(monthmin)

# Get the layout   
mx = [monthmax, max_value]
mn = [monthmin, min_value]
revenue_change = sum(average) / (totalrow - 1)

#---------------------------------------------------------------
# RESULTS 

print("Finantial Analysis")
print("--------------------------")
print ("Total Months: %d" % totalrow) 
print ("Toral Revenue:  %d" %totalrev)
print ("Agerage Revenue Change: {0:.0f}".format(revenue_change))
print("Greatest Increade in Revenue: ", mx[0], "$",mx[1])
print("Greatest Decrease in Revenue: ",  mn[0], "$", mn[1])
#------------------------------------------------------------------------

