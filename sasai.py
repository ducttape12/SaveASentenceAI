import time

from ollama import chat
from ollama import ChatResponse

def generate_sentence(topic):
    prompt = f"Generate a single sentence about {topic}."
    print()
    print("Please wait while the sentence is written...")

    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    print()
    print("Sentence writing completed!")

    return response.message.content


def save_sentence():
    topic = input("Enter a topic: ")

    sentence = generate_sentence(topic)

    return sentence

def load_sentence(sentence):
    print("Please wait... loading...")
    time.sleep(1)

    print()
    print("Your sentence:")
    print(sentence)

def main_menu():
    sentence = ""

    while True:
        print("AI Save a Sentence: AI-Powered AI Sentence Saver with AI")
        print("--------------------------------------------------------")
        print("1. Generate and save a sentence")
        print("2. Load a sentence")
        print("3. Quit")
        print()
        selection = input("Choose an option: ")
        print()

        if selection == "1":
            sentence = save_sentence()
        elif selection == "2":
            load_sentence(sentence)
        elif selection == "3":
            print("WARNING: Your sentence will be lost if you quit!")
            really_quit = input("Do you want to quit? (Y/N) ")

            if really_quit == "y" or really_quit == "Y":
                break

        print()
        print()

    print("Thanks for using AI Save a Sentence: AI-Powered AI Sentence Saver with AI!")

if __name__ == "__main__":
    main_menu()
