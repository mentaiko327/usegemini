import streamlit as st
import google.generativeai as genai

# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY, transport='rest')
except:
    st.error("APIキーの設定を確認してや。")
    st.stop()

# --- 2. モデル設定 (名前をあえてシンプルにする) ---
model = genai.GenerativeModel("gemini-1.5-flash")

# --- 3. 画面のデザイン ---
st.title("💡 アイデア採点マシン")
user_idea = st.text_area("アイデアを入力してや：", placeholder="例：AI土地解析アプリ")

if st.button("AIに採点してもらう"):
    if user_idea:
        with st.spinner("AIが考え中..."):
            try:
                # ここで余計な設定をせず、シンプルに投げる！
                response = model.generate_content(user_idea + " を「収益性」「独創性」「実現性」で採点して。")
                st.success("成功や！結果を見てや！")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # もしエラーが出ても、内容を詳しく出すようにしたで
                st.error(f"またエラーか！内容はこれや：{e}")
    else:
        st.warning("何か書いてくれへんと採点できへんで！")
