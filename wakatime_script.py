import requests
import re

# Your Wakatime API key
api_key = "YOUR_WAKATIME_API_KEY"

# Fetch Wakatime data
response = requests.get(f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={waka_583ca795-7039-4c47-bc89-d02b2b698c4a}")
data = response.json()

# Extract and format Wakatime data as needed

# Read the current README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Update the README content with your Wakatime statistics

# Write the updated content back to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
