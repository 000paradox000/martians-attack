import logging

import pyttsx3


logger = logging.getLogger(__name__)


class TTS:
    def __init__(self):
        """Initialize the text-to-speech engine with default settings."""
        self._engine = pyttsx3.init()
        self._setup()

    def _setup(self) -> None:
        """Set up the default configurations for the TTS engine."""
        self.rate = 125  # Default speaking rate
        self.volume = 1.0  # Max volume

        # Set the default voice if available
        voices = self.voices
        selected_voice_id = 35
        default_voice_id = 0
        default_voice = voices[default_voice_id].id
        cond = len(voices) >= selected_voice_id + 1
        self.voice = voices[selected_voice_id].id if cond else default_voice

        self.run_and_wait()

    @property
    def rate(self) -> int:
        """Get the current speaking rate of the TTS engine."""
        return self._engine.getProperty("rate")

    @rate.setter
    def rate(self, value: int) -> None:
        """Set a new speaking rate for the TTS engine."""
        self._engine.setProperty("rate", value)

    @property
    def volume(self) -> float:
        """Get the current speaking volume of the TTS engine."""
        return self._engine.getProperty("volume")

    @volume.setter
    def volume(self, value: float) -> None:
        """Set a new speaking volume for the TTS engine."""
        self._engine.setProperty("volume", value)

    @property
    def voices(self) -> list:
        """Get the available voices of the engine."""
        return self._engine.getProperty("voices")

    @property
    def voice(self) -> str:
        """Get the current speaking voice of the TTS engine."""
        return self._engine.getProperty("voice")

    @voice.setter
    def voice(self, value: str) -> None:
        """Set a new speaking voice for the TTS engine."""
        self._engine.setProperty("voice", value)

    def speak(self, text: str | list[str]) -> None:
        """Speak the given text using the TTS engine."""
        logger.debug(f"Speaking: {text}")
        if isinstance(text, list):
            texts = text
        else:
            texts = [text]

        for text in texts:
            self._engine.say(text)

        self.run_and_wait()

    def run_and_wait(self) -> None:
        """Run the speech engine and wait for completion."""
        self._engine.runAndWait()

    def info(self) -> None:
        """Display the current settings of rate, volume, and voice."""
        logger.debug(f"Current speaking rate: {self.rate}")
        logger.debug(f"Current speaking volume: {self.volume}")
        logger.debug(f"Current speaking voice: {self.voice}")

    def start(self):
        logger.debug("Start")

    def stop(self):
        """Stop the TTS engine"""
        logger.debug("End")
        self._engine.stop()
