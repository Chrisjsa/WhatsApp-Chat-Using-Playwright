from playwright.sync_api import sync_playwright
from chat_handler import WhatsAppHandler
from utils.log_caller import log_caller_info


def main():
    """Main function to execute the WhatsApp bot.

    This function launches the browser, navigates to WhatsApp Web, and allows
    the user to send messages continuously until they type 'Cerrar Bot'.

    The user must scan the QR code and can enter the name of the contact to chat with.

    Example:
        main()
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            # Navigate to WhatsApp Web
            page.goto("https://web.whatsapp.com")
            input("Scan the QR code and press Enter...")

            # Create an instance of WhatsAppHandler
            whatsapp = WhatsAppHandler(page)

            # Request the contact name from the user
            contact = input("Enter the contact name: ")
            whatsapp.open_chat(contact)  # Open the contact's chat

            # Store the buffer for messages
            message_buffer = []

            while True:
                # Read and save the last message from the contact
                last_message = whatsapp.read_messages()
                if last_message and (not message_buffer or last_message != message_buffer[-1]):
                    print(f"{contact} said:", last_message)
                    message_buffer.append(last_message)

                message = input("You said: ")

                if message.lower() == 'close bot':
                    print("Exiting the bot.")
                    break
                elif message.lower() == 'change contact':
                    contact = input("Enter the new contact name: ")
                    whatsapp.open_chat(contact)  # Open the new contact's chat

                    # Update the message buffer
                    message_buffer.clear()
                    last_message = whatsapp.read_messages()
                    if last_message and (not message_buffer or last_message != message_buffer[-1]):
                        print(f"{contact} said:", last_message)
                        message_buffer.append(last_message)

                else:
                    # Send the message
                    whatsapp.send_message(message, contact)

            input("Press Enter to close the browser...")
            page.close()
            browser.close()

    except Exception as e:
        log_caller_info(ex=e, error=True)


if __name__ == "__main__":
    main()