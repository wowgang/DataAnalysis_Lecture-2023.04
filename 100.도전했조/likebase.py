import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

# 좋아요/댓글 기반
df = pd.read_csv('data/melon_song_v2.csv')
df.date.fillna(0, inplace=True) 
df['date'] = df.date.astype(int).astype(str) 
df.fillna('', inplace=True)
df['comment_like_total'] = df.comment + df.like
df['songId'] = df.songId.astype(str)

songIds = df[df.title.str.contains(title) & df.artist.str.contains(artist)]

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
    song_indices = sim_scores.sort_values(ascending=False).head(31).tail(30).index
    return df.songId.iloc[song_indices]

def aaa(songId, cosine_sim):
    a = get_recommendation(songId, cosine_sim).to_frame()
    cosine_sim_total = linear_kernel(total_tv, total_tv)
    sim_scores = pd.Series(cosine_sim_total[indices[songId]])
    sim_scores.sort_values(ascending=False).head(11).tail(10)

    numbers = df['comment_like_total']
    sorted_numbers = np.sort(numbers)
    q1 = np.percentile(sorted_numbers, 25)
    q2 = np.percentile(sorted_numbers, 50)
    filtered_data = df[(df['comment_like_total'] >= q1) & (df['comment_like_total'] < q2)]
    filtered_data = filtered_data[['songId', 'comment_like_total']]
    filtered_data.songId.values
    filtered_df = df[df['songId'].isin(a.songId.values[:5])].to_dict('records')
    return filtered_df



