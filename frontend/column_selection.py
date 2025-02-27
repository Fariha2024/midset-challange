import streamlit as st

def select_columns():
    st.subheader("📊 Select Columns")

    # Check if a file has been uploaded
    if 'uploaded_df' not in st.session_state:
        st.warning("⚠️ Please upload a dataset first!")
        return

    df = st.session_state['uploaded_df']

    # Multi-select option for users to choose columns
    selected_columns = st.multiselect("Select columns for analysis:", df.columns.tolist())

    if selected_columns:
        st.write("### Preview of Selected Columns:")
        st.dataframe(df[selected_columns].head())

        # Store selected columns in session state for further processing
        st.session_state['selected_columns'] = df[selected_columns]
    else:
        st.info("ℹ️ No columns selected yet.")

