import pandas as pd
import numpy as np
import os, re, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search_songs(key_title, key_artist, app):
    filename = os.path.join(app.static_folder, 'data/melon_song_v2.csv')
    df = pd.read_csv(filename)
    df.songId = df.songId.astype(str)
    key_title = re.sub('['+string.punctuation+']', '', key_title)
    key_artist = re.sub('['+string.punctuation+']', '', key_artist)
    songIds = df[df.title.str.replace('['+string.punctuation+']', '', regex=True).str.contains(key_title, case=False)
                 &df.artist.str.replace('['+string.punctuation+']', '', regex=True).str.contains(key_artist, case=False)][]




























# 컨텐츠기반
df = pd.read_csv('data/melon_song_v2.csv')
df.date.fillna(0, inplace=True)
df.date = df.date.astype(int).astype(str)
df.songId = df.songId.astype(str)
df.fillna('', inplace=True)


df['total'] = df.morphs + (' ' + df.title) + (' ' + df.artist) * 2 + (' ' + df.composer) * 2 + (' ' + df.lyricist) * 2 + (' ' + df.genre) * 3

df.set_index('songId', inplace=True)
df.reset_index(inplace=True)
tvect = TfidfVectorizer(stop_words='english')
total_tv = tvect.fit_transform(df.total)
indices = pd.Series(df.index, index=df.songId)
cosine_sim = cosine_similarity(total_tv)



def get_recommendation(songId, cos_sim):
    index = indices[songId]
    sim_scores = pd.Series(cos_sim[index])
    song_indices = sim_scores.sort_values(ascending=False).head(6).tail(5).index
    df.songId.iloc[song_indices]

    def aaa(ssongId, cosine_sim2):
        a = get_recommendation(ssongId, cosine_sim2)
        filtered_df = df[df['songId'].isin(a)].to_dict('records')
        return filtered_df
