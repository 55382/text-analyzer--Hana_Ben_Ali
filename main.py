from analyzer import analyze_text
def main():
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    results = analyze_text(text)

    print("Text Analysis Results")
    print("---------------------")
    print(f"Word Count: {results['word_count']}")
    print(f"Sentence Count: {results['sentence_count']}")
    print("Top 10 Most Frequent Words:")

    for word, freq in results["top_10_words"]:
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
