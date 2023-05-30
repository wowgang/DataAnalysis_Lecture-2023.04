import numpy as np
import pandas as pd


df = pd.read_csv('data/melon_song.csv')
df.fillna('', inplace=True)
df['comment_like_total'] = df.comment + df.like
df['songId'] = df.songId.astype(str)
df['total'] = df.lyric + (' ' + df.title) + (' ' + df.artist) * 2 + (' ' + df.composer) * 2 + (' ' + df.lyricist) * 2 + (' ' + df.genre) * 2
df.set_index('songId', inplace=True)
df.reset_index(inplace=True)


from sklearn.feature_extraction.text import TfidfVectorizer
tvect = TfidfVectorizer()
total_tv = tvect.fit_transform(df.total)
indices = pd.Series(df.index, index=df.songId)


from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(total_tv)


def get_recommendation(songId, cos_sim):
    index = indices[songId]
    sim_scores = pd.Series(cos_sim[index])
    song_indices = sim_scores.sort_values(ascending=False).head(30).index
    return df.songId.iloc[song_indices]


sorted_numbers = np.sort(df['comment_like_total'])
q1 = np.percentile(sorted_numbers, 25)
q2 = np.percentile(sorted_numbers, 50)
filtered_data = df[(df['comment_like_total'] >= q1) & (df['comment_like_total'] < q2)]


a = get_recommendation('35609035', cosine_sim)
b = [i for i in a.values if i in filtered_data.songId.values]
filtered = df[df['songId'].isin(b[:5])].to_dict()