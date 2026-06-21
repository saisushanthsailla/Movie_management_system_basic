import streamlit as st
import requests

st.set_page_config(
    page_title="Movie Explorer",
    page_icon="🎬",
    layout="wide"
)

st.title("Movie Explores & Review Management System")
st.write('''

Discover, explore, and review your favorite movies all in one place. Search through an extensive movie database, view ratings and details, read user reviews, and share your own opinions. Whether you're a casual viewer or a movie enthusiast, this platform helps you find great films and engage with the movie community.

🍿 View All Movies | ⭐ Search / Filter Movies| 📝 Add New Movie | 🎬 Update Movie | Delete Movie ''')


with st.sidebar :
    option = st.selectbox("Features",["View All Movies","Search / Filter Movies",'Add New Movie','Update Movie','Delete Movie'])
api_url = "http://127.0.0.1:8000"
if option == "View All Movies" :
    st.write("Do you want to view the Movies List")
    if st.button("List of Movies") :
        response = requests.get(f"{api_url}/Movies")
        movies = response.json()
        st.success("Movies Loaded Successfully")

        for movie in movies:

            st.write(f"🎬 {movie['movie_name']}")
            st.write(f"Genre: {movie['genre']}")
            st.write(f"Language: {movie['language']}")
            st.write(f"Rating: ⭐ {movie['rating']}")
            st.divider()

    

elif option == "Search / Filter Movies" :
    genre = st.selectbox("Genre",["Action","Sci-Fi","Comedy"])
    language = st.selectbox("Language",["English","Telugu","Hindi"])
    rating = st.slider("Rating",1,10,5)

    if st.button("Submit") :
        response = requests.get(f"{api_url}/filter",params={
            "genre": genre,
            "language": language,
            "rating": rating})
        df = response.json()
        st.write(df)

elif option == "Add New Movie" :
    movie_id = st.number_input("Enter movie id",min_value=1,step=1)
    movie_name = st.text_input("Enter Movie Name")
    genre = st.selectbox("Genre",["Action","Sci-Fi","Comedy"])
    language = st.selectbox("Language",["English","Telugu","Hindi"])
    rating = st.slider("Rating",1,10,5)
    if st.button("Add Movie"):
        new_movie_details = {
           "id" :  movie_id,
           "movie_name" : movie_name,
           "genre" : genre,
           "language" : language,
           "rating" : rating
        }
        response = requests.post(f"{api_url}/addmovie",json = new_movie_details)
        st.success(response.json()["message"])


elif option == "Update Movie" :
    movie_id = st.number_input(
        "Movie ID",
        min_value=1,
        step=1
    )

    movie_name = st.text_input("Movie Name")

    genre = st.selectbox(
        "Genre",
        ["Action", "Comedy", "Drama", "Sci-Fi"]
    )

    language = st.selectbox(
        "Language",
        ["English", "Hindi", "Telugu"]
    )

    rating = st.slider(
        "Rating",
        1,
        10,
        5
    )
    updated_information = {
        "id" : movie_id,
        "movie_name" : movie_name,
        "genre" : genre,
        "language" : language ,
        "rating" : rating,

    }
    if st.button("Update Information"):
        response = requests.put(f"{api_url}/updatemovie/{movie_id}",json = updated_information)
        message = response.json()
        st.success(response.json()["message"])



elif option == "Delete Movie" :
    movie_id = st.number_input(
        "Enter Movie ID",
        min_value=1,
        step=1
    )
    if st.button("Delete") :
        response = requests.delete(f"{api_url}/deletemovie/{movie_id}" )
        st.success(response.json()['message'])



