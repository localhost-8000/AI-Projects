# -*- coding: utf-8 -*-
"""MailSpamDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bDM476cEi5dfKDmHOlvQnLf-_9PY80my
"""

# Description: This program detects if an email is spam or not.

# Import libraries
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

#Load the data
from google.colab import files
uploaded = files.upload()

#Read the CSV file
df = pd.read_csv('emails.csv')

#Print the first 5 rows of data
df.head(5)

# Print the shape i.e. get the number of rows and columns
df.shape

# Get the columns names
df.columns

# Check for duplicates and remove them
df.drop_duplicates(inplace = True)

# Show the new shape of dataset
df.shape

#Show the number of missing data for each column
df.isnull().sum()

# Download the stopword package
nltk.download('stopwords')

def process_text(text):
  #1 remove punctuation
  #2 remove stopwords
  #3 return a list of clean text words

  nopunc = [char for char in text if char not in string.punctuation]
  nopunc = ''.join(nopunc)

  clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

  return clean_words

# Show the tokenization i.e. a list of tokens
df['text'].head().apply(process_text)

# Convert a collection of text to a matrix of tokens
from sklearn.feature_extraction.text import CountVectorizer
messages_bow = CountVectorizer(analyzer = process_text).fit_transform(df['text'])

#Split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(messages_bow, df['spam'], test_size = 0.20, random_state = 0)

#Get the shape of messages_bow
messages_bow.shape

# Create and train the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(X_train, Y_train)

# Print the predictions
print(classifier.predict(X_train))

#Print the actual values
print(Y_train.values)

# Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(X_train)
print(classification_report(Y_train, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(Y_train, pred))
print()
print('Accuracy: ', accuracy_score(Y_train, pred))

# Test the data set
# Print the predictions
print(classifier.predict(X_test))

#Print the actual values
print(Y_test.values)

# Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(X_test)
print(classification_report(Y_test, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(Y_test, pred))
print()
print('Accuracy: ', accuracy_score(Y_test, pred))