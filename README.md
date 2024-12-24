# Instagram Bot

This project is an **Instagram Automation Bot** designed for tasks such as logging into an account, saving session cookies, and retrieving posts (photos and reels) from a specified Instagram account. Built using Python and Selenium, it is highly customizable and efficient.

---

## Features

- **Automated Login**: Logs into Instagram using provided credentials and handles authentication cookies.
- **Cookie Management**: Saves and reuses cookies for session continuity.
- **Post Scraping**: Fetches photo and reel post URLs from a target account and saves them in categorized text files.
- **Error Handling**: Graceful handling of missing elements or exceptions during execution.
- **Dynamic Scrolling**: Scrolls through the Instagram feed dynamically to load and collect more posts.
- **Custom Browser Settings**: Uses a custom user agent and browser preferences to avoid detection.
- **Like POST**: Like all user posts
- **Download user photo** download all types of user photo she can be photo collections or simple photo
- **Download user Reels** download all user reels
---

## Prerequisites  
1. Python 3.x installed on your machine.  
2. Firefox browser installed.  
3. GeckoDriver (path configured in `self.service`).  
4. A valid Pexels account (if needed for specific features).
5. Website where can you [Get User Agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)



---

## Setup and Execution  

### 1. Create and Activate a Virtual Environment

**Install Python**

If you don't have python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of python.
Then you can check if your version of python using the command lines bellow


```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```


### 2. Install the required libraries:  

```bash
pip install -r requirements.txt
```

### 3. Setup project configurations

You can use ```setup_private.py``` or bash code to your preference for create ```.env``` file with private data (user-agent, username, password)

```bash
#!/bin/bash

# Define the path to the config directory and the .env file
CONFIG_DIR="config"
ENV_FILE="$CONFIG_DIR/.env"

# Create the config directory if it doesn't exist
if [ ! -d "$CONFIG_DIR" ]; then
    echo "Creating directory: $CONFIG_DIR"
    mkdir "$CONFIG_DIR"
else
    echo "Directory $CONFIG_DIR already exists."
fi

# Change to the config directory
cd "$CONFIG_DIR" || exit

# Check if the .env file already exists
if [ -f "$ENV_FILE" ]; then
    echo "$ENV_FILE already exists. Overwriting..."
else
    echo "$ENV_FILE does not exist. Creating a new one..."
fi

# Write the data into the .env file
echo "USER_AGENT='user agent'" > "$ENV_FILE"
echo "ACCOUNT_USERNAME='account username'" > "$ENV_FILE"
echo "ACCOUNT_PASSWORD='account password'" > "$ENV_FILE"

echo ".env file created successfully with data:"
cat "$ENV_FILE"

 ```