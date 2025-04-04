from libs.tts import TTS


def test_speak() -> None:
    """
    Test the speak method of the TTS class to ensure that it does not raise
    any exceptions when invoked with a valid message.
    """
    msg: str = "Hola equipo les deseo un excelente día."
    tts: TTS = TTS()
    tts.speak(msg)
