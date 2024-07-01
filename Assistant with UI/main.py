from flask import Flask, render_template, request, jsonify
import threading
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

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
        threading.Thread(target=record_and_transcribe).start()

def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        # Combine the recorded sentences and perform a Google search
        query = " ".join(sentence)
        if query:
            return google_search(query)
        else:
            return None

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    start_recording()
    return jsonify({"status": "Recording started"})

@app.route('/stop', methods=['POST'])
def stop():
    results = stop_recording()
    if results:
        return jsonify({"status": "Recording stopped", "results": results})
    else:
        return jsonify({"status": "Recording stopped", "results": []})

if __name__ == '__main__':
    app.run(debug=True)
