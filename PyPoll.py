# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv") 

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a variable. Add before opening file.
total_votes = 0

# Declare empty new list for candidate options. Add before opening file.
candidate_options = []

# Declare empty new dictionary. Add before opening file.
candidate_votes = { }

# Declare Winning Candidate and Winning Count Tracker variables. Add before opening file.
winning_candidate = "" #this is a string
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. This formula will automatically close the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:

        # add to the total vote count variable for each loop
        total_votes += 1

        # print the candidate name from each row. It's located in the second index on the data sheet
        candidate_name = row[2]

        # If candidate doesn't match any existing candidate name
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate_options list
            candidate_options.append(candidate_name)

            # Initiatlize key to track candidate votes
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count. Need to bring out of the if statement and aligned with for loop to ensure script increments each candidate's vote count every time their name appears in the row.
        candidate_votes[candidate_name] += 1

        

## This code was added to write below results into txt file. and then tabbed
with open(file_to_save, "w") as txt_file:

    ## After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes : {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    #Save final vote to text file
    txt_file.write(election_results)

    
    # After printing the final vote count to the terminal save the final vote count to the text file

    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate:
        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes:
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes. Change votes & total votes to floating decimal numbers since votes are in dictionary and total_votes are integers
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") ##ADJUSTED##
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        ## Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        ## Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine the winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If True, then set winning_count = votes & winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name #and set winning candidate equal to candidate's name

    # Print out the winning candidate, vote count, and percentage to terminal
    # Set blank variable to add values to
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")

    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
