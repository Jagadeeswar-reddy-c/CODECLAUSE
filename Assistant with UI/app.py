import tkinter as tk
from tkinter import messagebox
import threading
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Global variable to control the recording loop
is_recording = False
sentence = []

def record_and_transcribe():
    global is_recording, sentence
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while is_recording:
        with microphone as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Recording... Please speak.")
            audio = recognizer.listen(source)
            print("Finished recording.")

        try:
            # Transcribe the recorded audio to text
            text = recognizer.recognize_google(audio)
            print("Transcribed text:", text)

            # Split the transcribed text into words
            words = text.split()
            sentence.append(" ".join(words))
            print("Words in the sentence:", words)
            print(sentence)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    # Ensure the last recorded audio is transcribed
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=1)

    try:
        text = recognizer.recognize_google(audio)
        print("Final transcribed text:", text)
        sentence.append(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the final audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service for final audio; {e}")

def start_recording():
    global is_recording
    if not is_recording:
        is_recording = True
        start_button.config(text="Stop", command=stop_recording)
        threading.Thread(target=record_and_transcribe).start()

def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        start_button.config(text="Start", command=start_recording)
        # Combine the recorded sentences and perform a Google search
        query = " ".join(sentence)
        if query:
            results = google_search(query)
            display_results(results)

def google_search(query):
    # Set up the WebDriver (this example uses Chrome)
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or specify the path explicitly

    try:
        # Navigate to Google
        driver.get("https://www.google.com")

        # Find the search box, enter the query, and submit
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(2)

        # Find all the result containers
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

        results = []
        for result in search_results:
            title_element = result.find_element(By.TAG_NAME, 'h3')
            if title_element:
                title = title_element.text
                link_element = result.find_element(By.TAG_NAME, 'a')
                if link_element:
                    link = link_element.get_attribute('href')
                    results.append({"title": title, "link": link})

        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Close the WebDriver
        driver.quit()

def display_results(results):
    if results:
        results_text = "\n\n".join([f"{i+1}. {result['title']}\n{result['link']}" for i, result in enumerate(results)])
        messagebox.showinfo("Search Results", results_text)
    else:
        messagebox.showinfo("Search Results", "No results found or failed to retrieve search results")

# Set up the GUI
root = tk.Tk()
root.title("Voice Transcriber")

start_button = tk.Button(root, text="Start", command=start_recording)
start_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
