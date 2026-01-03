def analyze_text(text):
    # Convert to lowercase
    text = text.lower()

    # Sentence count
    sentence_count = 0
    for char in text:
        if char == '.' or char == '!' or char == '?':
            sentence_count += 1

    # Remove punctuation manually
    cleaned_text = ""
    punctuation = ".,!?;:'\"()[]{}"

    for char in text:
        if char not in punctuation:
            cleaned_text += char

    # Word count and frequency dictionary
    words = cleaned_text.split()
    word_count = 0
    frequency = {}

    for word in words:
        word_count += 1
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find top 10 most frequent words manually
    top_10 = []

    for _ in range(10):
        max_word = None
        max_count = 0

        for word in frequency:
            if frequency[word] > max_count:
                max_count = frequency[word]
                max_word = word

        if max_word is None:
            break

        top_10.append((max_word, max_count))
        frequency[max_word] = 0  # so it won’t be selected again

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10
    }



