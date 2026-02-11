
import streamlit as st
import pandas as pd
import json
from scraper import fetch_headlines
from sources import SOURCES

st.set_page_config(page_title="News Headline Scraper", layout="wide")

st.title("📰 News Headline Scraper")
st.write("Scrape latest headlines from multiple news sources")

sources_selected = st.multiselect(
    "Select news sources",
    options=list(SOURCES.keys()),
    default=list(SOURCES.keys())
)

keyword = st.text_input("Filter by keyword (optional)")

if st.button("🔍 Fetch Headlines"):
    all_headlines = []

    with st.spinner("Scraping headlines..."):
        for source in sources_selected:
            all_headlines.extend(fetch_headlines(source, keyword))

    if all_headlines:
        df = pd.DataFrame(all_headlines)
        st.success(f"Fetched {len(df)} headlines")
        st.dataframe(df, use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download CSV",
            csv,
            "headlines.csv",
            "text/csv"
        )

        # Download JSON
        json_data = json.dumps(all_headlines, indent=2).encode("utf-8")
        st.download_button(
            "⬇️ Download JSON",
            json_data,
            "headlines.json",
            "application/json"
        )
    else:
        st.warning("No headlines found")
