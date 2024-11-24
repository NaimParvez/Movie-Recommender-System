# Movie Recommender System

This project is a **content-based movie recommendation system** powered by **Python** and **Streamlit**. It uses movie data collected from **TMDB (The Movie Database)** to suggest movies similar to the ones you like.

## Features

- **Content-Based Recommendations**: The system generates recommendations based on movie attributes like genres, cast, and crew.
- **Interactive Web Interface**: Built with **Streamlit** for a seamless user experience.
- **Dynamic Similarity Matrix**: The `similarity.pkl` file storing the movie similarity matrix is automatically regenerated when the Jupyter notebook is run.
- **note:** after generating `similarity.pkl` copy it to the same directory where app.py located.

## How It Works

1. **Data Collection**: Movie metadata is fetched from TMDB.
2. **Similarity Calculation**: A similarity matrix is created using cosine similarity between movies based on their features.
3. **Recommendation Generation**: The app finds the top 5 similar movies for a given input movie.
4. **Streamlit Interface**: Users interact with the model through an intuitive web app interface.

## Running the Project
