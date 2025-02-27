import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():
    # Create Sidebar
    with st.sidebar:
        selected = option_menu(
            menu_title="Smart Data Tool",
            options=["Home", "Guide", "Featured", "Settings", "Support"],
            icons=["house", "book", "star", "gear", "question-circle"],
            menu_icon="cast",
            default_index=0,
        )

        if selected == "Guide":
            guide_section = option_menu(
                menu_title="User Guide",
                options=["Introduction", "Installation", "Frontend & Backend", "Troubleshooting"],
                icons=["info-circle", "download", "desktop", "wrench"],
                menu_icon="file-earmark-text",
                default_index=0,
            )
            return selected, guide_section

        elif selected == "Featured":
            featured_section = option_menu(
                menu_title="Features",
                options=["Data Upload & Import", "Data Cleaning & Processing", "Data Transformation", 
                         "Data Analysis", "Data Export", "Automation & AI", "AI-powered Insights", 
                         "Multi-file Processing", "User Roles & Access", "Database Integration", 
                         "Real-time Processing", "Support & Reporting", "Security & Encryption", 
                         "Workflow Automation", "Frontend Features", "Backend Features"],
                icons=["cloud-upload", "pencil", "shuffle", "graph-up", "arrow-right-circle", "robot", 
                       "lightbulb", "folder", "person-lock", "database", "cloud-sync", "shield-lock", "gear", 
                       "desktop", "server"],
                menu_icon="app",
                default_index=0,
            )
            return selected, featured_section
        
        else:
            return selected, None
