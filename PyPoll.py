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
file_to_save = os.path.join("Analysis","election_results.txt")
#initialize vote counter
total_votes = 0

#initialize winning candidate and vote tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#create candidate list and votes dictionary
candidate_options = []
candidate_votes = {}



# Open the election results and read the file

    # the old metho is: election_data = open(file_to_load, 'r')
    # The problem with this method is that files can be damaged if not closed at the end of the script. Using With prevents this

with open(file_to_load) as election_data:
    #read file with reader function
    file_reader = csv.reader(election_data)
    
    #Assign the header row
    headers = next(file_reader)
    
    #loop through rows in CSV
    for row in file_reader:
        #add to vote tally
        total_votes += 1
        #add to candidate options
        candidate_name=row[2]
        
        #add candidate if req'd
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        #add vote tally per candidate
        candidate_votes[candidate_name]+=1

#write to text file
with open(file_to_save, "w") as txt_file:
    election_results=(
        f"\nElection Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------\n"
    )
    print(election_results,end="")
    txt_file.write(election_results)

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        percentage_votes = votes/total_votes
        candidate_results = (f"{candidate_name}: {percentage_votes:.1%} ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        if (votes>winning_count) and (percentage_votes>winning_percentage):
            winning_percentage=percentage_votes
            winning_count=votes
            winning_candidate=candidate_name
    winning_candidate_sumary =(
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Vote Percentage: {winning_percentage:.1%}\n"
        f"------------------------\n"
    )
    print(winning_candidate_sumary)
    txt_file.write(winning_candidate_sumary)

    

