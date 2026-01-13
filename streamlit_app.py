import streamlit as st

st.title("カスタマイズしたアプリ")

# テキスト入力ボックス
name = st.text_input("お名前を入力してください")

# ボタン
if st.button("挨拶する"):
    st.write(f"こんにちは、{name}さん！Streamlitへようこそ。")

# スライダー
level = st.slider("今の気分は？", 0, 100, 50)
st.write(f"現在の気分レベル: {level}")