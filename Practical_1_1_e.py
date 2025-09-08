def most_occurring_words():
   
    print("--- Question 5: Most Occurring Words ---")
    sentence = "The quick brown fox jumps over the lazy dog. The quick dog is brown."
    print(f"The sentence is: '{sentence}'")

    # Convert to lowercase, remove period, and split into words
    words = sentence.lower().replace('.', '').split()
    word_counts = {}

    # Count occurrences
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    if word_counts:
        max_count = max(word_counts.values())
        most_common = [word for word, count in word_counts.items() if count == max_count]

        print(f"The word(s) with the highest frequency ({max_count}) are: {most_common}")
    else:
        print("The sentence is empty.")
    print("\n" + "-"*40 + "\n")


# Run function
if __name__ == "__main__":
    most_occurring_words()