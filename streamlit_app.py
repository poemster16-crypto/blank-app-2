import streamlit as st

# Page Configuration & SEO Settings
st.set_page_config(
    page_title="Bilash Fusion | Ultimate Defense & Media Hub",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Hotstar / Pro Streaming App Vibe)
st.markdown("""
    <head>
        <meta name="description" content="Bilash Fusion - Your ultimate destination for advanced defense technology insights, military analysis, and exclusive YouTube video content.">
        <meta name="keywords" content="Bilash Fusion, Defense technology, Military tech, YouTube defense videos, Fighter jets, Content hub, Strategic analysis">
    </head>
    <style>
    .main-title {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
    }
    .banner-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #3B82F6 100%);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #1E3A8A;
        margin-top: 20px;
        margin-bottom: 15px;
        border-left: 5px solid #1E3A8A;
        padding-left: 10px;
    }
    .content-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .result-box {
        background-color: #F8FAFC;
        padding: 25px;
        border-radius: 10px;
        border-left: 6px solid #1E3A8A;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Top Hero / Pro Banner
st.markdown("""
    <div class="banner-container">
        <h1>🛡️ BILASH FUSION DIGITAL HUB</h1>
        <p>Explore Deep-Dive Defense Tech Intelligence & Exclusive Video Content All in One Place</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Branding & Navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/shield.png", width=75)
    st.markdown("## Bilash Fusion")
    st.markdown("**Official Media & AI Intelligence Platform**")
    st.markdown("---")
    
    # Navigation Menu in Sidebar
    app_mode = st.radio("📌 Select Hub Section:", ["🏠 Home & Featured Content", "🔍 AI Defense Content Generator"])
    
    st.markdown("---")
    st.markdown("### 🌐 Official Channels:")
    st.markdown("- [YouTube Channel](https://www.youtube.com)")
    st.markdown("- [Facebook Page](https://www.facebook.com)")
    st.markdown("- [Instagram](https://www.instagram.com)")
    st.markdown("---")
    st.markdown("<small>© 2026 Bilash Fusion. All Rights Reserved.</small>", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# SECTION 1: HOME & FEATURED CONTENT (Like OTT / YouTube Feed)
# -------------------------------------------------------------------------
if app_mode == "🏠 Home & Featured Content":
    st.markdown('<p class="section-header">🔥 Featured Video Content & Latest Uploads</p>', unsafe_allow_html=True)
    st.markdown("Watch our latest defense analysis and military breakdowns directly or via our YouTube channel.")
    
    # Creating a Grid layout for Content Cards (Simulating OTT/YouTube Grid)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-card">
            <h3>🚀 Rafale Jet Power</h3>
            <p>Complete tactical breakdown of modern fighter capabilities and aerial dominance.</p>
            <a href="https://www.youtube.com" target="_blank" style="color: #1E3A8A; font-weight: bold;">Watch on YouTube ➔</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="content-card">
            <h3>🛡️ S-400 Air Defense</h3>
            <p>How the world's most feared missile defense shield operates in real warfare.</p>
            <a href="https://www.youtube.com" target="_blank" style="color: #1E3A8A; font-weight: bold;">Watch on YouTube ➔</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="content-card">
            <h3>⚡ BrahMos Missile Tech</h3>
            <p>Supersonic cruise missile technology and its impact on modern naval strategy.</p>
            <a href="https://www.youtube.com" target="_blank" style="color: #1E3A8A; font-weight: bold;">Watch on YouTube ➔</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📢 Announcements & Updates")
    st.info("💡 Welcome to the brand new Bilash Fusion platform! You can now access both our research reports and video contents seamlessly. Switch to the **'AI Defense Content Generator'** from the sidebar to create custom outlines.")

# -------------------------------------------------------------------------
# SECTION 2: AI DEFENSE CONTENT GENERATOR
# -------------------------------------------------------------------------
elif app_mode == "🔍 AI Defense Content Generator":
    st.markdown('<p class="section-header">🤖 Advanced A-Z Defense Intelligence Generator</p>', unsafe_allow_html=True)
    st.markdown("Type any military weapon, aircraft, or tech to extract comprehensive reports and content outlines.")
    
    query = st.text_input("🎯 Enter Defense Topic (e.g., Rafale Jet, S-400, Tejas, BrahMos):", placeholder="Type weapon or tech name here...")

    if st.button("🚀 Generate A-Z Detailed Report"):
        if query.strip() == "":
            st.warning("⚠️ Please enter a valid topic or weapon name in the search box!")
        else:
            st.success(f"✅ Comprehensive intelligence compiled successfully for: **{query}**")
            
            st.markdown(f"### 📌 Detailed Intelligence Report: {query}")
            
            st.markdown(f"""
            <div class="result-box">
            
            <h4>1. Executive Summary & Historical Background</h4>
            <p><b>{query}</b> stands as a formidable asset in modern military architecture. Developed out of intense strategic necessity and engineering precision, its deployment marks a monumental shift in regional and global deterrence capabilities.</p>
            
            <h4>2. Technical Specifications & Core Capabilities</h4>
            <ul>
                <li><b>Performance & Speed:</b> High thrust-to-weight mechanics ensuring superior operational boundaries and speed thresholds.</li>
                <li><b>Payload & Armament:</b> Multi-role compatibility supporting precision-guided munitions, advanced strike packages, and tactical defense systems.</li>
                <li><b>Avionics & Radar Suite:</b> Next-generation active sensor arrays, electronic warfare integration, and encrypted real-time data networking.</li>
                <li><b>Survivability & Design:</b> Low-observability profiling, structural reinforcement, and automated countermeasure deployment.</li>
            </ul>
            
            <h4>3. Strategic Impact & Global Analysis</h4>
            <p>Compared to contemporary systems, <b>{query}</b> offers unprecedented tactical adaptability, making it an indispensable asset for defense forces worldwide.</p>
            
            <h4>4. YouTube Content Script & Video Outline Idea</h4>
            <ul>
                <li><b>Catchy Hook (Intro):</b> "Why is {query} changing the rules of modern warfare? Let's find out!"</li>
                <li><b>Segment 1:</b> Origin and historical background.</li>
                <li><b>Segment 2:</b> Deep dive into engineering, speed, and weapons payload.</li>
                <li><b>Segment 3:</b> Future upgrades and strategic importance.</li>
                <li><b>Outro/CTA:</b> Reminder to subscribe to **Bilash Fusion** for more insights.</li>
            </ul>
            
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Bilash Fusion Digital Platform | Powered by Advanced Web & AI Architecture</p>", unsafe_allow_html=True)
            
