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

### 2. Run the assistant
```bash
python src/main.py

```markdown
---

##  Summary of Results

| Engine           | Accuracy (Quiet) | Accuracy (Noise) | Offline Support| Response Time |
|------------------|------------------|------------------|----------------|----------------|
| Google Web API   | 95%              | 85%              |  No            | Fast           |
| CMU Sphinx       | 70%              | 50%              |  Yes           | Moderate       |

---

##  Future Scope

- Add support for natural language conversations using ChatGPT or other NLP models.
- Integrate Whisper (OpenAI) for better offline accuracy than CMU Sphinx.
- Expand command set for smart home automation, file handling, or system monitoring.
- Deploy the assistant on mobile or IoT platforms for real-world use.
- Implement user voice profile recognition for personalization and access control.

---

##  Limitations

- CMU Sphinx has limited accuracy and struggles in noisy environments.
- Google Web Speech API requires a stable internet connection.
- Only basic commands are supported in this version (e.g., open apps, search web).
- No GUI or conversational memory implemented yet.

---
