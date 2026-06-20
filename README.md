# 🎨 NarraSpeech AI

### Image-to-Story-to-Speech Generator (Generative AI – Multimodal AI)

NarraSpeech AI is a Multimodal Generative AI application that transforms images into engaging stories and narrated audio. The system combines Computer Vision, Large Language Models, and Text-to-Speech technologies to generate creative storytelling experiences from uploaded images.

---

## 🚀 Features

- 🖼️ Image Understanding using BLIP Image Captioning
- 🤖 AI Story Generation using Llama 3 (Ollama)
- 🔊 Text-to-Speech Narration
- 🌐 Interactive Streamlit Interface
- 📖 Automatic Story Creation from Images
- 🎙️ Audio Playback of Generated Stories
- 💻 Fully Local Execution using Ollama

---

## 🏗️ Architecture

```text
Image Upload
      │
      ▼
BLIP Image Captioning
      │
      ▼
Image Description
      │
      ▼
Llama 3 (Ollama)
      │
      ▼
Story Generation
      │
      ▼
Text-to-Speech Engine
      │
      ▼
Audio Narration
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Generative AI
- Ollama
- Llama 3

### Computer Vision
- BLIP Image Captioning
- Transformers

### Speech Processing
- pyttsx3
- Text-to-Speech

### Backend
- Python

---

## 📂 Project Structure

```text
NarraSpeech-AI/
│
├── .streamlit/
├── img/
├── img-audio/
├── utils/
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

### Python

Recommended Version:

```text
Python 3.10+
```

Check version:

```bash
python --version
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Varunkurhade1674/NarraSpeech-AI.git

cd NarraSpeech-AI
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download from: https://ollama.com/download

Verify Installation:

```bash
ollama --version
```

---

## 📥 Download Llama 3

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

Expected Output:

```text
llama3
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## 🎯 How to Use

### Step 1

Upload an image.

### Step 2

BLIP generates an image description.

### Step 3

Llama 3 creates a story based on the description.

### Step 4

Text-to-Speech converts the story into audio.

### Step 5

Listen to the generated narration.

---

## 📸 Example Workflow

### Input

```text
Upload an image of a dog playing in a park.
```

### Generated Caption

```text
A dog running through a grassy park.
```

### Generated Story

```text
Once upon a time, a playful dog named Max loved
running through the green fields...
```

### Output

```text
Story + Audio Narration
```

---

## 🔥 Generative AI Components

| Component | Technology |
|------------|------------|
| Image Captioning | BLIP |
| Story Generation | Llama 3 |
| Text Generation | Ollama |
| Audio Narration | pyttsx3 |
| Interface | Streamlit |

---

## 📈 Future Enhancements

- Multi-language Story Generation
- Voice Selection Options
- PDF Story Export
- Story Illustration Generation
- Character-Aware Storytelling
- Video Story Generation
- Cloud Deployment

---

## 💼 Resume Description

**NarraSpeech AI – Image-to-Story-to-Speech Generator (Generative AI – Multimodal AI)**

- Developed a multimodal Generative AI application that transforms images into AI-generated stories and narrated audio.
- Integrated BLIP for image captioning, Llama 3 (Ollama) for story generation, and Text-to-Speech for voice narration.
- Built an end-to-end pipeline combining Computer Vision, Large Language Models, and Speech AI using Streamlit.

---

## 🏷️ Category

```text
Generative AI
    ↓
Multimodal AI
    ↓
Image-to-Story-to-Speech Generation
```

---

## 👨💻 Author

**Varun Kurhade**

---

## 📜 License

MIT License
