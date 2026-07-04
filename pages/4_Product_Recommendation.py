import streamlit as st
import pandas as pd

st.set_page_config(page_title="Product Recommendation", layout="wide")

st.title(" Product Recommendation System")

df = pd.read_csv("online_retail_small.csv")

st.success("Dataset Loaded Successfully ")
st.subheader("Select a Product")

products = sorted(df["Description"].dropna().unique())

selected_product = st.selectbox(
    "Choose Product",
    products
)

st.write("Selected Product:", selected_product)
st.subheader("Recommended Products")

recommendations = (
    df[df["Description"] != selected_product]["Description"]
    .drop_duplicates()
    .sample(10, random_state=42)
)

st.table(recommendations.reset_index(drop=True))
st.subheader("Selected Product Details")

product_data = df[df["Description"] == selected_product]

st.write("Number of Purchases:", len(product_data))
st.write("Average Price:", round(product_data["UnitPrice"].mean(),2))
st.write("Total Quantity Sold:", product_data["Quantity"].sum())
import plotly.express as px

st.subheader("Top 10 Best Selling Products")

top_products = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    top_products,
    x="Quantity",
    y="Description",
    orientation="h",
    title="Top 10 Best Selling Products"
)

st.plotly_chart(fig, use_container_width=True)