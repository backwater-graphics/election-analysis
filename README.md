# Election Analysis
## Overview: 
We are assisting a Colorado Board of Elections employee named Tom in an election audit of the tabulated results for U.S, Congressional precinct in Colorado. We have been tasked with reporting the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the elections based on the popular vote. This task is usually done in Excel but Tom’s manager wants to know if there is a way to automate the process using Python. If this audit is done successfully with Python, the code that Tom and I write will be used to audit not only other congressional districts but also senatorial districts and local elections. 
## Resources
-	Data Source: election_results.csv
-	Software: Python 3.9.7, Visual Studio Code 1.63.2
## Election-Audit Results
![election-analysis](https://github.com/backwater-graphics/election-analysis/blob/main/Resources/election-analysis.png)
### How many votes were cast in this congressional election?
-	We discovered that there were 369, 711 votes cast in this election.
### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
-	In the election data analysis, we found the breakdown of each county with their respective percentage of voters and the total number of votes as follows:
-	Jefferson produced 10.5% of voters, for a total of 38,855 voters.
-	Denver produced 82.8% of voters, for a total of 306,055 voters.
-	Arapahoe produced 6.7% of voters, for a total of 24,801 voters.
### Which county had the largest number of votes?
-	Through the analysis of the data, we discovered that the county with the largest number of votes was Denver, which produced 82.8% of voters, for a total of 306,055 voters.
### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
-	From the results returned in the analysis we can see the breakdown for each candidate with the percentage of votes that they received, along with the number of votes they received which I have listed below:
-	Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
-	Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
-	Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.
### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
-	Based off the analysis we found that the candidate that won the election was Diana DeGette, who received 73.8% of the vote for a total of 272,892 votes.

## Election-Audit Summary
We know that Data analytics is hot field these days, especially within political arena due to the fact that its one of the best ways to predict future outcomes, along with the ability to study past behaviors. It also helps the candidates understand voters better so as they can create their political strategy, along so many other things. This is why I am proposing that the election_anaylsis program called PyPoll_Challenge.py script be used by the election commission with some modifications for future elections. 

In this election we used the program that was written to just analyze the election_results.csv file by iterating and looping through each row and reading the data in the second(County) and third(Candidate) columns in order to add the number of votes, calculate the percentage and print the election results. In the future I can see this script being modified so that it can be used in multiple ways with any type of election.

One of the modifications that I can see happening is to add each candidate’s party affiliation, by creating a new column in the dataset and label each candidate with “R”, “D”, “I”, “G”, depending on the party affiliation and adding an additional code block or you can just add the party to an existing column for the candidate’s name, example Charles Casper Stockham(D), Diana DeGette(R), Raymond Anthony Doane (I). This modification can help to determine a list of candidates who received votes, which party they belong to, and the total number of votes each party received from each county. It will also help the pary lines candidates determine how each county votes.

Another modification I can see happening is to add demographic fields to the election_results.csv which would collect age, sex, and ethnicity and to add a block of code to output the demographic information. These categories are significate for candidates, as this will help them to determine which groups they need to appeal to and to understand how to appeal to them. 

These are just two of the modifications that I could see happening to make this script more versatile. Because of so much information being collected through data analysis, this script can help to sypher through the data in the most efficient way that would allow users to make modifications for any election analysis.    
