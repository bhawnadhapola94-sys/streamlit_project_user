import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")

st.title(" Conclusion")

st.markdown("---")

st.header(" Project Summary")

st.write("""
This project analyzed online retail transaction data to understand customer purchasing behavior.
Exploratory Data Analysis (EDA) was performed to identify sales trends, customer patterns, and product performance.
Using RFM (Recency, Frequency, Monetary) analysis, customers were segmented into different groups to support targeted marketing strategies.
A Product Recommendation module was also developed to help suggest relevant products based on customer interests.
""")

st.markdown("---")

st.header(" Key Insights")

st.write("""
 RFM analysis successfully identified valuable and less active customers.

 Customer segmentation helps businesses personalize marketing campaigns.

 Top-selling products were identified through sales analysis.

 Product recommendations can improve customer experience and increase sales.

 Interactive dashboards make business data easy to understand and analyze.
""")

st.markdown("---")

st.header(" Business Recommendations")

st.write("""
 Reward Champions with loyalty programs and exclusive offers.

 Provide personalized recommendations to Loyal Customers.

 Encourage Potential Loyalists with targeted promotions.

 Re-engage At-Risk customers through discount campaigns.

 Promote best-selling products to increase overall revenue.

 Use customer segmentation to improve marketing efficiency and customer retention.
""")

st.markdown("---")

st.header(" Future Scope")

st.write("""
• Apply Machine Learning for smarter product recommendations.

• Build real-time dashboards connected to live databases.

• Integrate customer feedback and ratings into recommendations.

• Develop personalized email and marketing campaign automation.

• Deploy the application for business users on the cloud.
""")

st.markdown("---")

st.success("Thank You! ")
st.write("Shopper Spectrum – Customer Segmentation & Product Recommendation System")