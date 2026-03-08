import streamlit as st

st.set_page_config(page_title="Özel Bir Soru", page_icon="🌹")
st.title("Küçük Bir Soru... 🤔")

cevap = st.text_input("Bugün günlerden ne?", placeholder="Buraya yaz...")

if st.button("Kontrol Et"):
    if cevap.lower().strip() == "dünya kadınlar günü":
        st.balloons()
        st.success("Dünyanın en güzel kadınının dünya kadınlar günü kutlu olsunnnnnn")
    else:
        st.error("Maalesef yanlış... Bir daha dene! ❌")
