import unittest
from unittest.mock import patch
import builtins
import random
import tkinter as tk

# Mock what we need from your main script
import AI_Trash_Talk_Ollama as main  # Adjust this if your filename is different

class TestTrashTalkApp(unittest.TestCase):
    def test_fallback_response(self):
        event = "AI Scores"
        line = main.get_ollama_response("bad prompt", event)
        self.assertIn(line, main.fallback_lines[event])

    @patch("pyttsx3.init")
    def test_trigger_trash_talk_runs(self, mock_tts):
        main.output_text = tk.StringVar()
        main.trigger_trash_talk("Game Over")
        self.assertTrue(len(main.output_text.get()) > 0)

if __name__ == '__main__':
    unittest.main()
