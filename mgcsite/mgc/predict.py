from keras.models import load_model
import numpy as np

model_path = "static/model/mfcc20_conv1d.keras"

model = load_model(model_path)


def predict(preprocessed_audio):
    # Manual genre mapping
    genre_mapping = {
        0: "blues",
        1: "classical",
        2: "country",
        3: "disco",
        4: "hiphop",
        5: "jazz",
        6: "metal",
        7: "pop",
        8: "reggae",
        9: "rock",
    }
    predictions = model.predict(preprocessed_audio)
    print(predictions)
    # mean_probabilities = np.mean(predictions, axis=0)
    predicted_classes = np.argmax(predictions, axis=1)
    # Confidence scores for each segment (probabilities corresponding to predicted class)
    confidence_scores = predictions[np.arange(len(predictions)), predicted_classes]

    # Aggregate predictions for the entire song
    predicted_genre = np.bincount(
        predicted_classes
    ).argmax()  # Most frequent predicted class
    print("Predicted Genre for Entire Song:", predicted_genre)

    # Aggregate confidence scores for the entire song
    overall_confidence_score = np.mean(
        confidence_scores
    )  # Example: Taking the average confidence score
    print("Overall Confidence Score for Entire Song:", overall_confidence_score)
    # most_likely_genre_index = np.argmax(mean_probabilities)

    # Get the overall predicted genre
    overall_predicted_genre = genre_mapping[predicted_genre]

    return overall_predicted_genre, overall_confidence_score
