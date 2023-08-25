import requests
from bs4 import BeautifulSoup

# Your Wakatime API key
api_key = "YOUR_WAKATIME_API_KEY"

# Fetch Wakatime data
response = requests.get(f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={api_key}")
data = response.json()

# Parse the data as needed and update the README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Update the README content with your Wakatime statistics

# Write the updated content back to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
