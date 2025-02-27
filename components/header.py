import streamlit as st

def show_header():
    st.markdown(
        """
        
        <style>
            .header {
                background-color: #415A77;
                padding: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                border-radius: 8px;
                margin-bottom: 10px;
            }
            .divider {
                border-top: 2px solid #415A77;
                margin-top: 10px;
            }
        </style>
        <div class="header">Smart Data Tool</div>
        <div class="divider"></div>
        """,
        unsafe_allow_html=True
    )
