import csv

with open("PyPoll/Resources/election_data.csv") as file:
    reader = csv.reader(file)
    headers = next(reader)
    count = 0

    candidates = {}

    for voter_id, county, candidate in reader:
        count += 1
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

output = f"""Election Results
-------------------------
Total Votes: {count}
-------------------------
"""

for candidate, votes in candidates.items():
    percentage = round(votes/count * 100,2)
    output += (f"{candidate}: {percentage}% ({votes})\n")
        
output+=f"""-------------------------
Winner: {max(candidates.keys(), key=lambda candidate: candidates[candidate])}
-------------------------"""

print(output)

with open("PyPoll/analysis/PyPoll Analysis.txt", "w") as file:
    file.write(output)