This tool will automatically register you for events in the Charlotte Chess Center page.

Use caution with the tool as it requires your to use your cookies from the site. This script will not work for paid events, only free events.

How to use:
1. Login to the Chess Center Website (events.charlottechesscenter.org)
2. Right-click the page and select "Inspect Element" -> Application -> Cookies
3. Copy the name of the cookie start with remember_web_RANDOMVALUE to the "name" parameter in env.example
4. Copy the value of the cookie to the "value" paramter in env.example
5. Replace the "event" parameter in env.example with the name of the event you want to register for on a recurring schedule
6. Replace the "section" parameter with the name of the section you play in. If there is no section then the script will still handle that situation
7. Change the name of .env.example to .env


If using Windows, Compile the script using 
1. Install uv: https://docs.astral.sh/uv/
2. Run 'uv venv'
3. uv install pyinstaller
4. pyinstaller --onefile --add-data=".env:." register.py
Use the compiled binary in a scheduled task in windows

If using Linux, setup a CRON job and run the file using uv, or use as a standalone
1. Install uv: https://docs.astral.sh/uv/
2. Run 'uv venv'
3. Run 'uv pip install -r requirements.txt'
4. Run 'uv run register.py'
