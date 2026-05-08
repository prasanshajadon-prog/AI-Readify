# 📖 Readify AI: Extract & Speak Text Instantly

A simple and practical tool that extracts text from images and converts it into speech in seconds.

Upload an image, let Azure handle OCR and speech synthesis, and get both readable text and downloadable audio — all in one place.

---

## 🚀 What This Project Does

1. Upload an image (JPG, PNG, BMP, TIFF, WebP)
2. Extract text using Azure Computer Vision (OCR)
3. Convert extracted text into speech using Azure Speech Service
4. Display the text along with word and character count
5. Play the generated audio
6. Download the audio file (.wav)

---

## 🧠 Tech Stack

| Layer   | Technology                              |
|--------|------------------------------------------|
| UI     | Streamlit (Python)                       |
| OCR    | Azure Computer Vision (Read API)         |
| Speech | Azure Speech Service (Text-to-Speech)    |
| Config | python-dotenv (.env file)                |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/prasanshajadon-prog/AI-Readify
cd readify-ai