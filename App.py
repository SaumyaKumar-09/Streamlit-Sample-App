import streamlit as st

st.title("Title -> GeeksForGeeks")                                  # Title
st.header("Header -> GeeksForGeeks")                                # Header
st.subheader("Subheader -> GeeksForGeeks")                          # Sub Header
st.text("Text -> GeeksForGeeks")                                    # Text

st.markdown("# Hi")                                                 # Markdown
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")
st.markdown("##### Hi")
st.markdown("Hi")

st.success("Success!")                                              # Success
st.info("Information")                                              # Info
st.warning("Warning!")                                              # Warning
st.error("Error!")                                                  # Error

st.exception(ZeroDivisionError("Division by 0 not possible!"))       # Exception

st.help(ZeroDivisionError)                                          # Help - Defines the exception

st.write("range(1,10)")                                             # Write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.code('x = 10 \n'                                                 # Code
        'for i in range(x):'
        '\tprint(i)')

if (st.checkbox('Male')):                                           # CheckBox with Validation
    st.write("You're Male")
st.checkbox('Female')                                               # CheckBox
st.checkbox('Other')

radioButton = st.radio('Select : ', ('Male','Female','Other'))      # Radio Button

if (radioButton == 'Male'):
    st.write("You're a Male")
elif (radioButton == "Female"):
    st.write("You're a Female")
elif (radioButton == "Other"):
    st.write("You're an Other Gender")

st.subheader("Select Box")                                          # SelectBox                                    # SelectBox
selectBox = st.selectbox("Data Science : ", ["Data Analysis", "Web Scraping", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Image Processing"])
st.write("Yo've selected :",selectBox)

st.subheader("Multi Select Box")                                    # Multi Select Box
multiSelectBox = st.multiselect("Data Science : ", ["Data Analysis", "Web Scraping", "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision", "Image Processing"])
st.write("ou've selected :", len(multiSelectBox), "courses")

st.subheader("Button")                                              # Button
if (st.button("Click me")):
    st.write("Thanks for clicking!")

st.subheader("Slider")                                              # Slider
val = st.slider("Select the level", 1, 100, step = 1)
st.write("The voume is : ", val)

st.subheader("Text Input")                                          # Text Input
username = st.text_input("Username : ")
password = st.text_input("Password : ", type = 'password')

st.subheader("Text Area")                                          # Text Area
textarea = st.text_area("Write something about yourself ")

st.subheader("Input Number")                                          # Text Area
age = st.number_input("select your age : ", 10, 150)

st.subheader("Input Date")                                          # Text Area
date = st.date_input("Date")

st.subheader("Input Time")                                          # Text Area
time = st.time_input("Time")

