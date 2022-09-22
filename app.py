import streamlit as st


@st.experimental_memo(persist="disk")
def my_func(x, y):
    result = st.slider("INSIDE MEMOIZED FUNC", x, y)
    st.write(result**2)
    print("INSIDE MEMOIZED FUNCTION!!!!")


my_func(5, 42)
print("OUTSIDE MEMOIZED FUNCTION")
