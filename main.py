import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3

from neuralintents import GenericAssistant


class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()