import string
import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

""" Preprocessing the text """
with open("1.Harry Potter and the Sorcerer's Stone.txt", encoding="ISO-8859-1") as text:
    contents = text.read()

# Convert text to lowercase
contents = contents.lower()

# Remove numbers
contents = re.sub(r'\d+', '', contents)

# Remove punctuatons
contents = contents.translate(str.maketrans("","", string.punctuation))

# Tokenization and remove stop words
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(contents)
contents_list = []
for i in tokens:
    if not i in stop_words:
        contents_list.append(i)

# Stemming
stemmer = PorterStemmer()
words = [stemmer.stem(word) for word in contents_list]

# Lemmatization
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word) for word in words]

print(len(words))
