import tkinter as tk
from tkinter import ttk
import webbrowser
import speech_recognition as sr


class WebBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Web Browser")
        self.root.geometry("800x600")
        self.root.configure(background="#baffea")  # Set background color

        self.create_widgets()

    def create_widgets(self):
        # Create browser frame
        self.browser_frame = ttk.Frame(self.root)
        self.browser_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Welcome message
        self.welcome_label = ttk.Label(self.browser_frame, text="Welcome to Web Browser!", font=("Arial", 14))
        self.welcome_label.pack(side=tk.TOP, padx=5, pady=5)

        # Create address bar
        self.address_frame = ttk.Frame(self.browser_frame)
        self.address_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.url_entry = ttk.Entry(self.address_frame, width=70)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.url_entry.bind("<Return>", self.navigate)
        self.go_button = ttk.Button(self.address_frame, text="Go", command=self.navigate)
        self.go_button.pack(side=tk.RIGHT)

        # Create voice search button
        self.voice_button = ttk.Button(self.browser_frame, text="Voice Search", command=self.voice_search)
        self.voice_button.pack(pady=5)

        # Browser display area
        self.browser = ttk.Label(self.browser_frame, text="", font=("Arial", 12))
        self.browser.pack(fill=tk.BOTH, expand=True)

    def navigate(self, event=None):
        user_input = self.url_entry.get()
        if user_input.startswith(("http://", "https://")):
            try:
                webbrowser.open_new(user_input)
            except Exception as e:
                print(e)
        else:
            search_url = "https://www.google.com/search?q=" + user_input.replace(" ", "+")
            try:
                webbrowser.open_new(search_url)
            except Exception as e:
                print(e)

    def voice_search(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for voice command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print("Voice command:", query)
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, query)
            self.navigate()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


def main():
    root = tk.Tk()
    web_browser = WebBrowser(root)
    root.mainloop()


if __name__ == "__main__":
    main()
