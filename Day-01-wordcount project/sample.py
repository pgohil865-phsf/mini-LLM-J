def clean_text(text): #created function named clean_text 
    import string #(imported string)
    text = text.lower() #converted text into lowercase
    for char in string.punctuation: # replaced punctuation with empty string
        text = text.replace(char,"")
    return text

def word_count(file_path): #created function named word_count that takes file_path as an argument
    with open(file_path,"r") as file:
        text = file.read() #read the file

        text = clean_text(text) #cleaned the text using clean_text function
        words = text.split() #split the text into words

        word_count={} #created an empty dictionary to store word counts

        for word in words: #iterated through each word in the list of words
            if word in word_count: #if the word is already in the dictionary, increment its count
                word_count[word] +=1 #incremented the count of the word by 1
            else:
                word_count[word] = 1 #if the word is not in the dictionary, add it with a count of 1

        return word_count #returned the word count dictionary
    
def display_top_words(word_count, top_n=10): #created a function named display_top_words that takes word_count and top_n as arguments
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True) #sorted the word count dictionary by count in descending order
    print("\n Top words : \n")
    for word, count in sorted_words[:top_n]: #iterated through the top_n words and their counts
        print(f"{word}: {count}") #printed the word and its count

file_path = "sample.txt" #defined the file path to the text file
counts = word_count(file_path) #called the word_count function to get the word counts from the specified file
display_top_words(counts) #called the display_top_words function to display the top words and their counts  z