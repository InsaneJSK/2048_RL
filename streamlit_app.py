import streamlit as st
import streamlit.components.v1 as components

def lol():
    pass

if "counter" not in st.session_state:
    st.session_state.counter = 0


def read_index_html(copy_text: int):
    with open("index.html") as f:
        return f.read().replace("python_string", f'"Counter value is {copy_text}"')

st.title("Hacking Streamlit Frontend")
st.caption(
    "Press left / right arrow keys to simulate decrement / increment button click"
)

left, right, up, down, reset = st.columns([1, 1, 1, 1, 3])

left.button("Left", on_click=lol)
right.button("Right", on_click=lol)
up.button("Up", on_click=lol)
down.button("Down", on_click=lol)
reset.button("Reset", on_click=lol)

st.metric("Counter", st.session_state.counter)

components.html(
    read_index_html(st.session_state.counter),
    height=0,
    width=0,
)