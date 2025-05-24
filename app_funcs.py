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
