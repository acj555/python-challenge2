"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
total_sum = 0
net_change_total = 0
next_profit = 0
greatest_increase = float('-inf')  # Set to negative infinity for comparison
greatest_decrease = float('inf')     # Set to positive infinity for comparison
month_list = []
previous_profit = None

# Open and read the csv
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    for row in reader:
        month_list.append(row[0])
        current_profit = int(row[1])
        
        # Calculate total sum
        total_sum += current_profit
        
        # Calculate net change
        if previous_profit is not None:
            net_change = current_profit - previous_profit
            net_change_total += net_change
            
            # Calculate the greatest increase in profits (month and amount)
            if net_change > greatest_increase:
                greatest_increase = net_change
                greatest_increase_month = row[0]

            # Calculate the greatest decrease in losses (month and amount)
            if net_change < greatest_decrease:
                greatest_decrease = net_change
                greatest_decrease_month = row[0]

        previous_profit = current_profit  # Update previous profit
        total_months += 1  # Increment the month count

# Calculate the average net change across the months
average_change = net_change_total / (total_months - 1) if total_months > 1 else 0

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------\n"
    f"The total number of months is: {total_months}\n"
    f"The net total amount of Profit/Losses over the period: ${total_sum}\n"
    f"The average change is: ${average_change:.2f}\n"
    f"The greatest increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"The greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
