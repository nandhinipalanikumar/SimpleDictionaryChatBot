import numpy as np
import nltk
import string
import random

from nltk.corpus import stopwords

f=open(r"C:\Users\Jayalakshmi\Documents\EngChatBo.txt",errors='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
sent_tokens=nltk.sent_tokenize(raw_doc)
word_tokens=nltk.word_tokenize(raw_doc)
lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return[lemmer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREET_INPUTS = ("hello", "hey", "hi", "greetings", "sup", "wassup", "what's up", "hlo")
GREET_RESPONSES = ("hello", "hey", "hi", "greetings", "sup", "hi there", "HEY! I'm glad you found me", "hlo")


def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)


GOOD_MORN_INPUTS = ("gm", "good morning", "morning")
GOOD_MORN_RESPONSES = ("Hlo bud! Great day", "Hello, Good morning:)", "Hey pal. How can I help you?", "Good morning<3")


def morn(sentence):
    for word in sentence.split():
        if word.lower() in GOOD_MORN_INPUTS:
            return random.choice(GOOD_MORN_RESPONSES)


GOOD_AFT_INPUTS = ("ga", "good afternoon", "good noon", "noon")
GOOD_AFT_RESPONSES = ("Hlo bud! Great day", "Hello, Good afternoon:)", "Hey pal. How can I help you?", "Good afternoon<3",
"HEY,NOON! How was lunch?")

def aft(sentence):
    for word in sentence.split():
        if word.lower() in GOOD_AFT_INPUTS:
            return random.choice(GOOD_AFT_RESPONSES)


GOOD_EVE_INPUTS = ("ge", "good evening", "good eve", "eve")
GOOD_EVE_RESPONSES = ("Hlo bud! Great eve", "Hello, Good evening:)", "Greetings pal. How can I help you?", "Good evening<3",
                      "HEY,GUD EVE! Had dinner?")


def eve(sentence):
    for word in sentence.split():
        if word.lower() in GOOD_EVE_INPUTS:
            return random.choice(GOOD_EVE_RESPONSES)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
  robo1_response=''
  TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,)
  tfidf=TfidfVec.fit_transform(sent_tokens)
  vals=cosine_similarity(tfidf[-1],tfidf)
  idx=vals.argsort()[0][-2]
  flat=vals.flatten()
  flat.sort()
  req_tfidf=flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"I am sorry! I couldn't find a way to help you"
    return robo1_response
  else:
    robo1_response=robo1_response+sent_tokens[idx]
    return robo1_response
flag = True
print("BOT:Hey,glad to help you! I'm NVocab. Let's have a chat. Also, feel free to exit anytime just by typing bye!")
while (flag == True):
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("BOT: You're welcome...")
        else:
            if (greet(user_response) != None):
                  print("BOT: " + greet(user_response))
            elif (morn(user_response) != None):
                  print("BOT: " + morn(user_response))
            elif (aft(user_response) != None):
                  print("BOT: " + aft(user_response))
            elif (eve(user_response) != None):
                  print("BOT: " + eve(user_response))
            else:
                  sent_tokens.append(user_response)
                  word_tokens = word_tokens + nltk.word_tokenize(user_response)
                  final_words = list(set(word_tokens))
                  print("BOT: ", end="")
                  print(response(user_response))
                  sent_tokens.remove(user_response)
    else:
            flag = False
            print("BOT: Goodbye! TC<3")
