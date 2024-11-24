import streamlit as st
import pickle
import pandas as pd
import requests

# Load the model
movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies



st.title("MOvie Recommender System")
selected_movie = st.selectbox("Select a movie", movies["title"].values)
if st.button("Recommend"):
    recommendation=recommend(selected_movie)
    for i in recommendation:
        st.write(i)
        
    
        