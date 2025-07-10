# 🎉 Happy Birthday Letter 🎉

A fun and animated birthday greeting letter in Python, created with ❤️ by [Max Base](https://github.com/BaseMax) for his Australian friend **John** from Brisbane 🇦🇺.

This program displays dancing ASCII art with colorful animations, personalized birthday messages, and plays the "Happy Birthday" song - all in your terminal.

---

## ✨ Features

- 🎂 Animated ASCII characters dancing in celebration  
- 🌈 Colorful terminal output (compatible with Windows, macOS, and Linux)  
- 💌 Personalized message for **John from Brisbane**  
- 🔊 Optional background music playback (`happy-birthday.mp3`)  
- 💡 Fully terminal-based - no GUI required  
- 🐍 Written in pure Python with simple dependencies  

---

## Run

```
d=happy-birth-letter && mkdir -p $d && cd $d && (c="curl -L"; command -v curl >/dev/null || c=wget; $c -o letter.py https://github.com/BaseMax/happy-birth-letter/raw/main/letter.py && $c -o requirements.txt https://github.com/BaseMax/happy-birth-letter/raw/main/requirements.txt && $c -o happy-birthday.mp3 https://github.com/BaseMax/happy-birth-letter/raw/main/happy-birthday.mp3) && pip install -r requirements.txt && (command -v python3 >/dev/null && python3 letter.py || python letter.py)
```

---

## 📸 Preview

Here's a glimpse of what you’ll see in your terminal:

```
🎉🎉🎉 Let's Celebrate! 🎉🎉🎉

   (\(^_^)/)
     \   /
      | |
    🎵 Happy

🎊 🎊 🎊
````

---

## 🧑‍💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/BaseMax/happy-birth-letter.git
cd happy-birth-letter
````

### 2. Install required dependencies

```bash
pip install -r requirements.txt
```

> **Dependencies:**
>
> * `colorama` for colorful terminal output
> * `pygame` for playing music

You can also install manually:

```bash
pip install colorama pygame
```

### 3. Add music (optional)

Place a file named `happy-birthday.mp3` in the same directory.
Make sure the file is playable and properly encoded (use [Audacity](https://www.audacityteam.org/) or `ffmpeg` if needed).

### 4. Run the program

```bash
python letter.py
```

To enable music, uncomment this line in `letter.py`:

```python
# play_music()
```

---

## 📦 Package as .EXE (Optional)

To send this as a surprise executable gift:

```bash
pip install pyinstaller
pyinstaller --onefile letter.py
```

The generated `.exe` will be available in the `dist/` folder.

---

## 💬 Why This Project?

This was a heartfelt letter created for a dear Australian friend - **John from Brisbane** - to bring joy, laughter, and a dancing ASCII friend into his birthday celebration.

Feel free to fork it, personalize it, and make someone’s day brighter too! 🎈

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

Copyright 2025, Max Base
