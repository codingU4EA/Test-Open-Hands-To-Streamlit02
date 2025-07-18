import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Basic Streamlit App",
    page_icon="🖤",
    layout="wide"
)

# Custom CSS for black background
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    .main-header {
        color: #FFFFFF;
        text-align: center;
        padding: 2rem 0;
    }
    
    .content-box {
        background-color: #1A1A1A;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 2px solid #333333;
        color: #FFFFFF;
    }
    
    /* Style Streamlit elements for dark theme */
    .stSelectbox > div > div {
        background-color: #1A1A1A;
        color: #FFFFFF;
    }
    
    .stTextInput > div > div > input {
        background-color: #1A1A1A;
        color: #FFFFFF;
        border: 1px solid #333333;
    }
    
    .stMetric {
        background-color: #1A1A1A;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #333333;
    }
    
    .stButton > button {
        background-color: #333333;
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    
    .stButton > button:hover {
        background-color: #555555;
        border: 1px solid #777777;
    }
    
<<<<<<< HEAD
    /* Style README content for better readability */
    .readme-content {
        background-color: #1A1A1A;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333333;
        color: #FFFFFF;
        margin: 1rem 0;
    }
    
    .readme-content h1, .readme-content h2, .readme-content h3 {
        color: #FFFFFF;
        border-bottom: 1px solid #333333;
        padding-bottom: 0.5rem;
    }
    
    .readme-content code {
        background-color: #333333;
        color: #FFFFFF;
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
    }
    
    .readme-content pre {
        background-color: #333333;
        color: #FFFFFF;
        padding: 1rem;
        border-radius: 5px;
        overflow-x: auto;
    }
    
    /* Style expander for dark theme */
    .streamlit-expanderHeader {
        background-color: #1A1A1A;
        color: #FFFFFF;
        border: 1px solid #333333;
    }
    
    .streamlit-expanderContent {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-top: none;
=======
    /* Style sliders for dark theme */
    .stSlider > div > div > div > div {
        background-color: #1A1A1A;
    }
    
    .stSlider > div > div > div > div > div {
        color: #FFFFFF;
    }
    
    .stSlider .stSlider-thumb {
        background-color: #FFFFFF;
    }
    
    .stSlider .stSlider-track {
        background-color: #333333;
    }
    
    /* Style README content for better readability */
    .readme-content {
        background-color: #1A1A1A;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333333;
        color: #FFFFFF;
        margin: 1rem 0;
    }
    
    .readme-content h1, .readme-content h2, .readme-content h3 {
        color: #FFFFFF;
        border-bottom: 1px solid #333333;
        padding-bottom: 0.5rem;
    }
    
    .readme-content code {
        background-color: #333333;
        color: #FFFFFF;
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
    }
    
    .readme-content pre {
        background-color: #333333;
        color: #FFFFFF;
        padding: 1rem;
        border-radius: 5px;
        overflow-x: auto;
    }
    
    /* Style expander for dark theme */
    .streamlit-expanderHeader {
        background-color: #1A1A1A;
        color: #FFFFFF;
        border: 1px solid #333333;
    }
    
    .streamlit-expanderContent {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-top: none;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">🖤 Welcome to Our Basic Streamlit App</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="content-box">
    <h2>About This App</h2>
    <p>This is a basic Streamlit application with a sleek black background theme. 
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
        "What's your favorite dark color?",
        ["Black", "Dark Gray", "Charcoal", "Midnight Blue", "Dark Purple"]
    )
    
    if favorite_color:
        st.info(f"Great choice! {favorite_color} is a beautiful color! 🖤")

with col2:
    st.markdown("""
    <div class="content-box">
        <h3>App Statistics</h3>
    </div>
    """, unsafe_allow_html=True)
    
    import random
    import time
    
    # Simple metrics
    st.metric("App Version", "2.0.0")
    st.metric("Background Color", "Black", "Sleek! 🖤")
    
    # Simple chart
    if st.button("Generate Random Data"):
        data = [random.randint(1, 100) for _ in range(10)]
        st.line_chart(data)

# Interactive Slider Section
st.markdown("---")
st.markdown("""
<div class="content-box">
    <h3>Interactive Controls</h3>
</div>
""", unsafe_allow_html=True)

# Add a slider for controlling chart data points
data_points = st.slider(
    "Number of data points for chart generation:",
    min_value=5,
    max_value=50,
    value=10,
    step=1,
    help="Adjust the number of data points to generate in the random chart"
)

# Add another slider for controlling the data range
data_range = st.slider(
    "Data value range:",
    min_value=1,
    max_value=200,
    value=100,
    step=5,
    help="Set the maximum value for randomly generated data points"
)

# Display current slider values
col1, col2 = st.columns(2)
with col1:
    st.metric("Data Points", data_points)
with col2:
    st.metric("Max Value Range", data_range)

# Generate chart with slider-controlled parameters
if st.button("Generate Chart with Slider Settings"):
    import random
    data = [random.randint(1, data_range) for _ in range(data_points)]
    st.line_chart(data)
    st.success(f"Generated chart with {data_points} points, max value {data_range}!")

# README Contents Section
st.markdown("---")
st.markdown("""
<div class="content-box">
    <h3>📖 Project Documentation</h3>
</div>
""", unsafe_allow_html=True)

# Read and display README contents
try:
    with open("README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()
    
    # Display README content using Streamlit's markdown with an expander for better UX
    with st.expander("📖 View Full README Documentation", expanded=True):
        st.markdown(readme_content)
    
except FileNotFoundError:
    st.error("README.md file not found in the project directory.")
except Exception as e:
    st.error(f"Error reading README.md: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #FFFFFF; padding: 1rem;">
    <p>Built with ❤️ using Streamlit | Black Theme Active 🖤</p>
</div>
""", unsafe_allow_html=True)