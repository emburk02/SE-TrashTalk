# AI Foosball Trash Talker

A desktop application that delivers AI-generated one-liners during a foosball game. Using a local model (via Ollama), the app listens to game events like goals and blocks and trash-talks your opponent using text-to-speech.

---

## Features

- Text-to-speech commentary powered by `pyttsx3`
- Fullscreen Tkinter GUI with custom background image
- AI-generated responses using `ollama` + `mistral`
- Buttons for common game events (score, block, miss, etc.)
- Unit-tested and GitHub Actions CI-enabled

---

## GUI Preview
![image](https://github.com/user-attachments/assets/07e9680a-4135-4d3b-96be-c2cf82ede9ac)
---

## Event Types

| Event           | Behavior                                  |
|-----------------|-------------------------------------------|
| `AI Scores`     | Generates funny one-liner after scoring   |
| `AI Blocks`     | Brags about blocking the human player     |
| `Human Scores`  | Responds sarcastically                    |
| `Human Misses`  | Mocks missed shots                        |
| `Game Start`    | Intimidates human opponent                |
| `Game Over`     | Delivers victory taunt                    |

---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch the App

```bash
python AI_Trash_Talk_Ollama.py
```

Make sure Ollama is installed and the `mistral` model is available: https://ollama.com

---

## Running Tests

```bash
python -m unittest discover tests
```

Tests are fully mocked so they pass in GitHub Actions (headless environment with no GUI/audio).

---

## Project Structure

```
SE-TrashTalk/
├── AI_Trash_Talk_Ollama.py     # Main app
├── requirements.txt            # Python dependencies
├── tests/
│   └── test_main.py            # Unit test for trash talk trigger
├── assets/
│   └── bg_screenshot.png       # (Optional) background image
├── .github/workflows/
│   └── python-app.yml          # GitHub Actions CI
├── TEST_PLAN.md
└── README.md
```

---

# TEST PLAN

This section outlines the testing approach used to validate the application's reliability and integration with CI/CD.

---

## Test Types

### Unit Tests

| Function               | Purpose                                                            |
|------------------------|--------------------------------------------------------------------|
| `get_ollama_response`  | Verifies output or fallback based on subprocess result             |
| `trigger_trash_talk`   | Verifies correct fallback text is set for all defined event types  |

---

## Mocking Strategy

To make this testable in headless CI environments:

- `pyttsx3.init()` → Mocked to avoid `espeak` errors
- `tkinter.Tk()` → Mocked to skip real window creation
- `tkinter.StringVar()` → Mocked to bypass root errors
- `PIL.ImageTk.PhotoImage()` → Mocked to skip Tk image creation

---

## Continuous Integration

- CI tool: GitHub Actions
- File: `.github/workflows/python-app.yml`

The workflow:
- Installs dependencies
- Runs unit tests from the `tests/` folder
- Validates GUI/AI logic with mock patches

---

## How to Run Locally

### Install Requirements:

```bash
pip install -r requirements.txt
```

### Run Tests:

```bash
python -m unittest discover tests
```

---

## Test Coverage Summary

- [x] Subprocess fallback handling
- [x] Text-to-speech mock call
- [x] GUI response update for all 6 event types
- [x] Fully mocked for headless CI (GUI + TTS + ImageTk)


---

## Authors

- Evan Burk
- GitHub: [@emburk02](https://github.com/emburk02)
- Zachary Oyer
- GitHub: [@zmanoyer](https://github.com/zmanoyer)


---

## License

This project is for academic use. No license currently applied.
