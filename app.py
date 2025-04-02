import asyncio
import streamlit as st
from googletrans import Translator

tr = Translator()
async def translate_text(text, dest='en'):
    loop = asyncio.get_event_loop()
    try:
        translation = await loop.run_in_executor(None, lambda: tr.translate(text, dest=dest))
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.write("Refer to the following link for supported language codes:\nhttps://developers.google.com/workspace/admin/directory/v1/languages\n")
    text = st.text_input("Enter text to translate:")
    dest_lang = st.text_input("Enter target language code (e.g., 'en' for English, 'fr' for French):")
    
    if st.button("Translate"):
        if text and dest_lang:
            translation = asyncio.run(translate_text(text, dest=dest_lang))
            st.write(f"Translated text: {translation}")
        else:
            st.write("Please enter both text and target language.")

if __name__ == "__main__":
    main()