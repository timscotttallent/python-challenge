import csv

with open("PyBank/Resources/budget_data.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    first = next(reader)

    count = 1
    net_profit = int(first[1])
    max_profit = int(first[1])
    max_profit_date = first[0]

    min_profit = int(first[1])
    min_profit_date = first[0]
    for row in reader:
        count += 1
        profit_loss = int(row[1])
        net_profit += profit_loss
        if profit_loss > max_profit:
            max_profit = profit_loss
            max_profit_date = row[0]

        elif profit_loss < min_profit:
            min_profit = profit_loss
            min_profit_date = row[0] 
           
average_profit = net_profit/count

output = f"""Financial Analysis
----------------------------
Total Months: {count}
Total: ${net_profit}
Average  Change: ${round(average_profit, 2)}
Greatest Increase in Profits: {max_profit_date} (${max_profit})
Greatest Decrease in Profits: {min_profit_date} (${min_profit})"""

print(output)

with open("PyBank/analysis/PyBank Analysis.txt", "w") as file:
    file.write(output)