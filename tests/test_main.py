import unittest
from unittest.mock import patch, MagicMock

class TestTrashTalkApp(unittest.TestCase):
    @patch("tkinter.Tk", return_value=MagicMock())               # 🧠 Mock the Tk GUI root
    @patch("pyttsx3.init")                                       # 🧠 Mock TTS engine
    def test_trigger_trash_talk_runs(self, mock_tts, mock_tk):
        import AI_Trash_Talk_Ollama as main  # Update this if you rename your .py file

        # Set up the fake TTS engine
        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        # Simulate the StringVar manually
        import tkinter as tk
        main.output_text = tk.StringVar()
        main.trigger_trash_talk("AI Scores")

        # Check fallback output line was set
        self.assertIn(main.output_text.get(), main.fallback_lines["AI Scores"])

if __name__ == "__main__":
    unittest.main()
