# WhatsApp Bot Using Playwright

## Overview

This project is a simple bot that automates messaging in WhatsApp Web using Python and Playwright. The bot allows users to send messages to specified contacts continuously until they choose to stop, facilitating easy communication without manual input.

## Features

- **Automated Messaging**: Send messages to any contact in WhatsApp.
- **Dynamic Contact Handling**: Easily switch between contacts using commands.
- **Message Receiving**: The bot can read and store the last received message from the contact.
- **User-Friendly Input**: Prompts for contact name and messages.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Playwright
- Dependencies listed in `requirements.txt`

### Installation

1. Clone this repository or download the source files.
2. Navigate to the project directory.

### Configuring the Environment

To set up the project, use the provided `setup.sh` script:

1. **Give Execute Permission**:

   ```bash
   chmod +x setup.sh
   ```

2. **Run the Setup Script**:

   ```bash
   ./setup.sh

    Menu:
    1. Initialize Environment
    2. Run Bot
    3. Exit
    
    Select an option: 1
    Python 3.13 is already installed.
    Virtual environment already initialized.
   
   ```

The `setup.sh` script will:
- Check for Python 3.13; if not found, it will install it.
- Create a virtual environment if it doesn't exist.
- Install the necessary dependencies listed in `requirements.txt`.
- Install Playwright's required dependencies.

### Running the Bot

After initializing the environment, you can run the WhatsApp bot:

- The bot can be executed through the same `setup.sh` script by select the appropriate option from the menu or through the python script:

**Example Bash**:

```bash
    ./setup.sh 
        
    Menu:
    1. Initialize Environment
    2. Run Bot
    3. Exit
    
    Select an option: 2
    Activating virtual environment and running the bot...
```

**Example Python**:

```bash
    source venv/bin/activate
    python3 src/bot.py 
```

### Example of Bot Interaction

- Once the bot is running a pop-up window will appear with the QR code of the WhatsApp Web, it will prompt you to scan the QR code and enter the contact name.
- You have to wait until the windows load all the chats and then interact with the bot through the terminal.

```bash
    python src/bot.py 
    
    Scan the QR code and press Enter...
    
    Enter the contact name: Anya Forger
    
    Search box found.
    Contact Anya Forger chat opened.
    
    Anya Forger said: Where are you?
    
    You said: Hello
    You said: I am coming to your house
    You said: change contact
    
    Enter the new contact name: Mary Sue
    
    Search box found.
    Contact Mary Sue chat opened.
    
    Mary Sue said: Did you arrive at Anya Forger house?
    
    You said: Almost, I am close
    Mary Sue said: Ok
    
    You said: close bot
    
    Exiting the bot.
    Press Enter to close the browser...
```

### Limitations

1. **Message Reading**: Currently, the bot reads only the last message received from the contact. If multiple messages are sent while you are typing, only the most recent will be displayed.
2. **Pending Improvement**: Future enhancements may include handling multiple unread messages or allowing the user to interact with those messages more effectively.
3. **Docker Functionality**: The project is not currently compatible with Docker.

### Compatibility

This project works best in Ubuntu versions that come with Python 3.13 by default. Consider using such versions to avoid any installation issues.

## Conclusion

This WhatsApp bot is a demonstration of how to automate messaging using Playwright, showcasing a practical application of web automation. Future iterations can enhance its functionality and user experience.

If you have any suggestions or need further assistance, feel free to reach out!
