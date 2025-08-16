import os
import pandas as pd

def load_data_imdb(filepath_imdb):
    
    data_imdb = pd.read_csv(filepath_imdb)

    return data_imdb

def load_data_20newsgroups(filepath_20newsgroups):
    
    rows = []

    for newsgroup in os.listdir(filepath_20newsgroups):

        newsgroup_path = os.path.join(filepath_20newsgroups, newsgroup)

        print(f"{newsgroup}")
        print(f"{newsgroup_path}")

        if os.path.isdir(newsgroup_path):

            for file_name in os.listdir(newsgroup_path):

                document_id = os.path.splitext(file_name)[0]
                rows.append({'newsgroup': newsgroup, 'document_id': document_id})
                    
    data_20newsgroups = pd.DataFrame(rows)
    data_20newsgroups.to_csv('../data/raw/20_newsgroup/list.csv', index=False)

    print(data_20newsgroups.head())

    return data_20newsgroups