import streamlit as st
import google.generativeai as genai

# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # configureの中で transport='rest' を指定するのが今の正解や
    genai.configure(api_key=API_KEY, transport='rest')
except:
    st.error("APIキーの設定を確認してや。")
    st.stop()

# --- 2. モデル設定 ---
# 最新版なら 'models/' をつけず、シンプルにこう書く
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. 画面 ---
st.title("💡 アイデア採点マシン")
user_idea = st.text_area("アイデアを入力してや：")

if st.button("AIに採点してもらう"):
    if user_idea:
        with st.spinner("Googleの最新サーバーに接続中..."):
            try:
                # 実行！
                response = model.generate_content(user_idea)
                st.success("ついに行ったあああ！！！")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # もしこれでも v1beta が出たら、Google側の気まぐれや
                st.error(f"これでもダメか！ 生の声：{e}")
    else:
        st.warning("何か書いてや！")
