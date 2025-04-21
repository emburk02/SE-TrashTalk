import unittest
from unittest.mock import patch, MagicMock

class TestTrashTalkAllEvents(unittest.TestCase):
    @patch("tkinter.StringVar", return_value=MagicMock())
    @patch("tkinter.Tk", return_value=MagicMock())
    @patch("pyttsx3.init")
    @patch("PIL.ImageTk.PhotoImage", return_value=MagicMock())
    def test_all_trash_talk_events(self, mock_img, mock_tts, mock_tk, mock_strvar):
        import AI_Trash_Talk_Ollama as main

        mock_engine = mock_tts.return_value
        mock_engine.say.return_value = None
        mock_engine.runAndWait.return_value = None

        main.output_text = mock_strvar.return_value

        for event in main.event_prompts.keys():
            with self.subTest(event=event):
                main.trigger_trash_talk(event)
                output_line = main.output_text.set.call_args[0][0]
                self.assertIn(output_line, main.fallback_lines[event])

if __name__ == "__main__":
    unittest.main()
