import streamlit as st
import google.generativeai as genai

# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # 【ここが最重要！】api_versionを'v1'に固定して、古い道を通らんようにする
    genai.configure(api_key=API_KEY, transport='rest')
except:
    st.error("APIキーの設定を確認してや。")
    st.stop()

# --- 2. モデル設定 (名前をシンプルに) ---
# 最新の安定版なら 'models/' をつけずに呼ぶのが一番確実や
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. 画面のデザイン ---
st.title("💡 アイデア採点マシン")
user_idea = st.text_area("アイデアを入力してや：")

if st.button("AIに採点してもらう"):
    if user_idea:
        with st.spinner("最新のGoogle AI(v1)と通信中..."):
            try:
                # シンプルに実行
                response = model.generate_content(user_idea + " を採点して。")
                st.success("ついに行ったああああ！！")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"これでもダメか！生の声：{e}")
    else:
        st.warning("何か書いてや！")
