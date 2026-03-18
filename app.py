import streamlit as st
import google.generativeai as genai
import json

# --- 1. セキュリティ設定 ---
# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # ↓ここ！これに書き換えるんや！
    genai.configure(api_key=API_KEY, transport='rest')
except:
    st.error("APIキーが設定されてへんで！SettingsのSecretsを確認してや。")
    st.stop()

model = genai.GenerativeModel("models/gemini-1.5-flash")

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
            prompt = f"""
            以下のビジネスアイデアを「収益性」「実現性」「独創性」の3項目で0-100点で採点してください。
            必ず以下のJSON形式のみで出力し、余計な説明は一切省いてください。
            
            アイデア: {user_idea}

            出力形式:
            {{
              "収益性": {{"点数": 0, "理由": ""}},
              "独創性": {{"点数": 0, "理由": ""}},
              "実現性": {{"点数": 0, "理由": ""}}
            }}
            """
            
            try:
                response = model.generate_content(prompt)
                clean_text = response.text.replace("```json", "").replace("```", "").strip()
                score_data = json.loads(clean_text)

                st.success("採点完了や！")
                cols = st.columns(3)
                items = ["収益性", "独創性", "実現性"]
                for i, item in enumerate(items):
                    with cols[i]:
                        st.metric(label=item, value=f"{score_data[item]['点数']}点")
                        st.caption(score_data[item]['理由'])
                
                st.balloons()

            except Exception as e:
                st.error(f"エラーが発生したわ：{e}")
                st.info("もう一回試してみて！")
    else:
        st.warning("アイデアを入力せんと始まらんで！")
