import streamlit as st
import pandas as pd

st.set_page_config(page_title="EDA Dashboard", layout="wide")

df = pd.read_csv(r"online_retail_small.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.title("Exploratory Data Analysis")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)
import plotly.express as px

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.subheader(" Top 10 Countries by Sales")

country_sales = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    country_sales,
    x="Country",
    y="Sales",
    color="Sales",
    title="Top 10 Countries by Sales"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader(" Monthly Sales Trend")
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)
st.subheader("Top 10 Products by Sales")

top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_products,
    x="Sales",
    y="Description",
    orientation="h",
    color="Sales",
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig3, use_container_width=True)
st.subheader(" Quantity Distribution")

fig4 = px.histogram(
    df,
    x="Quantity",
    nbins=50,
    title="Quantity Distribution"
)

st.plotly_chart(fig4, use_container_width=True)
st.subheader(" Sales Distribution")

fig5 = px.histogram(
    df,
    x="Sales",
    nbins=50,
    title="Sales Distribution"
)

st.plotly_chart(fig5, use_container_width=True)