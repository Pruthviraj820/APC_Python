from collections import Counter

def text_analysis(text):

    words = text.lower().split()
    
    total_words = len(words)
    
    word_freq = Counter(words)
    
    top_three = word_freq.most_common(3)
    
    vowels = set("aeiou")
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    
    print("\n--- Text Analysis Report ---")
    print(f"Total number of words: {total_words}")
    print("\nWord Frequency:")
    for word, count in word_freq.items():
        print(f"{word}: {count}")
    
    print("\nTop 3 Most Frequent Words:")
    for word, count in top_three:
        print(f"{word}: {count}")
    
    print(f"\nTotal number of vowels: {vowel_count}")


text_input = input("Enter your text: ")
text_analysis(text_input)
