import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    api_key = 'b3ce41f12b1e9f21b713a68f09e30167'  # Your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    data = requests.get(url).json()
    poster_path = data['poster_path']
    base_url = 'https://image.tmdb.org/t/p/original'
    full_path = base_url + poster_path
    return full_path
movies=pickle.load(open("movies_list.pkl", 'rb'))
similarity =pickle.load(open("similarity.pkl",'rb'))
movies_list=movies['title'].values
st.header('Movie Recomender System')
#create the dropdown to select the movie 
selected_movie=st.selectbox("Select a movie:", movies_list)
import streamlit.components.v1 as components
def recommend(movie):
    index=movies[movies['title'] == movie].index[0]
    distance=sorted (list(enumerate(similarity[index])),reverse=True, key=lambda vector: vector[1])
    recommend_movies=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.illoc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movies,recommend_poster
if st.button("Show recomendation"):
    movie_name,movies_poster =recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movies_poster[0])
    
    with col2:
        st.text(movie_name[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movies_poster[4])
    



