# OCR → Voice

A small but handy tool that pulls text out of images and reads it aloud. Upload a picture, let Azure do the heavy lifting (OCR + speech synthesis), and get both the extracted text and a downloadable audio file — all from a single browser tab.

Built with **Streamlit** on the frontend and **Azure Cognitive Services** on the backend.

---

## What It Does

1. You upload an image (screenshot, photo of a document, scanned page, whatever).
2. Azure's Computer Vision API reads every line of text in that image.
3. Azure's Speech Service turns that text into natural-sounding speech.
4. You get the extracted text on screen, word/character counts, and a `.wav` file you can play or download.

That's it. No accounts to create inside the app, no complicated steps.

---

## Quick Look at the Stack

| Layer     | Tech                                  |
|-----------|---------------------------------------|
| UI        | Streamlit (Python)                    |
| OCR       | Azure Computer Vision (Read API)      |
| Speech    | Azure Speech Service (Text-to-Speech) |
| Config    | `.env` file via `python-dotenv`       |

---

## Getting Started

### Prerequisites

- **Python 3.9+** installed on your machine.
- An **Azure account** with two resources provisioned:
  - [Computer Vision](https://portal.azure.com/#create/Microsoft.CognitiveServicesComputerVision) — for the OCR part.
  - [Speech Service](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) — for text-to-speech.

### 1. Clone or download this repo

```bash
git clone https://github.com/Prashray21/Readify-AI.git
cd Readify-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Azure keys

Create a `.env` file in the project root (there's already a template in the repo). Fill in your own credentials:

```
VISION_KEY=your_vision_api_key_here
VISION_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
SPEECH_KEY=your_speech_api_key_here
SPEECH_REGION=eastus
```

> **Heads up:** Never commit real API keys to a public repo. The `.env` file should be in your `.gitignore`.

### 4. Run the app

```bash
streamlit run Abishek_sir_project_azure_ocr_to_speech.py
```

Streamlit will open a new browser tab at `http://localhost:8501`. That's your app.

---

## How to Use

1. Click the upload area and pick an image (PNG, JPG, BMP, TIFF, or WebP).
2. Hit **"✨ Extract Text & Generate Speech"**.
3. Wait a few seconds — the spinner will show progress.
4. Once done, the left panel shows the extracted text with stats (word count, character count), and the right panel has the audio player plus a download button.
5. **The audio plays automatically in your browser** — no extra clicks needed.

For best results, use images where the text is clearly visible. High-contrast, well-lit photos work best. Blurry or heavily stylized text might not come through perfectly.

---

## Project Structure

```
.
├── Abishek_sir_project_azure_ocr_to_speech.py   # Main app — everything lives here
├── .env                                          # Your Azure API keys (not committed)
└── README.md                                     # You're reading this
```

It's a single-file project on purpose. Keeps things simple and easy to hand off or deploy.

---

## Supported Image Formats

- PNG
- JPEG / JPG
- BMP
- TIFF
- WebP

---

## Troubleshooting

**"Missing Azure credentials"** error on launch?
→ Double-check your `.env` file. Make sure the variable names match exactly: `VISION_KEY`, `VISION_ENDPOINT`, `SPEECH_KEY`, `SPEECH_REGION`.

**OCR returns empty text?**
→ The image might be too blurry, too small, or the text might be in a language/script Azure doesn't handle well. Try a cleaner scan.

**Speech synthesis fails or gets canceled?**
→ Usually a quota or region issue on the Azure side. Verify your Speech resource is active and the region in `.env` matches the one you created the resource in.

---

## Deployment

The easiest way to deploy **Readify AI** is using **Streamlit Community Cloud**:

1.  Push your code to a GitHub repository.
2.  Go to [share.streamlit.io](https://share.streamlit.io/) and connect your account.
3.  Click **"New app"** and select your repo/branch.
4.  **Important**: Before clicking Deploy, go to **Advanced Settings** -> **Secrets** and paste your Azure credentials there:
    ```toml
    VISION_KEY = "your_key"
    VISION_ENDPOINT = "your_endpoint"
    SPEECH_KEY = "your_key"
    SPEECH_REGION = "your_region"
    ```
5.  Click **Deploy**!

---

## License

This project doesn't currently ship with a license file. If you're planning to share it, consider adding an MIT or Apache 2.0 license.

---

Built by **Prashray Sharma** — [GitHub](https://github.com/Prashray21) · [Portfolio](https://prashraysharma.netlify.app/) · [prashraysharma805@gmail.com](mailto:prashraysharma805@gmail.com)
