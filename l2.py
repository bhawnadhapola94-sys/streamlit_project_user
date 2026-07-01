import streamlit as st
import pandas as pd
st.set_page_config(page_title="Shopper Spectrum",page_icon="🛒", layout="wide")
# Load Dataset
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\bhawna python\market_data\online_retail_data.csv")
# Convert Date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
# Sales Column
df["Sales"] = df["Quantity"] * df["UnitPrice"]
# ---------------- HOME PAGE ----------------
st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation & Product Recommendation System")
st.markdown("---")
col1, col2 = st.columns(2)
with col1:st.info("""Business Problem Retail businesses generate huge amounts of sales data but often struggle to understand customer purchasing behaviour.Without customer segmentation they cannot:- Identify loyal customers
- Reduce customer churn
- Increase sales
- Improve marketing strategies
""")
with col1:
    st.info("""
### Business Problem
Retail businesses generate huge amounts of sales data but often struggle to understand customer behavior.

- Reduce customer churn
- Increase sales
- Improve marketing strategies
""")
st.markdown("---")
st.subheader("📊 Dataset Overview")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Customers", df["CustomerID"].nunique())
c4.metric("Countries", df["Country"].nunique())
st.markdown("---")
st.write("### Preview Dataset")
st.dataframe(df.head())
