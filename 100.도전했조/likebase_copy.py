import numpy as np
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

def search_songs(key_title, key_artist, app):
    filename = os.path.join(app.static_folder, 'data/melon_song_v2.csv')
    df = pd.read_csv(filename)
    df.songId = df.songId.astype(str)
    songIds =  df[df.title.str.lower().str.contains(key_title.lower()) & df.artist.str.lower().str.contains(key_artist.lower())][['songId', 'title', 'artist', 'album', 'date', 'img']].to_dict('records')
    return songIds

def propose(find_songId, app):
    def get_recommendation(songId, cos_sim):
        index = indices[songId]
        sim_scores = pd.Series(cos_sim[index])
        song_indices = sim_scores.sort_values(ascending=False).head(31).tail(30).index
        return df.songId.iloc[song_indices]

    filename = os.path.join(app.static_folder, 'data/melon_song_v2.csv')
    plist_filename1 = os.path.join(app.static_folder, 'data/melon_playlist1.csv')
    plist_filename2 = os.path.join(app.static_folder, 'data/melon_playlist2_v2.csv')


    df = pd.read_csv(filename)
    plist1 = pd.read_csv(plist_filename1)
    plist2 = pd.read_csv(plist_filename2)

    plist1.plylstSeq = plist1.plylstSeq.astype(str)
    plist2.songId = plist2.songId.astype(str)

    df.date.fillna(0, inplace=True)
    df['date'] = df.date.astype(int).astype(str)
    df.fillna('', inplace=True)
    df['comment_like_total'] = df.comment + df.like
    df['songId'] = df.songId.astype(str)
    df.lyric = df.lyric.str.replace('\r', '')    

    indices = pd.Series(df.index, index=df.songId)

    tvect = TfidfVectorizer(stop_words='english')
    total_tv = tvect.fit_transform(df.total)
    cosine_sim = cosine_similarity(total_tv)

    a = get_recommendation(find_songId, cosine_sim).to_frame()

    numbers = df['comment_like_total']
    sorted_numbers = np.sort(numbers)
    q1 = np.percentile(sorted_numbers, 25)
    q2 = np.percentile(sorted_numbers, 50)
    filtered_data = df[(df['comment_like_total'] >= q1) & (df['comment_like_total'] < q2)]
    filtered_data = filtered_data[['songId', 'comment_like_total']]

    d = a[a['songId'].isin(filtered_data.songId.values)].head(5)
    pro_meong = df[df['songId'].isin(d.songId.values[:5])][['songId', 'title', 'artist', 'genre', 'album', 'lyricist', 'composer']].to_dict('records')


    tags = np.unique(' '.join(plist1[plist1.songIds.str.contains(find_songId)]['tag'].values).split(), return_counts=True)
    df_tags = pd.DataFrame({'tag' : tags[0], 'count' : tags[1]})
    pro_tags = ' '.join(df_tags.sort_values('count', ascending=False).head(2)['tag'])

    songs = np.unique(' '.join(plist1[plist1.songIds.str.contains(find_songId)]['songIds'].values).replace(find_songId, '').split(), return_counts=True)
    df_songs = pd.DataFrame({'songId' : songs[0], 'count' : songs[1]})
    song_list = df_songs.sort_values('count', ascending=False).head(5)['songId'].values


    pro_psongs = df[df.songId.isin(song_list)][['songId', 'title', 'artist', 'genre', 'album', 'lyricist', 'composer']]

    if pro_psongs.empty:
        pro_psongs = plist2[plist2.songId.isin(song_list)]

    pro_psongs = pro_psongs.to_dict('records')
    return pro_tags, pro_meong, pro_psongs
# pro_tags 태그
# pro_contents 컨테츠 기반 추천
# pro_meong 명곡
# pro_psongs propose_play_list 기반추천