import streamlit as st
import pickle
import pandas as pd

mv_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pd.DataFrame(mv_dict)


def recommend_mv(movie):
    mv_index = movies[movies["title"] == movie].index[0]
    distances = similarity[mv_index]
    mv_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recm_movies = []
    for mv in mv_list:
        recm_movies.append(movies.iloc[mv[0]].title)
    return recm_movies


st.title("Movies Recommendation")
selected_movie_name = st.selectbox(
    label="Select Movies",
    options=movies["title"].values,
    index=0,
)

if st.button("Recommend"):
    recm_movies = recommend_mv(selected_movie_name)
    for mv in recm_movies:
        st.write(mv)
