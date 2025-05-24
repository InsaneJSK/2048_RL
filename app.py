# app.py
import streamlit as st
import numpy as np
from engine import Game2048          # your logic file
from app_funcs import get_tile_style
import streamlit.components.v1 as components


# ------------- Streamlit page config -------------
st.set_page_config(page_title="2048 Game", page_icon="🎮", layout="centered")

st.title("🎮 2048 Game")

# ------------- Create or load game object -------------
if "game" not in st.session_state:
    st.session_state.game = Game2048()

game = st.session_state.game          # shorthand

if "counter" not in st.session_state:
    st.session_state.counter = 0


def read_index_html(copy_text: int):
    with open("index.html") as f:
        return f.read().replace("python_string", f'"Counter value is {copy_text}"')

def restart():
    st.session_state.game = Game2048()

def left_step():
    game.step(0)

def down_step():
    game.step(1)

def right_step():
    game.step(2)

def up_step():
    game.step(3)

# ------------- Control buttons -------------
moved = False
left, right, up, down, reset = st.columns(5)

left.button("⬅️ Left", on_click=left_step)
right.button("➡️ Right", on_click=right_step)
up.button("⬆️ Up", on_click=up_step)
down.button("⬇️ Down", on_click=down_step)
reset.button("🔄 Reset", on_click=restart)



# ------------- Read state from engine -------------
board     = game.board
score     = int(game.score)
game_over = game.gameover
game_won  = np.any(board == 2048)

# ------------- Score & status display -------------
st.metric("Score", score)


# Most important part to hack in JS
components.html(
    read_index_html(st.session_state.game),
    height=0,
    width=0,
)

if game_over:
    st.error("😢 Game Over!")
elif game_won:
    st.success("🎉 You reached 2048!")

# ------------- Board rendering -------------
st.markdown("### Game Board")
for row in board:
    cols = st.columns(4)
    for i, val in enumerate(row):
        tile_val = f"{int(val)}" if val != 0 else ""
        cols[i].markdown(
            f"<div style='{get_tile_style(int(val))}'>{tile_val}</div>",
            unsafe_allow_html=True
        )

# ------------- Sidebar placeholders -------------
st.sidebar.title("🛠️ Game Settings")
st.sidebar.radio("Mode", ["Manual", "Auto-play AI (Coming Soon)"])

st.markdown("---")
st.caption("Made by Jaspreet Singh · [GitHub](https://github.com/InsaneJSK/2048_RL)")

