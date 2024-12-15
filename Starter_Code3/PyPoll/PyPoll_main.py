# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidates_options =[]
Candidates_dict ={}

# Winning Candidate and Winning Count Tracker
winner_total = 0
winner_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        Candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if Candidate_name not in Candidates_options:
            Candidates_options.append(Candidate_name)
            Candidates_dict[Candidate_name]=0

        # Add a vote to the candidate's count
        Candidates_dict[Candidate_name]+=1

    # Determine the winning candidate by counting votes in dictionary
    for candidate, votes in Candidates_dict.items():
        if votes > winner_total:
            winner_candidate = candidate
            winner_total = votes
        
    # Calculate the percentages for each candidate and format them as percentages
    Candidate_1_percent = Candidates_dict[Candidates_options[0]]/total_votes
    Candidate_1_percentage = Candidate_1_percent * 100
    Candidate_1_percentage_format =  f"{Candidate_1_percentage:.3f}%"   

    Candidate_2_percent = Candidates_dict[Candidates_options[1]]/total_votes
    Candidate_2_percentage = Candidate_2_percent * 100
    Candidate_2_percentage_format =  f"{Candidate_2_percentage:.3f}%"   

    Candidate_3_percent = Candidates_dict[Candidates_options[2]]/total_votes
    Candidate_3_percentage = Candidate_3_percent * 100
    Candidate_3_percentage_format =  f"{Candidate_3_percentage:.3f}%"   

#Convert integers to strings so they can be written in .txt file
total_votes_str = f'{total_votes}'
Candidate_1_str = f'{Candidates_dict[Candidates_options[0]]}'
Candidate_2_str = f'{Candidates_dict[Candidates_options[1]]}'
Candidate_3_str = f'{Candidates_dict[Candidates_options[2]]}'

# print to terminal 
print ("Election Results")
print ("----------")
print ("Total Votes:", f'{total_votes}')
print ("----------")
print (Candidates_options[0], Candidate_1_percentage_format, "Vote Total:", Candidates_dict[Candidates_options[0]])
print (Candidates_options[1], Candidate_2_percentage_format, "Vote Total:", Candidates_dict[Candidates_options[1]])
print (Candidates_options[2], Candidate_3_percentage_format, "Vote Total:", Candidates_dict[Candidates_options[2]])
print ("----------")
print (winner_candidate)
print ("----------")


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("---------------\n")
    txt_file.write("Total Votes: ")
    txt_file.write(total_votes_str)
    txt_file.write("\n---------------\n")
    txt_file.write(Candidates_options[0])
    txt_file.write(": ")
    txt_file.write(Candidate_1_percentage_format)
    txt_file.write("Votes: ")
    txt_file.write(Candidate_1_str)
    txt_file.write("\n")
    
    txt_file.write(Candidates_options[1])
    txt_file.write(": ")
    txt_file.write(Candidate_2_percentage_format)
    txt_file.write("Votes: ")
    txt_file.write(Candidate_2_str)
    txt_file.write("\n")

    txt_file.write(Candidates_options[2])
    txt_file.write(": ")
    txt_file.write(Candidate_3_percentage_format)
    txt_file.write("Votes: ")
    txt_file.write(Candidate_3_str)
    txt_file.write("\n")

    txt_file.write("\n---------------\n")
    txt_file.write("Winner: ")
    txt_file.write(winner_candidate)
    txt_file.write("\n---------------")

    