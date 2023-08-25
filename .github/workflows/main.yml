name: Update Wakatime Stats

on:
  schedule:
    - cron: '0 * * * *' # Run every hour

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install wakatime

      - name: Run Wakatime update script
        env:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
        run: python wakatime_script.py

      - name: Commit and push if changed
        run: |
          git config user.name "${{ github.actor }}"
          git config user.email "${{ github.actor }}@users.noreply.github.com"
          git add README.md
          git commit -m "Update Wakatime stats"
          git push
