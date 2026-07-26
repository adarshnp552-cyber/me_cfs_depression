import streamlit as st

st.title("Scikit-learn Test")

try:
    import sklearn
    st.success(f"✅ Scikit-learn is installed! Version: {sklearn.__version__}")
except Exception as e:
    st.error("❌ Scikit-learn is NOT installed.")
    st.write(e)

st.stop()