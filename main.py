import os
import asyncio
from googletrans import Translator

tr = Translator()
async def translate_text(text, dest='en'):
    loop = asyncio.get_event_loop()
    try:
        translation = await loop.run_in_executor(None, lambda: tr.translate(text, dest=dest))
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    os.system('cls')
    while True:
        print("Refer to the following link for supported language codes:\nhttps://developers.google.com/workspace/admin/directory/v1/languages\n")
        text = input("Enter text to translate (or 'q' to quit): ")
        if text.lower() == 'q':
            print("Goodbye!")
            break
        dest_lang = input("Enter target language code (e.g., 'en' for English, 'fr' for French): ")
        translation = await translate_text(text, dest=dest_lang)
        print(f"Translated text: {translation}\n")

if __name__ == "__main__":
    asyncio.run(main())