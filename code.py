import pywhatkit as kit

class Pywhatkit:
    """Pywhatkit module codes."""

    def whatsapp_instant(self, 
                nine_digit_number, 
                message,
                wait_time=20):
        """Send an instant whatsapp message"""
        kit.sendwhatmsg_instantly(f"+233{nine_digit_number}",
                                message,
                                wait_time)
    
    def whatsapp_scheduled(self, 
                nine_digit_number, 
                message,
                gmt_hour=None,
                minute=None,
                wait_time=20):
        """Send a scheduled whatsapp message"""
        kit.sendwhatmsg(f"+233{nine_digit_number}",
                        message,
                        gmt_hour, minute,
                        wait_time)
    
    def youtube(self, title):
        """Launch a youtube video by providing title."""
        kit.playonyt(title)

    def google_search(self, topic):
        """Make a google search on a given topic."""
        kit.search(topic)

    def info(self, topic, lines=5):
        """Fetch information about a given topic"""
        kit.info(topic, lines)
    
    def image_to_ascii(self, 
                        img_path, 
                        output_file="pywhatkit_asciiart.txt"):
        """Convert an image to ASCII art."""
        kit.image_to_ascii_art(img_path, output_file)

    def text_to_handwriting(self, 
                            text, 
                            save_to="pywhatkit.png",
                            rgb=[0,0,138]):
        """Convert a text to handwriting."""
        kit.text_to_handwriting(text,
                                save_to,
                                rgb)

    def shutdown(self, time=100):
        """Shutdown the system."""
        kit.shutdown(time)

    def cancel_shutdown(self):
        """Cancel scheduled shutdown."""
        kit.cancelShutdown()


