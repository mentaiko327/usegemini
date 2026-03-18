import streamlit as st
import google.generativeai as genai
import os

# --- 1. 極限のセキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # 【ここが究極の裏技】
    # ライブラリの内部設定を上書きして、強制的に v1 (最新版) に向かわせる！
    os.environ["GOOGLE_API_VERSION"] = "v1" 
    genai.configure(api_key=API_KEY, transport='rest')
except:
    st.error("APIキーの設定を確認してや。")
    st.stop()

# --- 2. モデル設定 (名前の前に models/ をつけるのが今の流行り) ---
model = genai.GenerativeModel('models/gemini-1.5-flash')

# --- 3. 画面 ---
st.title("💡 アイデア採点マシン")
user_idea = st.text_area("アイデアを入力してや：", value="上がりそうな土地を解析、解説するアプリ。")

if st.button("AIに採点してもらう"):
    if user_idea:
        with st.spinner("Googleの壁を突破中..."):
            try:
                # 実行！
                response = model.generate_content(user_idea)
                st.success("ついに行ったあああ！！！")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # エラーが出ても、絶対に諦めへんからな
                st.error(f"生の声：{e}")
    else:
        st.warning("何か書いてや！")
