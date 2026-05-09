import streamlit as st

# <img src='https://i.ibb.co/YTYGn5qv/logo.png' />

def main():
    st.header("This is title")
    name = st.text_input("enter your name")

    # col1, col2 = st.columns(2, gap="small")
    # col1, col2 = st.columns(2, gap="xlarge")
    col1, col2 = st.columns(2, gap="xsmall")
    with col1:
        if st.button("Hi", type="primary", key="btn1", width="stretch"):
            print("hi", name)
    
    with col2:    
        if st.button("Bye", type="secondary", key="btn2", width="stretch"):
            print("bye", name)
    
    st.markdown("""
        <div>
                <img src='https://tse3.mm.bing.net/th/id/OIP.XVImQ-QaDyrK1haLcRldVwHaHa?pid=ImgDet&w=184&h=184&c=7&o=7&rm=3' />
                <h1> Snap Class </h1>
        </div>
        <style>
                button {
                    background : orange !important;
                }
        </style>
    """, unsafe_allow_html=True)

main()