import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Basic Streamlit App",
    page_icon="🌊",
    layout="wide"
)

# Custom CSS for light blue background
st.markdown("""
<style>
    .stApp {
        background-color: #E6F3FF;
    }
    
    .main-header {
        color: #2E86AB;
        text-align: center;
        padding: 2rem 0;
    }
    
    .content-box {
        background-color: #F0F8FF;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 2px solid #B8E0FF;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">🌊 Welcome to Our Basic Streamlit App</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="content-box">
    <h2>About This App</h2>
    <p>This is a basic Streamlit application with a beautiful light blue background theme. 
    It demonstrates the fundamental capabilities of Streamlit for creating interactive web applications.</p>
</div>
""", unsafe_allow_html=True)

# Interactive elements
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-box">
        <h3>Interactive Features</h3>
    </div>
    """, unsafe_allow_html=True)
    
    name = st.text_input("Enter your name:", placeholder="Your name here...")
    if name:
        st.success(f"Hello, {name}! Welcome to our app! 👋")
    
    favorite_color = st.selectbox(
        "What's your favorite shade of blue?",
        ["Light Blue", "Sky Blue", "Navy Blue", "Turquoise", "Cyan"]
    )
    
    if favorite_color:
        st.info(f"Great choice! {favorite_color} is a beautiful color! 💙")

with col2:
    st.markdown("""
    <div class="content-box">
        <h3>App Statistics</h3>
    </div>
    """, unsafe_allow_html=True)
    
    import random
    import time
    
    # Simple metrics
    st.metric("App Version", "1.0.0")
    st.metric("Background Color", "Light Blue", "Perfect! 🎨")
    
    # Simple chart
    if st.button("Generate Random Data"):
        data = [random.randint(1, 100) for _ in range(10)]
        st.line_chart(data)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #2E86AB; padding: 1rem;">
    <p>Built with ❤️ using Streamlit | Light Blue Theme Active 🌊</p>
</div>
""", unsafe_allow_html=True)