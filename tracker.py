import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
from colorama import init, Fore

# Initialize colorama for colored text output
init()

# URL of the webpage you want to monitor
url = "https://apps.richmondgov.com/applications/activecalls/"

# Initialize the Chrome WebDriver
service = Service(r'your_driver_here')
driver = webdriver.Chrome(service=service)

# Store the last sent message
last_message = None

# Create or open the log.txt file for appending logs
log_file = open("log.txt", "a")

while True:
    # Refresh the webpage
    driver.get(url)
    time.sleep(5)  # Wait for 5 seconds

    # Get the content of the webpage
    page_source = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the specific table row (tr) you want to extract
    target_row = soup.find('tr', class_='odd')

    if target_row:
        # Extract the text from the desired td elements within the row
        cells = target_row.find_all('td')
        data_to_send = [cell.get_text(strip=True) for cell in cells]

        # Create a formatted message
        message = "\n".join(data_to_send)

        # Send the message if it's different from the last sent message
        if message != last_message:
            # Send the message to a Discord webhook
            webhook_url = "your_webhook_here"
            webhook = DiscordWebhook(url=webhook_url, content=message)
            webhook.execute()

            # Update the last sent message
            last_message = message

            # Print a green + symbol and white text indicating successful sending
            print(Fore.WHITE + "[" + Fore.GREEN + "+"  + Fore.WHITE + "] Message sent to webhook successfully!")

            # Log the message and API prompt to the log.txt file
            log_entry = f"Message: {message}\nAPI Prompt: {webhook_url}\n\n"
            log_file.write(log_entry)
            log_file.flush()

# Close the WebDriver and log file when done (you can use KeyboardInterrupt to stop the script)
driver.quit()
log_file.close()
