import requests
import json

# Language mapping: names to codes
LANGUAGE_MAP = {
    "english": "en",
    "german": "de",
    "spanish": "es",
    "french": "fr",
    "hindi": "hi",
    "chinese": "zh",
    "japanese": "ja",
    "russian": "ru",
    "arabic": "ar",
    "portuguese": "pt"
}

def get_language_code(language_name):
    """Get the language code from the name."""
    language_code = LANGUAGE_MAP.get(language_name.lower())
    if not language_code:
        raise ValueError(f"Unsupported language: {language_name}")
    return language_code

def translate_text_google(api_key, text, source_lang, target_lang):
    """Translate text using Google Translate API."""
    # Mock translation for demonstration
    translations = {
        ("नमस्ते दुनिया", "hi", "en"): "Hello World",
        ("हैलो", "hi", "en"): "Hello",
        ("bonjour", "fr", "en"): "Hello"
    }
    return translations.get((text.lower(), source_lang, target_lang), "[Mock Translation Unavailable]")

def translate_text_microsoft(api_key, region, text, source_lang, target_lang):
    """Translate text using Microsoft Translator API."""
    # Mock translation for demonstration
    translations = {
        ("नमस्ते दुनिया", "hi", "en"): "Hello World",
        ("हैलो", "hi", "en"): "Hello",
        ("bonjour", "fr", "en"): "Hello"
    }
    return translations.get((text.lower(), source_lang, target_lang), "[Mock Translation Unavailable]")

def unified_translation_output(text, google_api_key, microsoft_api_key, microsoft_region, source_lang, target_lang):
    """Combine translations from Google and Microsoft into a single output."""
    google_translation = translate_text_google(google_api_key, text, source_lang, target_lang)
    microsoft_translation = translate_text_microsoft(microsoft_api_key, microsoft_region, text, source_lang, target_lang)

    # Combine translations intelligently
    if google_translation and microsoft_translation:
        if google_translation.lower() == microsoft_translation.lower():
            final_translation = google_translation  # Use either as they match
        else:
            final_translation = f"{google_translation} / {microsoft_translation}"  # Combine if different
    elif google_translation:
        final_translation = google_translation
    elif microsoft_translation:
        final_translation = microsoft_translation
    else:
        final_translation = "Error: Unable to translate the text with both APIs."

    # Unified output
    combined_output = (
        f"Original Text: {text}\n"
        f"Source Language: {source_lang.capitalize()}\n"
        f"Target Language: {target_lang.capitalize()}\n\n"
        f"Translation: {final_translation}\n"
    )
    return combined_output

if __name__ == "__main__":
    print("Welcome to the Language Translation Tool!")

    try:
        while True:
            # Ask for source and target languages
            source_lang_name = input("\nEnter the source language (e.g., 'German', 'French'): ").strip()
            target_lang_name = input("Enter the target language (e.g., 'English', 'Spanish'): ").strip()

            # Map language names to codes
            source_lang = get_language_code(source_lang_name)
            target_lang = get_language_code(target_lang_name)

            # Take user input for text to translate
            text_to_translate = input(f"\nEnter the text you want to translate (from {source_lang_name} to {target_lang_name}): ").strip()

            # API keys and region configuration (ensure these are securely stored in a real application)
            google_api_key = "AIzaSyF5gH0xT2JxXxL7Km8rOq3VvU6YzA9bN6F"
            microsoft_api_key = "a3f1d2d4-982f-459f-a7b5-87c0b56778d9"
            microsoft_region = "northeur"

            # Get unified translation output
            output = unified_translation_output(
                text_to_translate, google_api_key, microsoft_api_key, microsoft_region, source_lang, target_lang
            )

            # Display unified output
            print("\nTranslation Result:")
            print(output)

            # Ask user if they want to continue
            continue_choice = input("\nDo you want to translate another text? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("\nThank you for using the Language Translation Tool. Goodbye!")
                break
    except ValueError as e:
        print(f"Error: {e}")
