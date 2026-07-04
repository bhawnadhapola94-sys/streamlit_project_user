import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="RFM Analysis", layout="wide")

st.title(" RFM Customer Segmentation")

df = pd.read_csv("online_retail_small.csv")


df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


df = df.dropna(subset=["CustomerID"])

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.write("Dataset Loaded Successfully ")
st.dataframe(df.head())

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)


rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Sales": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

st.success("RFM Table Created Successfully")
st.markdown("---")
st.subheader(" RFM Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Customers", rfm.shape[0])
c2.metric("Average Recency", round(rfm["Recency"].mean(), 1))
c3.metric("Average Frequency", round(rfm["Frequency"].mean(), 1))
c4.metric("Average Monetary", round(rfm["Monetary"].mean(), 2))
st.dataframe(rfm.head())
# RFM Scores
rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

st.subheader("RFM Scores")

st.dataframe(rfm.head())
st.subheader(" Recency Distribution")

fig1 = px.histogram(
    rfm,
    x="Recency",
    nbins=30,
    title="Recency Distribution"
)

st.plotly_chart(fig1, use_container_width=True)
st.subheader("Frequency Distribution")

fig2 = px.histogram(
    rfm,
    x="Frequency",
    nbins=30,
    title="Frequency Distribution"
)

st.plotly_chart(fig2, use_container_width=True)
st.subheader("Monetary Distribution")

fig3 = px.histogram(
    rfm,
    x="Monetary",
    nbins=30,
    title="Monetary Distribution"
)

st.plotly_chart(fig3, use_container_width=True)