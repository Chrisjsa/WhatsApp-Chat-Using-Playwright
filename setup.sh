#!/bin/bash

# Function to check if python3.13 is installed
check_python() {
    if ! command -v python3.13 &> /dev/null; then
        echo "Python 3.13 is not installed. Installing..."
        sudo apt-get update
        sudo apt-get install -y python3.13 python3.13-venv
        echo "Python 3.13 installed successfully."
    else
        echo "Python 3.13 is already installed."
    fi
}

# Function to create a virtual environment and install dependencies
create_venv() {
    venv_dir="venv"
    if [ ! -d "$venv_dir" ]; then
        echo "Creating virtual environment..."
        python3.13 -m venv $venv_dir

        # Activate the virtual environment
        source $venv_dir/bin/activate

        # Install Python dependencies
        echo "Installing Python dependencies..."
        pip install --no-cache-dir -r requirements.txt

        # Install Playwright browsers
        echo "Installing Playwright browsers..."
        playwright install
    else
        echo "Virtual environment already initialized."
    fi
}

# Function to run the bot
run_bot() {
    echo "Activating virtual environment and running the bot..."
    source venv/bin/activate
    python3 src/bot.py
}

# Function to display the menu
main_menu() {
    while true; do
        echo ""
        echo "Menu:"
        echo ""
        echo "1. Initialize Environment"
        echo "2. Run Bot"
        echo "3. Exit"

        read -p "Select an option: " choice

        case $choice in
            1)
                check_python
                create_venv
                ;;
            2)
                run_bot
                ;;
            3)
                echo "Exiting..."
                break
                ;;
            *)
                echo "Invalid choice. Please try again."
                ;;
        esac
    done
}

# Start the menu
main_menu