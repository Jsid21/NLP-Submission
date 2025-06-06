from transformers import pipeline

model1_name = "cardiffnlp/twitter-roberta-base-sentiment"
sa_pipeline1 = pipeline("sentiment-analysis", model=model1_name)

model2_name = "distilbert-base-uncased-finetuned-sst-2-english"
sa_pipeline2 = pipeline("sentiment-analysis", model=model2_name)

label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}

texts = [
    "I absolutely love this product! It's amazing.",
    "The experience was terrible, I would not recommend it.",
    "The movie was okay, not the best but not the worst either.",
    "This service is exceptional and exceeded my expectations.",
    "I'm very disappointed with the quality of the item."
]
def ensemble_sentiment(text):
    result1 = sa_pipeline1(text)[0]
    result2 = sa_pipeline2(text)[0]

    label1 = label_map.get(result1["label"], result1["label"])
    label2 = result2["label"].capitalize()

    if label1 == label2:
        final_label = label1
    else:
        final_label = label1 if result1["score"] >= result2["score"] else label2

    return {
        "text": text,
        "model1": {"label": label1, "score": result1["score"]},
        "model2": result2,
        "ensemble": final_label
    }

for text in texts:
    result = ensemble_sentiment(text)
    print(f"Text: {result['text']}")
    print(f" Model 1 ({model1_name}): {result['model1']}")
    print(f" Model 2 ({model2_name}): {result['model2']}")
    print(f" Ensemble Sentiment: {result['ensemble']}")
    print("-" * 60)
