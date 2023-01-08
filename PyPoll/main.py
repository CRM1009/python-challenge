# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define variables
voters_candidates = []
votes = []

# Change directory
os.chdir(os.path.dirname(__file__))

# Path to csv file
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv file
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Read each row
    for row in csv_reader:

        voters_candidates.append(row[2])

    # Sort the list by ascending order
    sorted_list = sorted(voters_candidates)
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    # Count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes.append(count_candidate.most_common())

    # Calculate the percentage of votes per candicate in 3 digital points
    for item in votes:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        
    
# Print to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})")
print(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})")
print(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes[0][0][0]}")
print("-------------------------")


# Export results to a text file
election_file = os.path.join("Analysis", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})\n")
    outfile.write(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})\n")
    outfile.write(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes[0][0][0]}\n")
    outfile.write("-------------------------\n")