<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=WAV%20Cutter&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="WAV Cutter banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Trim%20uncompressed%20WAV%20audio%20by%20precise%20start%20and%20end%20times%20using%20Python's%20standard%20library." alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/wav-cutter/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/wav-cutter?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/wav-cutter/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/wav-cutter?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/wav-cutter?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="WAV Cutter custom illustration"></p>

## 🧭 Overview
Trim uncompressed WAV audio by precise start and end times using Python's standard library.. A small, local-first project designed to solve one focused problem with a simple workflow.

## ✨ Features
- 🎚️ Cut WAV clips using seconds or sample-accurate frame boundaries.
- 🎧 Preserve channels, sample rate, and sample width.
- 🧪 Validate ranges and reject unsupported compressed WAV input.
- 📦 No external audio tools or network access.

## 🖥️ Demo
~~~bash
python main.py examples/tone.wav output/clip.wav --start 0.5 --end 2.5
~~~
The demo uses local sample input. No hosted service or external account is required.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/wav-cutter.git
cd wav-cutter
python main.py examples/tone.wav output/clip.wav --start 0.5 --end 2.5
~~~

## 🧰 Tech Stack
- Python 3.10+
- wave, argparse, pathlib, unittest (standard library)

## 🗂️ Folder Structure
~~~text
wav-cutter/\n├── assets/icon.svg\n├── examples/\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add batch processing for a folder of WAV files.
- [ ] Add optional fade-in and fade-out envelopes.

## 🤝 Contributing
Bug reports and focused pull requests are welcome. Add or update tests when changing behavior, and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
