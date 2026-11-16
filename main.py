#!/usr/bin/env python3
"""Trim PCM WAV audio without re-encoding."""
import argparse
import wave
from pathlib import Path

def cut_wav(source: Path, destination: Path, start: float, end: float) -> float:
    if start < 0 or end <= start:
        raise ValueError("Require 0 <= start < end.")
    with wave.open(str(source), "rb") as reader:
        params = reader.getparams()
        if params.comptype != "NONE":
            raise ValueError("Only uncompressed PCM WAV files are supported.")
        rate = reader.getframerate()
        total = reader.getnframes()
        first = int(round(start * rate))
        last = min(total, int(round(end * rate)))
        if first >= total or last <= first:
            raise ValueError("The selected range does not overlap the audio.")
        reader.setpos(first)
        frames = reader.readframes(last - first)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(destination), "wb") as writer:
        writer.setparams(params)
        writer.writeframes(frames)
    return (last - first) / rate

def main():
    parser = argparse.ArgumentParser(description="Trim an uncompressed WAV file.")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--start", type=float, required=True, help="Start time in seconds")
    parser.add_argument("--end", type=float, required=True, help="End time in seconds")
    args = parser.parse_args()
    try:
        duration = cut_wav(args.source, args.destination, args.start, args.end)
    except (OSError, wave.Error, ValueError) as exc:
        parser.error(str(exc))
    print(f"Wrote {args.destination} ({duration:.3f}s)")
if __name__ == "__main__":
    main()
