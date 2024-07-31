import streamlit as st
#---page setup---
home_page = st.Page(
  page="views/Home.py",
  title="Home",
  icon="✔",
  default=True,
)
about_me_page = st.Page(
  page="About/About me.py",
  title="About Me",
  icon="✔",
)
gallery_page = st.Page(
  page="views/Gallery.py",
  title="  Gallery",
  icon="✔",
)
ptojet_1_page = st.Page(
  page="views/Projet_1.py",
  title="Projet_1",
  icon="✔",
)
contact_page = st.Page(
  page="views/Contact.py",
  title="Contact",
  icon="✔",
)
#---navigation setup---
pg =st.navigation(pages=[home_page,about_me_page,gallery_page,ptojet_1_page,contact_page])

#run navigation
pg.run()