import unittest
from unittest.mock import patch
import tkinter as tk

class TestTrashTalkApp(unittest.TestCase):
    @patch("pyttsx3.init")
    def test_trigger_trash_talk_runs(self, mock_tts):
        # Delay import until after mock is set
        import AI_Trash_Talk_Ollama as main  # Use your actual file name here

        # Mock the engine
        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        # Simulate the output text variable
        main.output_text = tk.StringVar()
        main.trigger_trash_talk("AI Scores")

        # Check fallback line was used
        self.assertIn(main.output_text.get(), main.fallback_lines["AI Scores"])

if __name__ == "__main__":
    unittest.main()
