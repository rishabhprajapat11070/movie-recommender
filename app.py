import streamlit as st
import pandas as pd 
import pickle
import requests

def recommand(movies):
    indexs = movie_name[movie_name["title"]==movies].index[0]
    sim = simailar[indexs]
    sort = sorted(list(enumerate(sim)),reverse=True,key=lambda x:x[1])[1:6]
    
    recom = []
    for i in sort:
        recom.append(movie_name.iloc[i[0]].title)
    return recom   
    
         
simailar = pickle.load(open("similarty.pkl","rb"))
movies_list =pickle.load(open("movies_dict.pkl","rb")) 
st.title("MOVIES RECOMMENDATION")
movie_name = pd.DataFrame(movies_list)


my_movie = st.selectbox("select you favourite movies",movie_name["title"])

if st.button("Rcommand"):
    fetch = recommand(my_movie)
    for i in fetch:
        st.write(i)
        
