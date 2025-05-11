# Instagram Bot

## Repository Overview

**Repository Name:** Instagram Bot  
**Repository Owner:** [mihaiapostol14](https://github.com/mihaiapostol14)  
**Language:** Python  
**Repository URL:** [Instagram Bot](https://github.com/mihaiapostol14/Instagram_bot)  
**Created On:** May 11, 2025  
**Last Pushed At:** May 11, 2025  
**Default Branch:** main  
**Visibility:** Public  
**Forks Count:** 0  
**Open Issues Count:** 0  
**Stargazers Count:** 0  
**Watchers Count:** 0  

## Introduction

The **Instagram Bot** project is designed for automating various tasks on Instagram. This bot can log into an Instagram account, manage session cookies, and retrieve posts (photos and reels) from a specified Instagram account. Below are some of the core features of this project.

## Features

- **Automated Login:** Logs into Instagram using provided credentials and handles authentication cookies.
- **Cookie Management:** Saves and reuses cookies for session continuity.
- **Post Scraping:** Fetches photo and reel post URLs from a target account and saves them in categorized text files.
- **Error Handling:** Graceful handling of missing elements or exceptions during execution.
- **Dynamic Scrolling:** Scrolls through the Instagram feed dynamically to load and collect more posts.
- **Like POST:** Like all user posts.
- **Download User Photo:** Download all types of user photos, whether they are photo collections or simple photos.
- **Download User Reels:** Download all user reels.

## Prerequisites

1. Python 3.x installed on your machine.
2. Firefox browser installed.
3. GeckoDriver (path configured in `self.service`).
4. A valid Pexels account (if needed for specific features).
5. Website where you can [Get User Agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

## Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/Instagram_bot.git
cd Instagram_bot
```

### 2. Create and Activate a Virtual Environment

**Install Python**

If you don't have Python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of Python. Then you can check your version of Python using the command lines below:

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Setup Project Configurations

You can use `setup_private.py` or bash code to your preference for creating a `.env` file with private data (user-agent, username, password):

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

## Contributors

- [mihaiapostol14](https://github.com/mihaiapostol14) - Contributions: 7

---

This detailed markdown description provides an in-depth look at the **Instagram Bot** project, its features, setup instructions, and contributor acknowledgments. Feel free to suggest any additional details or modifications.
