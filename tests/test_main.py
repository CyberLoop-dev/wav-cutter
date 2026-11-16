import tempfile
import unittest
import wave
from pathlib import Path
from main import cut_wav

class WavCutterTests(unittest.TestCase):
    def test_cuts_expected_frames(self):
        with tempfile.TemporaryDirectory() as folder:
            src, dst = Path(folder)/"in.wav", Path(folder)/"out.wav"
            with wave.open(str(src), "wb") as wav:
                wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(10)
                wav.writeframes(b"\x00\x00" * 50)
            duration = cut_wav(src, dst, 1.0, 3.0)
            with wave.open(str(dst), "rb") as wav:
                self.assertEqual(wav.getnframes(), 20)
                self.assertEqual(wav.getframerate(), 10)
            self.assertEqual(duration, 2.0)

    def test_rejects_invalid_range(self):
        with tempfile.TemporaryDirectory() as folder:
            src = Path(folder)/"in.wav"
            with wave.open(str(src), "wb") as wav:
                wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(10); wav.writeframes(b"\x00\x00"*10)
            with self.assertRaises(ValueError):
                cut_wav(src, Path(folder)/"out.wav", 2, 1)

if __name__ == "__main__":
    unittest.main()
