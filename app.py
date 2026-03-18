import streamlit as st
import google.generativeai as genai
import json

# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # 【ここが最重要！】古い道(v1beta)じゃなくて、今の標準の道を通るように指定したで
    genai.configure(api_key=API_KEY)
except:
    st.error("APIキーが設定されてへんで！SettingsのSecretsを確認してや。")
    st.stop()

# --- 2. モデル設定 ---
# model_name の指定を、一番エラーが出にくいこれに変えるで
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# --- 3. 画面のデザイン ---
st.set_page_config(page_title="Idea Evaluator", page_icon="💡")
st.title("💡 アイデア採点マシン (100点満点版)")
st.write("あなたのビジネスアイデアをAIがガチで評価するで。")

# 入力欄
user_idea = st.text_area("アイデアを詳しく入力してや：", height=200, placeholder="例：余ったクッキーとコーヒーをセットで売るアプリ")

# 実行ボタン
if st.button("AIに採点してもらう", type="primary"):
    if user_idea:
        with st.spinner("Gemini AIが考え中や。ちょっと待ってな..."):
            prompt = f"以下のアイデアを収益性、実現性、独創性の3項目で採点してJSONで出して：{user_idea}"
            
            try:
                # 【ここも重要！】古いバージョンを指定せず、最新版で動かす書き方や
                response = model.generate_content(prompt)
                
                # AIの返答を表示するで
                st.success("採点完了や！")
                st.write(response.text)
                st.balloons()

            except Exception as e:
                st.error(f"エラーが発生したわ：{e}")
    else:
        st.warning("アイデアを入力せんと始まらんで！")
