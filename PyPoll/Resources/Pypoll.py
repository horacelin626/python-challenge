import os
import csv
csvpath = os.path.join("..", "Resources", "data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#The total number of votes cast
total_votes =0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for votes in csvreader:
       total_votes = total_votes + 1


#A complete list of candidates who received votes


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    OTooley_vote=0

    for row in csvreader:
      if (row[2]) == "Khan":
            Khan_vote = Khan_vote + 1
      if (row[2]) == "Correy":
            Correy_vote = Correy_vote + 1
      if (row[2]) == "Li":
            Li_vote = Li_vote + 1
      if (row[2]) == "O'Tooley":
          OTooley_vote = OTooley_vote + 1



#The percentage of votes each candidate won

Khan_vote_percentage = Khan_vote / total_votes * 100
Correy_vote_percentage = Correy_vote / total_votes * 100
Li_vote_percentage = Li_vote / total_votes * 100
OTooley_vote_percentage = OTooley_vote / total_votes *100

Khan_vote_percentage = round(Khan_vote_percentage)
Correy_vote_percentage = round(Correy_vote_percentage)
Li_vote_percentage = round(Li_vote_percentage)
OTooley_vote_percentage = round(OTooley_vote_percentage)

dict={'Khan':Khan_vote_percentage, 'Correy':Correy_vote_percentage,
        'Li':Li_vote_percentage, 'OTooley':OTooley_vote_percentage}

winner=sorted(dict, key=lambda x:dict[x])[-1]

output = (
    f"\nElection Results\n"

    f"----------------------------\n"

    f"Total Votes: {total_votes}\n"

    f"----------------------------\n"
    
    f"Khan: {Khan_vote_percentage:.3f}% ({Khan_vote})\n"

    f"Correy: {Correy_vote_percentage:.3f}% ({Correy_vote})\n"

    f"Li: {Li_vote_percentage:.3f}% ({Li_vote})\n"

    f"O'Tooley: {OTooley_vote_percentage:.3f}% ({OTooley_vote})\n"
    
    f"----------------------------\n"

    f"Winner: {winner}\n"

    f"----------------------------\n")

print(output)



   

