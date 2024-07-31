import streamlit as st  # pip install streamlit

#st.header(":mailbox: Get In Touch With Me!")
st.markdown(""" <h2 style='text-align:center;color:white;'>📭   Get In Touch With Me!</h2>""",unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/firdaladrif@gmail.com" method="POST">
     <br><br>
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <br><br>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        


local_css("views/style/style.css")
