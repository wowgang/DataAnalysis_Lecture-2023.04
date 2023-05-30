import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data/melon_song.csv')
df['songId'] = df.songId.astype(str)
df.fillna('', inplace=True)
df['total'] = df.lyric + (' ' + df.artist) * 2 + (' ' + df.composer) * 2 + (' ' + df.lyricist) * 2 + (' ' + df.genre) * 2 + (' ' + df.title)
df.set_index('songId', inplace=True)
df.reset_index(inplace=True)

tvect = TfidfVectorizer()
total_tv = tvect.fit_transform(df.total)
indices = pd.Series(df.index, index=df.songId)

cosine_sim = cosine_similarity(total_tv)

def get_recommendation(songId, cos_sim):
    index = indices[songId]
    sim_scores = pd.Series(cos_sim[index])
    song_indices = sim_scores.sort_values(ascending=False).head(6).tail(5).index
    return df.songId.iloc[song_indices]

a = get_recommendation('35609035', cosine_sim)
df[df['songId'].isin(a)]
filtered_df = df[df['songId'].isin(a)]
filtered_df.to_dict()