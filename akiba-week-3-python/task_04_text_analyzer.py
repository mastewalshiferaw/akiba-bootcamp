def clean_and_tokenize(text):

    punctuation = ".,!?;:'\"-()[]{}<>/\\|@#$%^&*~`"
    cleaned_chars = []

    for char in text.lower():
        if char in punctuation:
            cleaned_chars.append(" ")  
        else:
            cleaned_chars.append(char)

    cleaned_text = "".join(cleaned_chars)
  
    return cleaned_text.split()


def count_words(words):
    
    return len(words)


def count_characters_no_spaces(text):
   
    return sum(1 for char in text if not char.isspace())


def count_vowels_and_consonants(text):
    
    vowels = set("aeiou")
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


def find_longest_word(words):

    if not words:
        return ""
    return max(words, key=len)


def count_word_frequencies(words):
    
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def find_repeated_words(frequencies):
   
    return [word for word, count in frequencies.items() if count > 1]


def get_top_n_frequent_words(frequencies, n=5):

    sorted_words = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]


