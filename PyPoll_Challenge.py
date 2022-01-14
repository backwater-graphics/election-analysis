#Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path. 
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis")

# Initialize a total vote counter.
total_votes = 0

# Create a canidate list and canidate votes dictionary.
candidate_options = []
county_options = []

#1: Create a county list and county votes dictionary.
candidate_votes = {}
county_votes = {}

# Winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the Header
    headers = next(file_reader)
    
    # Read each row in the CSV file.
    for row in file_reader:
       
        # Add to the total vote count.
        total_votes += 1
        
        #3: Get the candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
           
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           
            # Begin tracking the candidate's voter count.
            candidate_votes[candidate_name] = 0
       
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:
            
            #4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            
            #4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        
        #5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        
    # Save the results to our text file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results) 

    #6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        
        # 6b: Retrieve the county vote count.
        votes = county_votes[county]
       
        #6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # 6d: Print the county results to the terminal.
        county_election_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_election_results)
        
        #6e: Save the county votes to a text file.
        txt_file.write(county_election_results)
  
        #6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            winning_county = county
    txt_file.write("\n")

    #7: Print the county with the largest turnout to the terminal.
    county_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(county_results, end="")
    txt_file.write(county_results)

    # Determine the percentage of votes for each candidate by looping through the counts. Iterate through the candidate list.
    for candidate in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
       
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)    