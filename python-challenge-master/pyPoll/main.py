#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

csvpath=os.path.join("Resources","election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    votes=[]
    county=[]
    candidates=[]
    khan=[]
    correy=[]
    li=[]
    otool=[]

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    
        TotalVote= (len(votes))
        #print(TotalVote)
    
    for candidate in candidates:
        if candidate=="Khan":
            khan.append(candidates)
            khanVotes=len(khan)
        elif candidate=="Correy":
            correy.append(candidates)
            correyVotes=len(correy)
        elif candidate=="Li":
            li.append(candidates)
            liVotes=len(li)
        else:
            otool.append(candidates)
            otoolVotes=len(otool)
    #print(khanVotes)
    #print(correyVotes)
    #print(liVotes)
    #print(otoolVotes)

    
    kahnPer= round(((khanVotes/TotalVote)*100),5)
    corPer= round(((correyVotes/TotalVote)*100),5)
    liPer= round(((liVotes/TotalVote)*100),5)
    otoolPer= round(((otoolVotes/TotalVote)*100),5)
    #print(kahnPer)
    #print(corPer)
    #print(liPer)
    #print(otoolPer)

    if kahnPer > max(corPer, liPer, otoolPer):
        winner= "Khan"
    elif corPer >max(kahnPer,liPer, otoolPer):
        winner="Correy"
    elif liPer > max(kahnPer, corPer, otoolPer):
        winner="Li"
    else:
        winner= "O'Tooley"
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVote}")
print("-------------------------")
print(f"Khan: {kahnPer}% ({khanVotes})")
print(f"Correy: {corPer}% ({correyVotes})")
print(f"Li: {liPer}% ({liVotes})")
print(f"O'Tooley: {otoolPer}% ({otoolVotes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

f=open("Analysis/Analysis.text","w")
f.write("Election Results")
f.write("-------------------------")
f.write(f"Total Votes: {TotalVote}")
f.write("-------------------------")
f.write(f"Khan: {kahnPer}% ({khanVotes})")
f.write(f"Correy: {corPer}% ({correyVotes})")
f.write(f"Li: {liPer}% ({liVotes})")
f.write(f"O'Tooley: {otoolPer}% ({otoolVotes})")
f.write("-------------------------")
f.write(f"Winner: {winner}")
f.write("-------------------------")
