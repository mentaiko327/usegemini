import streamlit as st
import google.generativeai as genai
import traceback

# --- 1. セキュリティ設定 ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    # 【極限設定】通信の中身を全部さらけ出す設定や
    genai.configure(api_key=API_KEY, transport='rest')
except Exception as e:
    st.error(f"【設定ミス】APIキーが読み込めてへんで：{e}")
    st.stop()

# --- 2. モデル設定 ---
# あえてフルネームで指定する
model_name = "models/gemini-1.5-flash"
model = genai.GenerativeModel(model_name=model_name)

# --- 3. 画面 ---
st.title("💡 極限解析モード・採点マシン")
user_idea = st.text_area("アイデアを入力してや：")

if st.button("AIを解析・実行する"):
    if user_idea:
        with st.spinner("Googleのサーバーと格闘中..."):
            try:
                # 実行！
                response = model.generate_content(user_idea)
                st.success("ついに行ったで！！")
                st.write(response.text)
                st.balloons()
            
            except Exception as e:
                # 【ここが極限！】エラーの正体を徹底的にバラす
                st.error("🚨 門番（Google）に止められたで！")
                
                # エラーの種類
                st.warning(f"🚩 エラーの型: {type(e).__name__}")
                
                # 生のメッセージ
                st.code(f"生の声: {str(e)}", language="text")
                
                # 詳細な場所
                with st.expander("もっと詳しく（エンジニア用）"):
                    st.code(traceback.format_exc())
                    
                st.info("この上の『生の声』と『エラーの型』を俺に見せてくれ！")
    else:
        st.warning("アイデアを入れてな！")
