import nltk
import numpy as np
import pickle
import random
import string
import warnings
import scipy
warnings.filterwarnings('ignore')



f=open('test.txt','r',errors='ignore')
raw=f.read()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

sent_tokens[:2]

word_tokens[:2]


lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
  for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity




def response(user_response):
    chatbot1_response=''
    sent_tokens.append(user_response)
    tfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = tfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=chatbot1_response+"I am sorry! I don't understand you"
        return chatbot1_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return charbot1_response


flag=True
print("Chitti: My name is Chitti. I will answer your queries about global warming. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Chitti: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Chitti: "+greeting(user_response))
            else:
                print("Chitti: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("chatbot: Bye! take care..")