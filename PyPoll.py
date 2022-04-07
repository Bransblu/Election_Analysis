# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. THe winner of the election based on popular vote.

# Add our dependencies.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# candidate options
candidate_options = []

# 1. Declare empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # 2. Add to the total vote count.
        total_votes += 1

        # Print candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking the candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a cote to that candidates count.
        candidate_votes[candidate_name] += 1

# Create loop to get the candidates name through candidate_options.
for candidate_name in candidate_votes:

    # Use loop variable to retreive votes of the candidate from candidate_votes dictionary.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of the vote count.
    vote_percentage = float(votes) / float(total_votes) * 100

    # print out each candidates name, vote count, and percentahe of
    # votes to the terminal.

    # Determine winning vote count and candidate.

    # Determine if the vote is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):


        # if true then set winning count = votes and winning percent =
        # vote percent
        winning_count = votes
        winning_percentage = vote_percentage

        # Set winning candidate equal to candidates name.
        winning_candidate = candidate_name

    # Print out winning candidate, vote count, and percentage to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")
print(winning_candidate_summary)
    

