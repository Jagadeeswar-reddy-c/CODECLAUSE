# Project - 4 - Assistant with UI

```
Project ID: #CC9866
Project Title: Assistant with UI
Internship Domain: Python Development Intern
Project Level: Golden Level
```

### Project Overview

Create an interactive voice assistant with a user-friendly graphical user interface. The application records the user's voice when they click the microphone button, processes the command, and displays the interpreted command on the screen. The assistant then responds with relevant information, solutions, or feedback based on the command.

### Key Features:
  1. User-Friendly Interface:
     - Simple and intuitive interface for easy interaction.
     - Clean and responsive design for seamless user experience.
  2. Voice Command Recognition:
     - Records and transcribes voice commands using speech recognition.
     - Handles various commands and provides appropriate responses.
  3. Google Search Integration:
     - Automatically performs Google searches based on transcribed voice commands.
     - Displays search results within the application.
  4. Responsive Design:
     - Uses Tkinter for a desktop-friendly design.
     - Ensures a consistent user experience.
  5. Real-time Feedback:
     - Provides immediate feedback by displaying the interpreted command.
     - Shows search results in a message box.

### Technologies Used
  - `Python`: Core programming language used for backend logic.
  - `Tkinter`: Library used for creating the graphical user interface.
  - `SpeechRecognition`: Library used for integrating voice recognition.
  - `Selenium`: WebDriver used for automating Google search.

### Code Explanation
  1. Voice Assistant Application (`main.py`):
       - This part of the code sets up the Tkinter application, defines the voice recording and transcription functionality, and handles Google search integration.
  2. Main Functions:
       - `record_and_transcribe()`: Continuously records audio and transcribes it using Google's speech recognition service.
       - `start_recording()`: Starts the recording process.
       - `stop_recording()`: Stops the recording process and performs a Google search with the transcribed text.
       - `google_search(query)`: Uses Selenium to perform a Google search and retrieve the results.
       - `display_results(results)`: Displays the search results in a message box.

## How to Run the Project
## Version
```
Python >= 3.7.0 or anaconda
ChromeDriver
```

## Usage
Installation and Setup:

```
git clone https://github.com/Jagadeeswar-reddy-c/CODECLAUSE.git
cd "Assistant with UI"

```
  1. Install Dependencies:
     -  Ensure you have the necessary Python libraries installed. You can install them using pip:
```
pip install tkinter
pip install SpeechRecognition
pip install selenium
pip install pyaudio
```
  2. Set up ChromeDriver:
     - Ensure that the ChromeDriver executable is in your system PATH or provide the path to the executable in the `webdriver.Chrome()` call.


## Running the Application
  1. Run the Python script:
```
python app.py
```
  2. Use the Application:
     - Click the "Start" button to begin recording your voice.
     - Speak your command clearly.
     - Click the "Stop" button to stop recording and perform a Google search with the transcribed text.
     - View the search results in the message box.

## Results
<img src="./images/Output 1.png" alt = "Output Image"/>
<center>Starting of the Application</center>
<img src="./images/Output 2.png" alt = "Output Image"/>
<center>Outcome of the Project</center>

## Conclusion

The Assistant with UI project developed during my internship at CodeClause Pvt Ltd showcases my proficiency in Python and GUI development. Utilizing Tkinter for the frontend and various Python libraries for backend logic, I created a user-friendly desktop application that records and transcribes voice commands, performs Google searches, and displays results. This project highlights my ability to integrate various technologies to solve practical problems, enhancing my technical skills and preparing me for future software development challenges.
