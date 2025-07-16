# Speech Recognition Accuracy Comparison in Voice-Based Virtual Assistants

This project implements a **Python-based voice assistant** using both:
- **Google Web Speech API** (online)
-  **CMU Sphinx** (offline)

It compares their **accuracy, speed, and reliability** under different noise and connectivity conditions.

---

##  Features

- Accepts voice input via microphone
- Switches between online and offline speech engines
- Executes basic commands (open apps, tell time, search web)
- Gives spoken output using text-to-speech

---

## Tools & Libraries

| Tool/Library       | Purpose                                |
|--------------------|----------------------------------------|
| Python             | Main programming language              |
| SpeechRecognition  | Voice recognition interface            |
| PyAudio            | Microphone input                       |
| Google Web Speech API | Online speech-to-text              |
| CMU Sphinx (pocketsphinx) | Offline speech-to-text         |
| pyttsx3 / gTTS     | Text-to-speech (offline/online)        |
| playsound          | Play audio output                      |

---

##  How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

