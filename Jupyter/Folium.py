# %%
import folium

# %%
m = folium.Map(location=[37.547631, 126.942463], zoom_start=15)
m

# %%
m = folium.Map(location=[37.531926334244034, 126.91421892157778], zoom_start=15,
                width=800, height=600)
m

# %%
folium.Marker([37.531926334244034, 126.91421892157778], popup='팝업', tooltip='툴팁').add_to(m)
m

# %%
folium.Marker([37.531926334244034, 126.91421892157778], popup='팝업', tooltip='툴팁',
                icon=folium.Icon(color='black', icon="fa-solid fa-folder", prefix='fa-solid')).add_to(m)
m

# %%
m.add_child(folium.ClickForMarker(popup='클릭'))
m

# %%
m.add_child(folium.LatLngPopup())

# %%
folium.CircleMarker([37.531926334244034, 126.91421892157778],
                    radius=100,
                    color='#ff0000',
                    fill_color='#00ff00',
                    popup='CircleMarker').add_to(m)
folium.Circle([37.531926334244034, 126.91421892157778],
                    radius=90,
                    color='#0000ff',
                    fill_color='#ffffff',
                    popup='Circle').add_to(m)
m

# %%
import pandas as pd
data= pd.read_csv("택시승차대 현황.csv", encoding='cp949')
taxi = data.loc[:, ["위치명", "위도", "경도"]]
taxi

# %%
for index, row in taxi.iterrows():
    folium.Marker([row['위도'], row['경도']], popup=row['위치명'],
                icon=folium.Icon(color='red', icon="fa-solid fa-taxi", prefix='fa-solid')).add_to(m)

m


