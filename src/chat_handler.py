from utils.log_caller import log_caller_info


class WhatsAppHandler:
    """Class to handle WhatsApp messaging functionalities using Playwright.

    Attributes:
        page (Page): The Playwright page instance.
    """

    def __init__(self, page):
        """Initialize the WhatsAppHandler.

        Args:
            page (Page): The Playwright page instance to interact with WhatsApp Web.
        """
        self.page = page

    def send_message(self, message, contact):
        """Send a message to the currently active chat.

        Args:
            message (str): The message to be sent.

        Example:
            send_message("Hello!", "John Doe")
        """
        try:
            # Wait for the message box to become visible
            message_box = self._find_search_box(f"Type to {contact}")

            if message_box is None:
                message_box = self._find_search_box(f"Escribe a {contact}")

            if message_box is None:
                print("Message box not found in either language.")
                return

            message_box.fill(message)  # Fill the message
            message_box.press("Enter")  # Send the message

        except TimeoutError:
            print("Timeout: Element did not load in time.")
        except Exception as e:
            log_caller_info(ex=e, error=True)

    def open_chat(self, contact):
        """Open a chat with the specified contact.

        Args:
            contact (str): The name of the contact or group to open.

        Example:
            open_chat("John Doe")
        """
        try:
            # Try to find the search box in English
            search_box = self._find_search_box("Search input textbox")

            if search_box is None:
                search_box = self._find_search_box("Cuadro de texto para ingresar la búsqueda")

            if search_box is None:
                print("Search box not found in either language.")
                return
            else:
                print("Search box found.")

            # Click to focus on the search box and fill the contact name
            search_box.click()
            search_box.fill(contact)
            self.page.keyboard.press("Enter")  # Press Enter to select the contact

            # Wait for the contact chat to become visible
            self.page.wait_for_selector(f"span[title='{contact}']", timeout=5000)
            contact_chat = self.page.query_selector(f"span[title='{contact}']")

            if contact_chat is not None:
                contact_chat.click()
                print(f"Contact '{contact}' chat opened.")
            else:
                print("Contact chat not found.")

        except TimeoutError:
            print("Timeout: Element did not load in time.")
        except Exception as e:
            log_caller_info(ex=e, error=True)

    def _find_search_box(self, aria_label):
        """Helper function to find the search box by aria-label.

        Args:
            aria_label (str): The aria-label of the search box.

        Returns:
            Element: The found search box element or None if not found.

        Example:
            _find_search_box("Search input textbox")
        """
        try:
            self.page.wait_for_selector(f"div[aria-label='{aria_label}']", timeout=2000)  # 2 seconds timeout
            return self.page.query_selector(f"div[aria-label='{aria_label}']")
        except TimeoutError:
            print(f"Box not found for: {aria_label}")
            return None

    def read_messages(self):
        """Read messages from the current chat.

        Returns:
            str: Last message received in the current chat.

        Example:
            read_messages()
        """
        try:
            # Read last messages
            messages = self.page.query_selector_all("div.message-in")
            # Return the last message
            last_message = messages[-1].inner_text()

            # Due to the way WhatsApp Web displays messages, the last message comes with a line break
            # following next pattern [contact_name, hour, message, message_hour] then we take only the message
            last_message = last_message.split("\n")[-2]
            return last_message

        except Exception as e:
            log_caller_info(ex=e, error=True)