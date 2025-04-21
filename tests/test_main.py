import unittest
from unittest.mock import patch
import tkinter as tk

# Make sure the filename of your script is ai_trash_talk.py (no spaces!)
import AI_Trash_Talk_Ollama as main

class TestTrashTalkApp(unittest.TestCase):
    @patch("pyttsx3.init")
    def test_trigger_trash_talk_runs(self, mock_tts):
        # Simulate the TTS engine so CI doesn't try to speak
        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        # Simulate the output string
        main.output_text = tk.StringVar()
        main.trigger_trash_talk("AI Scores")

        # Make sure the fallback line or output was set
        self.assertIn(main.output_text.get(), main.fallback_lines["AI Scores"])

if __name__ == "__main__":
    unittest.main()
