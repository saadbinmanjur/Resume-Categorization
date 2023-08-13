import os
import argparse
import joblib
import pickle
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string


stop_words = stopwords.words('english')

lemmatizer = WordNetLemmatizer()

with open('model/bagging_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


# Command line arguments
parser = argparse.ArgumentParser(
    description="Categorize resumes using a trained model.")
parser.add_argument("--input_dir", type=str,
                    help="Path to input directory containing resumes")
parser.add_argument("--output_dir", type=str,
                    help="Path to output directory for categorized resumes")

args = parser.parse_args()
print(args)


def preprocess_text(text):
 # Tokenization
    tokens = word_tokenize(text.lower())

    # Removing punctuation and numeric values
    no_punct_tokens = [
        token for token in tokens if token not in string.punctuation and not token.isnumeric()]

    # Removing stop words
    no_stopwords_tokens = [
        token for token in no_punct_tokens if token not in stop_words]

    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(
        token) for token in no_stopwords_tokens]

    # Join tokens back into a string
    cleaned_text = ' '.join(lemmatized_tokens)
    return cleaned_text


def predict(text):
    text = preprocess_text(text)
    print(text)
    print(loaded_model.predict([text])[0])

    return loaded_model.predict([text])[0]


# Process resumes
resume_files = os.listdir(args.input_dir)
results = []

for resume_file in resume_files:
    resume_path = os.path.join(args.input_dir, resume_file)
    with open(resume_path, "r", encoding="utf-8") as f:
        resume_content = f.read()

    # Predict the category
    predicted_category = predict(resume_content)

    # Save categorized resume
    output_path = os.path.join(
        args.output_dir, predicted_category, resume_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(resume_content)

    results.append({"resume_file": resume_file,
                   "category": predicted_category})


# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv(os.path.join(
    args.output_dir, "categorized_resumes.csv"), index=False)
print("Processing completed!")