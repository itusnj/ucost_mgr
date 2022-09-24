#%% read data
%load_ext autoreload
%autoreload 2
from IPython.display import clear_output
from reader import factory
reader = factory()
clear_output()

# %% 年間の推移
reader.show_sum_denki_consume()
reader.show_sum_denki_sale()
reader.show_sum_suido()
# %%
