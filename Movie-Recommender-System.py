# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UBXi4-WQDhELz9scW19VQ_5IW1wTzH0Z
"""

# Description: Build a movie recommendation engine

# Import the libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
from google.colab import files

uploaded = files.upload()

df = pd.read_csv('movies_dataset.csv')

df.head(5)

# Get a count of the number of rows and columns
df.shape

# Create a list of important columns to keep
features = ['keywords', 'cast', 'genres', 'director']

df[features].head(3)

# Clean and process the data
for feature in features:
    df[feature] = df[feature].fillna('')  # Fill any missing values with the empty string


# Create a function to combine  the values of the important columns into a single string
def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']


# Apply the function to each row in the data set to store the combined strings into
# a new column called combined_features
df['combined_features'] = df.apply(combine_features, axis=1)

# Print the data frame
df.head(3)

# Convert a collection of text to a matrix of token counts
count_matrix = CountVectorizer().fit_transform(df['combined_features'])

# Get the cosine similarity matrix from the count matrix
cosine_sim = cosine_similarity(count_matrix)
print(cosine_sim)

# Get the number of rows and columns in cosine_sim
cosine_sim.shape


# Helper function to get the title from the index
def get_title_from_index(index):
    return df[df.index == index]['title'].values[0]


# Helper function to get the index from the tilte
def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]


# Get the title of the movie that the user likes
movie_user_likes = 'The Amazing Spider-Man'

# Find that movies index
movie_index = get_index_from_title(movie_user_likes)

movie_index

# Enumerate through all the similarity scorees of 'The Amazing Spider-Man' to make a tuple of movie index and similarity scores.
# We will return a list of tuples in the form (movie_index, similarity score)

similar_movies = list(enumerate(cosine_sim[movie_index]))

similar_movies

# Sort the list of similar movies according to the similarity scores in decs order
sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

# Print
sorted_similar_movies

# Create a loop to print the first 7 entris from the sorted similar movies list
i = 0
print('The top 7 similar movies to ' + movie_user_likes + ' are:')
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i = i + 1
    if i >= 7:
        break
