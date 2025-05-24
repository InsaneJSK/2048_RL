import streamlit as st
import streamlit.components.v1 as components

def keyboard_arrow_listener(key_state_name="arrow_key"):
    # This HTML+JS injects a listener for arrow keys and updates a Streamlit text_input
    # via a small hack: a visible text_input where user focuses and presses arrows.
    # We make the input visually tiny & unobtrusive.
    
    components.html(
        """
        <input id="key_input" style="opacity:0; position:absolute; top:-1000px;" autofocus>
        <script>
        const input = document.getElementById("key_input");
        input.focus();
        input.addEventListener("keydown", (event) => {
            if (["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].includes(event.key)) {
                event.preventDefault();
                // Send key to Streamlit via updating the input value and firing change
                input.value = event.key;
                input.dispatchEvent(new Event('change'));
            }
        });
        </script>
        """,
        height=0,
        width=0,
        scrolling=False,
    )
    
    # Create the Streamlit input box that will sync with the above HTML input
    val = st.text_input("##", key=key_state_name)
    return val

# def arrow_key_listener():
#     js_code = """
#     <script>
#     const sendKey = (key) => {
#         const input = window.parent.document.querySelector('input[data-key="arrow_key_input"]');
#         if (input) {
#             input.value = key;
#             input.dispatchEvent(new Event('change'));
#         }
#     };

#     document.addEventListener('keydown', function(event) {
#         if(['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
#             event.preventDefault();
#             sendKey(event.key);
#         }
#     });
#     </script>
#     """

#     # Create a hidden input box to store the keypresses
#     components.html(js_code + """
#     <input type="text" style="opacity:0; height:0; position:absolute; top:-1000px;" data-key="arrow_key_input" />
#     """, height=0, width=0)


def get_tile_style(value: int) -> str:
    """Return an inline‑CSS style string for a 2048 tile."""
    colors = {
        0:    "#ccc0b3",
        2:    "#eee4da",
        4:    "#ede0c8",
        8:    "#f2b179",
        16:   "#f59563",
        32:   "#f67c5f",
        64:   "#f65e3b",
        128:  "#edcf72",
        256:  "#edcc61",
        512:  "#edc850",
        1024: "#edc53f",
        2048: "#edc22e",
    }
    bg = colors.get(value, "#3c3a32")          # fall‑back for 4096, 8192, …
    txt = "#776e65" if value <= 4 else "#f9f6f2"

    return (
        f"background-color:{bg};"
        f"color:{txt};"
        "font-size:30px;"
        "font-weight:bold;"
        "text-align:center;"
        "border-radius:10px;"
        "padding:25px 0;"
        "height:80px;"
        "margin-bottom:10px;"   # vertical gap between rows
        "box-shadow:2px 2px 5px rgba(0,0,0,0.2);"
    )
