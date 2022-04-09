# Election Analysis

## Election Audit Overview
The goal of the election audit is to provide valuable information to clients Seth and Tom specific to the Colorado county election. Organize and display results in a user-friendly way to deliver analysis to clients. 

#### Client deliverables
- Total votes
- County-specific results
  - Votes and relative percentages
- Largest county turnout
- Candidate-specific results
  - Votes and relative percentages
  - Winning candidate

### Resources
[Decision Statements - Bootcamp](https://courses.bootcampspot.com/courses/1269/pages/3-dot-2-8-decision-statements)

[Python Conditional Statements](https://www.guru99.com/if-loop-python-conditional-structures.html)

Utilized Python 3.7.6 and Visual Studio Code 1.66.1


## Election Audit Results
- There were a total of 369,711 votes in the Colorado region specified for the election analysis. 
#### County Results
- Denver had the **largest voter turnout**, having 306,055 votes.
  - Denver election resulted in 82.8% of total votes.
- Jefferson had the second largest voter turnout, having 38,855 votes.
  - Jefferson election resulted in 10.5% of total votes.
- Arapahoe had the lowest turnout, having 24,801 votes.
  - Arapahoe election resulted in 6.7% of total votes.
#### Candidate Results
- Diana DeGette **won the election** with 272,892 votes, or 73.8% of votes.
- Charles Casper Stockham came in second with 85,213 votes, or 20.0% of votes.
- Raymon Anthony Doane came in last with 11,606 votes, or 3.1% of votes.

### Code



#### Creating county lists, county votes dictionary, and tracking winning counties.

    # 1: Create a county list and county votes dictionary.
    county = []
    county_votes = {}

    # Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # 2: Track the largest county and county voter turnout.
    winning_county = ""
    winning_county_votes = 0
    winning_county_percentage = 0

#### Read csv, convert into list, extract county name and write check to track county doesn't match existing county.

          # 3: Extract the county name from each row.
          county_name = row[1]

          # If the candidate does not match any existing candidate add it to
          # the candidate list
          if candidate_name not in candidate_options:

              # Add the candidate name to the candidate list.
              candidate_options.append(candidate_name)

              # And begin tracking that candidate's voter count.
              candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

          # 4a: Write an if statement that checks that the
          # county does not match any existing county in the county list.
          if county_name not in county:

              # 4b: Add the existing county to the list of counties.
              county.append(county_name)

              # 4c: Begin tracking the county's vote count.
              county_votes[county_name] = 0
              
#### Write loop to determine winning county, winning county votes, and winning county percentages
#### If decision statement to winning county by using decision

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes_count = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_votes_percentage = float(votes_count) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_votes_percentage:.1f}% ({county_votes[county_name]:,})\n")

        print(county_results,end="")
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes_count > winning_county_votes) and (county_votes_percentage > winning_county_percentage):
            winning_county_votes = votes_count
            winning_county_percentage = county_votes_percentage
            winning_county = county_name

## Election Audit Summary
