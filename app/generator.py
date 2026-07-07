from ollama import chat
from config import (
    OLLAMA_MODEL,
    NUM_SAMPLES,
    TEMPERATURE,
    TOP_P
)


def generate_samples(question):
    """
    Generate multiple responses from Ollama.
    """

    answers = []

    for i in range(NUM_SAMPLES):

        print(f"Generating response {i+1}/{NUM_SAMPLES}...")

        response = chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            options={
                "temperature": TEMPERATURE,
                "top_p": TOP_P,
            },
        )

        answers.append(response["message"]["content"])

    return answers