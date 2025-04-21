import unittest
from unittest.mock import patch, MagicMock

class TestTrashTalkApp(unittest.TestCase):
    @patch("tkinter.StringVar", return_value=MagicMock())                  # ✅ Mock StringVar
    @patch("tkinter.Tk", return_value=MagicMock())                         # ✅ Mock GUI root
    @patch("pyttsx3.init")                                                 # ✅ Mock TTS
    @patch("PIL.ImageTk.PhotoImage", return_value=MagicMock())            # ✅ Mock image creation
    def test_trigger_trash_talk_runs(self, mock_img, mock_tts, mock_tk, mock_strvar):
        import AI_Trash_Talk_Ollama as main

        # Mock the TTS engine
        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        main.output_text = mock_strvar.return_value
        main.trigger_trash_talk("AI Scores")

        # Check fallback was used
        self.assertIn(main.output_text.set.call_args[0][0], main.fallback_lines["AI Scores"])

if __name__ == "__main__":
    unittest.main()
