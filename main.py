import eel
import pandas as pd
import numpy as np
from sklearn import preprocessing

# 要変更
df = pd.read_csv("mobile_price.csv")

# 正規化ツール
mm = preprocessing.MinMaxScaler()
min_max = mm.fit_transform(df.values.tolist())

# 正規化済み Pandas データ
df_normalized = pd.DataFrame(min_max, columns=df.columns)
# 正規化してないもとのデータで上書き
df_normalized["price_range"] = df["price_range"] # 要変更

columns = list(df_normalized.columns) # カラム名のリスト
print(columns)

@eel.expose
def py_get_data(column_name):
    # pandas データフレームから必要な列データをリストで渡す
    return df_normalized[column_name].values.tolist()

@eel.expose
def py_get_columns():
    # pandas データフレームから列名をリストで渡す
    return columns


"""
アプリ起動オプション(サーバーを立ててブラウザでアクセスしている)
"""
web_app_options = {
    # "mode": "chrome-app",  # chromeのアプリケーションモードで起動
                           # "chrome" とすると、通常のchromeで起動
    "port": 8080,
    "chromeFlags": [
            # "--start-fullscreen",  # フルスクリーンで起動 他のChromeが起動していると機能しない？
            "--window-size=800,100",
            # "--window-position=0,0",
    ]
}


eel.init("web")
eel.start("main.html", options=web_app_options)