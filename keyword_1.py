reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
keywords = 'good' ',' 'excellent' ',' 'bad' ',' 'poor' ',' 'average'
keyword_cap = keywords.upper()
print(keyword_cap)

def count_sentiment_words(reviews, positive_words, negative_words):
    # Convert the review to lowercase and split it into words
   
    positive_count = 0
    negative_count = 0


    for word in words:
    
        if word in positive_words:
            positive_count += 1
       
        elif word in negative_words:
            negative_count += 1

    return positive_count, negative_count

positive_words ='good' ',' 'excellent' ',' 'great' ',' 'awesome' ',' 'fanastic' ',' 'superb' ',' 'amazing'
negative_words = 'bad' ',' 'poor' ',' 'terrible' ',' 'horrible' ',' 'awful' ',' 'disappointing' ',' 'subpar'
words = positive_words.lower()
words = negative_words.lower()
positive_count, negative_count = count_sentiment_words(reviews, positive_words, negative_words)
print(f"Positive words: {positive_words}, Negative Words:{negative_words}")