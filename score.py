import pandas as pd
import numpy as np

# Load the two CSV files
just_dance_df = pd.read_csv('just_dance.csv')
real_dance_df = pd.read_csv('real_dance.csv')

# Select the 5th column (index 4 as pandas indexing starts at 0) from each
just_dance_values = just_dance_df.iloc[3000:20000, 4].values  # From row 3001 to 20000 (Python uses 0-based indexing)
real_dance_values = real_dance_df.iloc[3000:20000, 4].values  # Same for the real dance data

# Ensure the two arrays have the same size for the calculation
if just_dance_values.shape != real_dance_values.shape:
    raise ValueError("The datasets do not have the same number of rows for comparison.")

# Calculate Euclidean distance (squared differences)
euclidean_distances = np.sqrt((just_dance_values - real_dance_values) ** 2)

# Sum of Euclidean distances (you could use different metrics based on the definition of score)
total_distance = np.sum(euclidean_distances)

# Normalize the score (assuming max possible distance for normalization, this depends on your scoring strategy)
# You can adjust the scaling factor based on what constitutes a perfect or worst performance
max_distance = 1000000  # This is an arbitrary maximum score; adjust it based on the domain knowledge
score = max(0, 100 - (total_distance / max_distance) * 100)

print(f"Score: {score:.2f}/100")
