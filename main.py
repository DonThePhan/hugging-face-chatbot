from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()


def start_chatbot():
    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        token=os.getenv("HUGGING_FACE_TOKEN")
    )

    prompt = ''

    while True:
        prompt = input('You:')
        if prompt == 'exit':
            print('Okay bye!')
            break

        response = client.text_generation(
            prompt=prompt,
            max_new_tokens=50
        )

        print(response)


if __name__ == "__main__":
    start_chatbot()
