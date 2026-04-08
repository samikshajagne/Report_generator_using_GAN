import streamlit as st
import pandas as pd
from report_generator import generate_report

st.set_page_config(page_title="AI Report Generator", layout="wide")

st.title("📊 AI-Powered Report Generator")
st.write("Upload your dataset and generate AI-based insights instantly!")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df)

    if st.button("Generate Report"):
        with st.spinner("Generating report..."):
            report = generate_report(df)

        st.subheader("📄 Generated Report")
        st.write(report)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="report.txt",
            mime="text/plain"
        )