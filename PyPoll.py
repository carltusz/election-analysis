# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file

    # the old metho is: election_data = open(file_to_load, 'r')
    # The problem with this method is that files can be damaged if not closed at the end of the script. Using With prevents this

with open(file_to_load) as election_data:
# To Do: Perform analysis
    #print(election_data)
    #To Do: read and analyze the data here
    
    #read file with reader function
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    print(headers)
    
    #for row in file_reader:
     #       print(row)

# Close file
election_data.close()



