import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title(" Customer Segmentation")

df = pd.read_csv("online_retail_small.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df.dropna(subset=["CustomerID"])
df["Sales"] = df["Quantity"] * df["UnitPrice"]

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Sales": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
st.subheader("RFM Table")
st.dataframe(rfm.head())

rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

st.subheader(" RFM Scores")

st.dataframe(
    rfm[["CustomerID","Recency","Frequency","Monetary",
         "R_Score","F_Score","M_Score"]].head()
)
def segment_customer(row):

    r = int(row["R_Score"])
    f = int(row["F_Score"])

    if r >= 4 and f >= 4:
        return " Champions"

    elif r >= 3 and f >= 3:
        return " Loyal Customers"

    elif r >= 4:
        return " Potential Loyalists"

    elif r <= 2 and f >= 3:
        return " At Risk"

    elif r <= 2 and f <= 2:
        return "Lost Customers"

    else:
        return " Others"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

st.subheader("Customer Segment Distribution")

segment_count = rfm["Segment"].value_counts().reset_index()
segment_count.columns = ["Segment", "Customers"]

st.write(segment_count)   # Debug

fig = px.bar(
    segment_count,
    x="Segment",
    y="Customers",
    title="Customer Segment Distribution",
    text="Customers"
)

st.plotly_chart(fig, use_container_width=True)