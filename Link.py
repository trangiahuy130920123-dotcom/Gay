import streamlit as st
import requests
from urllib.parse import urlparse

st.set_page_config(
    page_title="Link Checker",
    page_icon="🔗",
    layout="centered",
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {max-width: 680px; padding-top: 2rem;}
.title {text-align: center; font-size: 30px; font-weight: 800;}
.sub {text-align: center; opacity: .65; margin-bottom: 25px;}
.card {padding: 16px; border-radius: 16px; border: 1px solid rgba(128,128,128,.25); margin-top: 15px;}
.url {word-break: break-all;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔗 Link Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Kiểm tra redirect của URL</div>', unsafe_allow_html=True)

url = st.text_input("URL", placeholder="https://example.com/...", label_visibility="collapsed")

if st.button("🔎 Kiểm tra", use_container_width=True):
    if not url:
        st.warning("Nhập URL trước.")
        st.stop()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    if not parsed.netloc:
        st.error("URL không hợp lệ.")
        st.stop()

    try:
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X)"}
        with st.spinner("Đang kiểm tra..."):
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=12)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**Status:**", response.status_code)
        st.write("**Domain:**", parsed.netloc)
        st.write("**URL cuối:**")
        st.markdown(f'<div class="url">{response.url}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if response.history:
            st.subheader("↪️ Redirect")
            for i, item in enumerate(response.history, 1):
                location = item.headers.get("Location", "(không có)")
                st.write(f"{i}. `{item.status_code}` → `{location}`")
        else:
            st.info("Không có HTTP redirect công khai.")

    except requests.RequestException as e:
        st.error(f"Không thể truy cập URL: {e}")

st.caption("Chỉ kiểm tra redirect HTTP công khai; không vượt CAPTCHA, timer, token hoặc cơ chế bảo vệ.")
