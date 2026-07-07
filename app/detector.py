import torch
import spacy

from utils import clean_text
from selfcheckgpt.modeling_selfcheck import SelfCheckNLI


class HallucinationDetector:

    def __init__(self):

        print("Loading spaCy...")
        self.nlp = spacy.load("en_core_web_sm")

        print("Loading SelfCheck-NLI...")

        device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.checker = SelfCheckNLI(
            device=device
        )

    def analyze(self, main_answer, sampled_answers):

        # Clean markdown
        main_answer = clean_text(main_answer)

        # Split into sentences
        sentences = [
            sent.text.strip()
            for sent in self.nlp(main_answer).sents
            if sent.text.strip()
        ]

        # Predict hallucination scores
        scores = self.checker.predict(
            sentences=sentences,
            sampled_passages=sampled_answers
        )

        results = []

        for sentence, score in zip(sentences, scores):

            score = float(score)

            if score < 0.20:
                risk = "LOW"
            elif score < 0.50:
                risk = "MEDIUM"
            else:
                risk = "HIGH"

            results.append(
                {
                    "sentence": sentence,
                    "score": score,
                    "risk": risk
                }
            )

        return results