from textblob import TextBlob
from googletrans import Translator

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    translated_text = translation.text

    return translated_text

def main():
    # Sample text
    text = input("Enter text: ")

    # Analyze sentiment
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

    # Language translation
    target_languages = ["es", "fr", "de", "hi", "gu"]  # Add more language codes here
    languages = {
        'spanish': 'es',
        'french': 'fr',
        'german': 'de',
        'hindi': 'hi',
        'gujarati': 'gu'
    }

    print('CODE for different languages:')
    for language, code in languages.items():
        print(f'{language}: {code}')

    lang = input('Enter the code of the language you want to translate into:')
    if lang in target_languages:
        print("\nTranslated Texts:")
        translated_text = translate_text(text, lang)
        print(f"{lang}: {translated_text}")
    else:
        print("Invalid language code.")

if __name__ == "__main__":
    main()
