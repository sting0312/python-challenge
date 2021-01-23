import os
import csv
voterID = []
county = []
candidate = []
votes_total = 0
khan = 0
correy = 0
li = 0
tooley = 0

csvpath = os.path.join("Resources", "election_data.csv")

#open file to data
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    #test open
    print(csvreader)
    csv_header = next(csvreader)
    #test print header
    print(csv_header)

    for row in csvreader:
        #populate lists 
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        if row[2] == "Khan":
            khan = khan +1
        elif row[2] == "Correy":
            correy = correy +1
        elif row[2] == "Li":
            li = li +1
        elif row[2] == "O'Tooley":
            tooley = tooley + 1

        
      
    votes_total = len(voterID)
    khan_percent = ((khan/votes_total)*100)
    correy_percent = ((correy/votes_total)*100)
    li_percent = ((li/votes_total)*100)
    tooley_percent = ((tooley/votes_total)*100)
    
    candidates = {"Khan": khan, "Correy": correy, "Li": li, "O'Tooley": tooley}
    winner = max(candidates, key=candidates.get)

print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: ", votes_total)
print(f"--------------------------")
print(f"Khan: ", '{:.3f}%'.format(khan_percent), khan)
print(f"Correy:  ", '{:3f}%'.format(correy_percent), correy)
print(f"Li:  ", '{:.3f}%'.format(li_percent), li)
print(f"O'Tooley:  ",'{:.3f}%'.format(tooley_percent), tooley)
print(f"--------------------------")
print(f"Winner:  ", winner)

output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(output_path, "w") as text_file:
    print(f"Election Results", file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Total Votes: ", votes_total, file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Khan: ", '{:.3f}%'.format(khan_percent), khan, file = text_file)
    print(f"Correy:  ", '{:3f}%'.format(correy_percent), correy, file = text_file)
    print(f"Li:  ", '{:.3f}%'.format(li_percent), li, file = text_file)
    print(f"O'Tooley:  ",'{:.3f}%'.format(tooley_percent), tooley, file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Winner:  ", winner, file = text_file)