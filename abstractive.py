from transformers import pipeline
import torch

device = 0 if torch.backends.mps.is_available() else -1

summarizer = pipeline(
    "summarization",
    model="cointegrated/rut5-small",
    tokenizer="cointegrated/rut5-small",
    device=device,
    framework="pt"
)

def abstractive_summary(text: str) -> str:
    input_length = len(text.split())
    max_len = min(max(20, int(input_length * 0.5)), 50)
    min_len = min(10, max_len - 1)

    result = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False,
        num_beams=4,
        repetition_penalty=2.0,
        no_repeat_ngram_size=2,
        early_stopping=True,
        clean_up_tokenization_spaces=True
    )

    summary = result[0]['summary_text'].strip()
    first_sentence = summary.split('.')[0].strip()
    return first_sentence + '.' if first_sentence else summary
