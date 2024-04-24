import streamlit as st
st.title('Amal Roshan')
st.header('Who Am I')
st.write("Iam a Passionate Junior Data Scientist Working in Vitez Software Pvt Ltd. I like to learn anything related to computer, and also i like programming and thats why i choose the best field of study in IT jobs and that is data science.I like to play football on my free times.")
st.button("HIRE ME",type='primary')
if st.button("CONTACT ME"):
    st.write("Here is my Number : 9778218181")
else:
    st.write("My Resume is on my Profile")
skills = st.header(st.selectbox('Iam Skilled In',('Pandas','Python','Machine Learning','SQL','PowerBi','Matplotlib','Statistics','Probability','Recommendation System','ML Algorithms','Deep Learning','NLP','AI Fundamentals','Web Scraping','Data Cleaning','EDA','Visualisations')))
