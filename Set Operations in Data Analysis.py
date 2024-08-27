# Task 1: Duplicate Entries Cleanup

# List of customer IDs with some duplicates
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
unique_customer_ids = set(customer_ids)

# Convert the set back to a list and sort it to ensure the outcome is ordered
sorted_unique_customer_ids = sorted(list(unique_customer_ids))

# Display the unique and ordered customer IDs
print(sorted_unique_customer_ids)

# Expected Outcome: ['C001', 'C002', 'C003', 'C004']
