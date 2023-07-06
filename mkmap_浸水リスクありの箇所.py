import folium
import pandas as pd

# CSVファイルのパス
csv_path = 'input/input.csv'

# CSVファイルの読み込み
data = pd.read_csv(csv_path, encoding="SHIFT_JIS")

# 地図の初期設定
map = folium.Map()

# CSVデータの行数分ループ
for index, row in data.iterrows():
    # 緯度経度の取得
    lat = row[0]
    lng = row[1]

    # その他情報の取得（ヘッダーから取得）
    #info = f"<b>{data.columns[2]}:</b> {row[2]}<br>"  # 3列目の情報を取得
    info = ""
    for column in data.columns[2:]:
        info += f"<b>{column}:</b> {row[column]}<br>"

    # マーカーの作成
    marker_color = 'red' if row['河川氾濫'] == 'リスクあり' else 'blue'
    marker = folium.Marker(
        location=[lat, lng],
        popup=folium.Popup(info, max_width=300),  # マーカーをクリックしたときに表示する情報を設定
        icon=folium.Icon(color=marker_color)  # マーカーの色を設定
    )
    # マーカーを地図に追加
    marker.add_to(map)

# 地図をHTMLファイルとして保存
map.save('output/map_浸水リスクあり地点(赤).html')
