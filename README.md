# election-analysis
Module 3 of Bootcamp coursework

## Overview

The purpose of this analysis is to identify the winning candidate of a congressional election, in addition to what the total and relative number of votes were for each of the candidates, and counties for the voters.

## Results
- 369,711 votes were cast in this election
- Breakdown by county:
  - Jefferson: 38,855 votes (10.5% of the total vote)
  - Denver: 306,055 votes (82.8% of the total vote)
  - Araphoe: 24,801 votes (6.7% of the total vote)
- Denver county had the highest turnout of voters with 82.8% of the share of voters
- Breakdown by candidate:
  - Charles Casper Stockham: 85,213 (23.0% of the total vote)
  - Diana DeGette: 272,892 (73.8% of the total vote)
  - Raymon Anthony Doane: 11,606 (3.01% of the total vote)
- Election Results
  - Diana DeGette won the election with 272,892 votes, and 73.8% of the popular vote
  
## Summary
This script takes election results from a comma seperated values file as input, and outputs the overall election results (i.e. identifying the candidate with the highest number of votes). Additionally, the script provides analysis of voter turnout and vote share with respect to the county the vote was cast from, and the candidate. Results are output to a terminal application, or to a text file, election_results.txt in this case.

#### Sample Text Output
![](Resources\TextOutput.png)


#### Sample Terminal Output
![](Resources\TerminalOutput.png)


This script could be used for any election which sorts data by BallotID, County and Candidate with identical analysis provided. It could be modified to provide analysis based on different available dimensions as required; for example providing election insights based on demographics such as age and income, should that information be available.

Facts about new dimensions could be calculated with additional control structures as were created to calculate variables based on county and candidate, shown below:

![](Resources\ControlStructureExample.png)

Additionally, the output would need to be modified to loop through the new dimensions as was done with the counties and candidates, shown below:
![](Resources\OutputModificationExample.png)

In these examples, county or candidate could be replaced with variables or logic that checks against the other dimensions of interest.