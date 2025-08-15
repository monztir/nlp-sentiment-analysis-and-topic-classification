import pandas as pd

def load_data_imdb(filepath_imdb):
    
    data_imdb = pd.read_csv(filepath_imdb)

    return data_imdb

def load_data_20newsgroups(filepath_20newsgroups):
    
    data_20newsgroups = pd.read_csv(filepath_20newsgroups)

    return data_20newsgroups