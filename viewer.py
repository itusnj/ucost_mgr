#%%
# Display annual changes
from IPython.display import clear_output
from ipywidgets import interact
from reader import factory
reader = factory()

DENKI_CONSUME: str = "年間消費電力の推移"
DENKI_ELECGEN: str = "年間発電量(売電量)の推移"
DENKI_TIMEZONE: str = "時間帯毎の消費電力の推移"
SUIDO_CONSUME: str = "年間水道使用量の推移"

MODES = [DENKI_CONSUME, DENKI_ELECGEN, DENKI_TIMEZONE, SUIDO_CONSUME]

def show_annual_changes(mode: str):
    if mode == DENKI_CONSUME:
        reader.show_sum_denki_consume()
    elif mode == DENKI_ELECGEN:
        reader.show_sum_denki_sale()
    elif mode == DENKI_TIMEZONE:
        reader.show_timezone_denki()
    elif mode == SUIDO_CONSUME:
        reader.show_sum_suido()

interact(
    show_annual_changes,
    mode=MODES
)

# %%
