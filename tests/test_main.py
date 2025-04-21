import unittest
from unittest.mock import patch, MagicMock

class TestTrashTalkApp(unittest.TestCase):
    @patch("tkinter.Tk", return_value=MagicMock())                      # ✅ Mock GUI
    @patch("pyttsx3.init")                                             # ✅ Mock TTS
    @patch("PIL.ImageTk.PhotoImage", return_value=MagicMock())         # ✅ Mock image creation
    def test_trigger_trash_talk_runs(self, mock_img, mock_tts, mock_tk):
        import AI_Trash_Talk_Ollama as main

        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        import tkinter as tk
        main.output_text = tk.StringVar(master=mock_tk.return_value)   # ✅ HERE'S THE FIX

        main.trigger_trash_talk("AI Scores")
        self.assertIn(main.output_text.get(), main.fallback_lines["AI Scores"])

if __name__ == "__main__":
    unittest.main()
