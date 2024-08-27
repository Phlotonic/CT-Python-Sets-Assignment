# Task 1: Flight Route Comparison

# Define the sets of flight destinations for our airline and the competitor's airline
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to (Intersection of sets)
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# 2. Destinations unique to our airline (Difference of sets)
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# 3. Whether there are any destinations that neither airline shares (Symmetric difference of sets)
unique_destinations = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", unique_destinations)