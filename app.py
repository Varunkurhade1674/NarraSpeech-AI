import os
import sys

# Windows-specific DLL directory and path loading fallback for pywin32
if sys.platform == "win32":
    for path in list(sys.path):
        if "site-packages" in path:
            win32_path = os.path.join(path, "win32")
            win32_lib = os.path.join(path, "win32", "lib")
            pywin32_sys32 = os.path.join(path, "pywin32_system32")
            if os.path.isdir(win32_path) and win32_path not in sys.path:
                sys.path.insert(0, win32_path)
            if os.path.isdir(win32_lib) and win32_lib not in sys.path:
                sys.path.insert(0, win32_lib)
            if os.path.isdir(pywin32_sys32):
                try:
                    os.add_dll_directory(pywin32_sys32)
                except Exception:
                    pass

import time
from typing import Any

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from PIL import Image
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama
# pyrefly: ignore [missing-import]
from transformers import BlipProcessor, BlipForConditionalGeneration

from utils.custom import css_code

load_dotenv(find_dotenv())


def get_ollama_models() -> list[str]:
    """
    Fetch the list of installed local Ollama models.
    :return: List of model names as strings.
    """
    try:
        # pyrefly: ignore [missing-import]
        import ollama
        response = ollama.list()
        models = []
        for m in response.models:
            if hasattr(m, 'model') and m.model:
                models.append(m.model)
            elif isinstance(m, dict) and 'model' in m:
                models.append(m['model'])
            elif isinstance(m, dict) and 'name' in m:
                models.append(m['name'])
        return models
    except Exception as e:
        print(f"Error connecting to local Ollama service: {e}")
        return []


def progress_bar(amount_of_time: int) -> Any:
    """
    A very simple progress bar the increases over time,
    then disappears when it reached completion
    :param amount_of_time: time taken
    :return: None
    """
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()


def generate_text_from_image(url: str) -> str:
    """
    A function that uses the blip model to generate text from an image.
    :param url: image location
    :return: text: generated text from the image
    """
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    raw_image = Image.open(url).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs)
    generated_text: str = processor.decode(out[0], skip_special_tokens=True)

    print(f"IMAGE INPUT: {url}")
    print(f"GENERATED TEXT OUTPUT: {generated_text}")
    return generated_text


def generate_story_from_text(scenario: str, model_name: str) -> str:
    """
    A function using a prompt template and local Ollama model to generate a short story.
    :param scenario: generated text from the image
    :param model_name: Name of the Ollama model to use
    :return: generated story from the text
    """
    prompt_template: str = f"""
    You are a talented story teller who can create a story from a simple narrative./
    Create a story using the following scenario; the story should have be maximum 50 words long;
    
    CONTEXT: {scenario}
    STORY:
    """

    prompt: PromptTemplate = PromptTemplate(template=prompt_template, input_variables=["scenario"])

    llm: Any = ChatOllama(model=model_name, temperature=0.9)

    story_chain = prompt | llm | StrOutputParser()

    generated_story: str = story_chain.invoke({"scenario": scenario})

    print(f"TEXT INPUT: {scenario}")
    print(f"GENERATED STORY OUTPUT: {generated_story}")
    return generated_story


def get_local_voices() -> list[dict[str, str]]:
    """
    Fetch the list of installed local TTS voices.
    :return: List of voice dictionaries with 'id' and 'name'.
    """
    try:
        # pyrefly: ignore [missing-import]
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        res = []
        for v in voices:
            res.append({
                "id": v.id,
                "name": v.name
            })
        return res
    except Exception:
        return []


def generate_speech_from_text(
    message: str, 
    voice_id: str = None, 
    rate: int = 200, 
    volume: float = 1.0
) -> str:
    """
    A function that uses a local, offline pyttsx3 engine to convert text to speech.
    :param message: short story generated by the GPT model
    :param voice_id: Optional local pyttsx3 voice ID
    :param rate: Speed of local speech (default 200)
    :param volume: Volume of local speech (default 1.0)
    :return: path to the generated audio file
    """
    try:
        # pyrefly: ignore [missing-import]
        import pyttsx3
        engine = pyttsx3.init()
        if voice_id:
            engine.setProperty('voice', voice_id)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        audio_path = "generated_audio.wav"
        engine.save_to_file(message, audio_path)
        engine.runAndWait()
        return audio_path
    except Exception as local_e:
        st.error(f"Local text-to-speech engine failed: {local_e}")
        raise local_e


def main() -> None:
    """
    Main function
    :return: None
    """
    st.set_page_config(page_title="NarraSpeech AI", page_icon="🖼️")

    st.markdown(css_code, unsafe_allow_html=True)

    # Fetch available Ollama models
    available_models = get_ollama_models()

    with st.sidebar:
        st.subheader("Ollama Configuration")
        
        selected_model = None
        if available_models:
            selected_model = st.selectbox(
                "Select Ollama Model", 
                options=available_models,
                index=0
            )
        else:
            st.error("No Ollama models found!")
            st.markdown("""
            **Ollama Setup Instructions:**
            Please open your terminal and pull a model to get started:
            * `ollama pull llama3`
            * `ollama pull mistral`
            * `ollama pull gemma3`
            """)

        st.write("---")
        st.subheader("Local Speech Generation (Offline)")
        local_voices = get_local_voices()
        selected_voice_id = None
        if local_voices:
            selected_voice = st.selectbox(
                "Select Local Voice",
                options=local_voices,
                format_func=lambda x: x["name"]
            )
            selected_voice_id = selected_voice["id"]
        else:
            st.info("No local TTS voices detected.")
            
        tts_rate = st.slider("Speech Rate (Speed)", min_value=100, max_value=300, value=200, step=10)
        tts_volume = st.slider("Speech Volume", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
        
        st.write("---")
        st.markdown("""
        <div class="status-card">
            <div class="status-label">Engine Pipeline</div>
            <div style="display:flex; align-items:center; gap:8px;">
                <span class="status-dot"></span>
                <span class="status-text">Fully Local Mode Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">✨ NarraSpeech AI</h1>
        <p class="subtitle-text">Transform your images into captivating local audio stories completely offline.</p>
    </div>
    """, unsafe_allow_html=True)
    uploaded_file: Any = st.file_uploader("Please choose a file to upload", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_file is not None:
        if not available_models:
            st.error("Cannot generate story because no Ollama models are installed. Please install a model first using: `ollama pull llama3`")
            st.stop()

        print(uploaded_file)
        bytes_data: Any = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)

        # Restructured side-by-side layout
        col1, col2 = st.columns([1, 1], gap="medium")

        with col1:
            st.markdown("<h3 class='section-title'>🖼️ Uploaded Image</h3>", unsafe_allow_html=True)
            st.image(uploaded_file, caption="Input Image", width="stretch")

        with col2:
            st.markdown("<h3 class='section-title'>✨ Generated Narrative & Speech</h3>", unsafe_allow_html=True)
            
            with st.spinner("Analyzing image..."):
                scenario: str = generate_text_from_image(uploaded_file.name)
            
            with st.spinner("Generating story..."):
                story: str = generate_story_from_text(scenario, selected_model)
                
            with st.spinner("Synthesizing speech..."):
                audio_file = generate_speech_from_text(
                    story, 
                    voice_id=selected_voice_id, 
                    rate=tts_rate, 
                    volume=tts_volume
                )

            st.markdown(f"""
            <div class="result-card">
                <div class="card-label">🔍 Image Analysis</div>
                <div class="card-text">{scenario}</div>
            </div>
            <div class="result-card highlight-card">
                <div class="card-label">📖 Generated Story</div>
                <div class="card-text">{story}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='audio-title'>🎵 Listen to Story:</div>", unsafe_allow_html=True)
            st.audio(audio_file)


if __name__ == "__main__":
    main()