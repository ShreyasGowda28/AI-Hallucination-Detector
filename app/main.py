from generator import generate_samples
from detector import HallucinationDetector


def main():

    print("=" * 70)
    print("AI Hallucination Detector")
    print("=" * 70)

    question = input("\nAsk a question: ")

    # Generate responses
    answers = generate_samples(question)

    main_answer = answers[0]
    sampled_answers = answers[1:]

    print("\n")
    print("=" * 70)
    print("MAIN ANSWER")
    print("=" * 70)

    print(main_answer)

    detector = HallucinationDetector()

    results = detector.analyze(
        main_answer,
        sampled_answers
    )

    print("\n")
    print("=" * 70)
    print("HALLUCINATION ANALYSIS")
    print("=" * 70)

    for result in results:

        print(f"\nRisk : {result['risk']}")
        print(f"Score: {result['score']:.3f}")
        print(result["sentence"])


if __name__ == "__main__":
    main()