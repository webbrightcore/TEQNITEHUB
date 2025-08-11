import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import requests
from PIL import Image
from io import BytesIO
import json

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Teqnitehub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# Load Assets
# -------------------------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception as e:
        return None

def load_image_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.warning(f"Image not available: {url}")
        return None

# Lottie URLs
LOTTIE_URLS = {
    "hero": "https://assets1.lottiefiles.com/packages/lf20_gn0tojcq.json",
    "services": "https://assets1.lottiefiles.com/packages/lf20_ISdC6Z.json",
    "contact": "https://assets1.lottiefiles.com/packages/lf20_uk4Bok.json",
    "student": "https://assets1.lottiefiles.com/packages/lf20_5tkzkblw.json",
    "learning": "https://assets1.lottiefiles.com/packages/lf20_5tkzkblw.json"
}

# Load animations
lottie_hero = load_lottieurl(LOTTIE_URLS["hero"])
lottie_services = load_lottieurl(LOTTIE_URLS["services"])
lottie_contact = load_lottieurl(LOTTIE_URLS["contact"])
lottie_student = load_lottieurl(LOTTIE_URLS["student"])
lottie_learning = load_lottieurl(LOTTIE_URLS["learning"])

# Image URLs
IMAGE_URLS = {
    "coding": "https://images.unsplash.com/photo-1619410283995-43d9134e7656?w=600",
    "team": "https://images.unsplash.com/photo-1571260898934-05e6b57f7d1a?w=600",
    "success": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600"
}

# Fallback local images
FALLBACK_IMAGES = {
    "coding": "https://via.placeholder.com/600x400/1E2A78/FFFFFF?text=Coding",
    "team": "https://via.placeholder.com/600x400/263238/FFFFFF?text=Team",
    "success": "https://via.placeholder.com/600x400/4A148C/FFFFFF?text=Success"
}

def get_image(url, fallback_key):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return url
    except:
        pass
    return FALLBACK_IMAGES[fallback_key]

# -------------------------------
# Modern CSS Theme
# -------------------------------
def inject_custom_css():
    st.markdown("""
    <style>
        /* Remove all sidebar elements */
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Remove the main sidebar toggle button (hamburger) */
        button[title="View fullscreen"] {
            display: none !important;
        }
        
        /* Remove the arrow icon (expand/collapse button) */
        div[data-testid="stToolbar"] {
            display: none !important;
        }
        
        /* Remove the resize handle */
        div[data-testid="stDecoration"] {
            display: none !important;
        }
        
        /* Adjust main content padding */
        .stApp {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Remove Streamlit's default header/footer */
        header[data-testid="stHeader"], footer[data-testid="stFooter"] {
            display: none !important;
        }
        
        /* Base Styles */
        body, .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Modern Navbar */
        .navbar-container {
            display: flex;
            flex-direction: column;
            padding: 15px 5%;
            margin: -1rem -1rem 30px -1rem;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e) !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            backdrop-filter: blur(5px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .navbar-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .navbar-title {
            font-size: 2.2rem;
            margin: 0;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 10px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            background: linear-gradient(to right, #ffffff, #f9f9f9);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 10px 0;
            width: 100%;
            text-align: center;
        }
        
        .navbar-tabs {
            display: flex;
            gap: 15px;
            width: 100%;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 10px;
        }
        
        .navbar-tab {
            justify-content: center;
            padding: 8px 20px;
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 1rem;
            position: relative;
            white-space: nowrap;
            border-radius: 50px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .navbar-tab:hover {
            color: #000 !important;
            background: #fdbb2d !important;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .navbar-tab.active {
            color: white;
            background: rgba(255, 255, 255, 0.3);
            font-weight: 700;
        }
        
        .navbar-tab.active::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 50%;
            transform: translateX(-50%);
            width: 60%;
            height: 3px;
            background: white;
            border-radius: 3px;
        }
        
        /* Hero Section */
        .hero-section {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 10px 40px;
            border-radius: 16px;
            text-align: center;
            margin-top: 0;
            margin-bottom: 50px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        
        .hero-content {
            position: relative;
            z-index: 2;
        }
        
        .hero-header {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 20px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
            background: linear-gradient(to right, #ffffff, #f9f9f9);
            -webkit-background-clip: text;
            background-clip: text;
        }
        
        .hero-subtitle {
            font-size: 22px;
            color: rgba(255,255,255,0.9);
            margin-bottom: 30px;
        }
        
        /* Cards */
        .custom-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            margin-bottom: 25px;
            height: 100%;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .custom-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.2);
            border-color: rgba(255, 255, 255, 0.4);
        }
        
        .custom-card h2 {
            color: white;
            margin-top: 0;
        }
        
        .custom-card p {
            color: rgba(255,255,255,0.8);
        }
        
        .custom-card ul {
            padding-left: 20px;
            color: rgba(255,255,255,0.8);
        }
        
        /* Buttons - Updated to use #fdbb2d color */
        .stButton>button {
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: 700;
        background: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        background: #fdbb2d !important;
        color: #000 !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton>button:active {
        transform: translateY(0);
        background: rgba(255, 255, 255, 0.05) !important;
    }
    
    .stButton>button::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.1),
            transparent
        );
        transition: 0.5s;
    }
    
    .stButton>button:hover::after {
        left: 100%;
    }
        
        /* Form submit button specific styling */
        .stButton>button[type="submit"] {
            width: 100%;
            margin-top: 10px;
        }
        
        /* Images */
        .feature-img {
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            margin-bottom: 25px;
            width: 100%;
            height: 250px;
            object-fit: cover;
        }
        
        .feature-img:hover {
            transform: scale(1.02);
        }
        
        /* Testimonials */
        .testimonial-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            margin: 25px 0;
            border-left: 4px solid #fdbb2d;
        }
        
        .testimonial-text {
            font-style: italic;
            color: rgba(255,255,255,0.9);
            margin-bottom: 20px;
        }
        
        .testimonial-author {
            font-weight: 700;
            color: white;
        }
        
        /* Feature Cards */
        .feature-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            margin: 25px 0;
            border-left: 4px solid #5f2c82;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.2);
            border-color: rgba(255, 255, 255, 0.4);
        }
        
        /* Stats */
        .stats-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 16px;
            text-align: center;
            margin: 15px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .navbar-container {
                padding: 10px;
            }
            
            .navbar-content {
                flex-direction: column;
            }
            
            .navbar-title {
                font-size: 1.8rem;
                padding: 5px 0;
                margin-bottom: 10px;
            }
            
            .navbar-tabs {
                gap: 8px;
                margin-top: 5px;
            }
            
            .navbar-tab {
                padding: 6px 12px;
                font-size: 0.85rem;
            }
            
            .hero-header {
                font-size: 2.5rem;
            }
            
            .hero-subtitle {
                font-size: 18px;
            }
            
            .custom-card {
                padding: 20px;
            }
            
            .feature-img {
                height: 200px;
            }
            
            /* Stack columns on mobile */
            [data-testid="column"] {
                width: 100% !important;
                padding: 0 !important;
                margin-bottom: 20px;
            }
            
            /* Adjust typing animation container */
            #typed-text {
                font-size: 1.5rem;
                line-height: 1.3;
                margin-top: -100px;
            }
            
            /* Adjust button sizes */
            .stButton>button {
                width: 100%;
                margin-bottom: 10px;
            }
            
            /* Adjust testimonial layout */
            .testimonial-card {
                margin: 10px 0;
                padding: 20px;
            }
            
            /* Make sure images don't overflow */
            img {
                max-width: 100%;
                height: auto;
            }
            
            /* Adjust program cards */
            .custom-card h2 {
                font-size: 1.5rem;
            }
            
            /* Reduce padding in about section */
            .hero-section {
                padding: 20px;
            }
        }
        @media (max-width: 768px) {
            /* Navbar responsive styles */
            .st-emotion-cache-1kyxreq {
                flex-direction: column !important;
                gap: 10px !important;
            }
            
            h1 {
                width: 100% !important;
                text-align: center !important;
                margin-bottom: 10px !important;
                font-size: 1.8rem !important;
            }
            
            .navbar-tabs {
                width: 100% !important;
                justify-content: center !important;
                flex-wrap: wrap !important;
                gap: 8px !important;
            }
            
            .navbar-tab {
                padding: 6px 12px !important;
                font-size: 0.85rem !important;
            }
        }
        html, body, .stApp {
    overflow-x: hidden;
}

/* Only show spacer on small screens */
.mobile-spacer {
    display: none;
}

@media (max-width: 768px) {
    .mobile-spacer {
        display: block;
        height: 0px;  /* Will be updated via JS */
        transition: height 0.3s ease;
    }
}
    </style>
    """, unsafe_allow_html=True)
inject_custom_css()

# -------------------------------
# Navigation Bar
# -------------------------------

# Replace with your own hosted image URL (from Imgur, Postimages, etc.)
image_url = "https://i.postimg.cc/9XRV1j0d/img.png"  # 👈 Replace this with your hosted logo URL

st.markdown(f"""
<style>
/* Layout fix */
.block-container, .main {{
    padding-top: 0 !important;
    margin-top: 0 !important;
}}
html, body, .stApp {{
    overflow-x: hidden;
    margin: 0;
    padding: 0;
    background-color: #0e1117;
}}

/* Flex container for logo + title */
.header-container {{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 15px;
    margin-bottom: 20px;
}}

/* Always keep row layout, but center content on mobile */
@media (max-width: 768px) {{
    .header-container {{
        flex-direction: row !important;
        justify-content: flex-start !important;
        text-align: left !important;
        padding: 0 15px;
    }}
    .header-container h1 {{
        text-align: left !important;
    }}
}}

/* Navbar styling */
.navbar-links {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    margin-top: 0;
    padding-left: 15px;
}}
.navbar-link {{
    padding: 6px 16px;
    color: white !important;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
    white-space: nowrap;
    border-radius: 50px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: none;
    transition: all 0.3s ease;
}}
.navbar-link.active,
.navbar-link:hover {{
    background-color: #fdbb2d;
    color: #000 !important;
}}
</style>

<!-- Logo + Title -->
<div class="header-container">
    <img src="{image_url}" alt="Logo" style="height: 50px;">
    <h1 style="font-size: 2rem; font-weight: 800; color: #fdbb2d; text-shadow: 0 2px 10px rgba(0,0,0,0.3); text-transform: uppercase; margin: 0; text-align: left;">
        Teqnitehub
    </h1>
</div>

<!-- Navigation Links -->
<div class="navbar-links">
    <a href="#home" class="navbar-link active">Home</a>
    <a href="#about" class="navbar-link">About</a>
    <a href="#courses" class="navbar-link">Courses</a>
    <a href="#programs" class="navbar-link">Programs</a>
    <a href="#contact" class="navbar-link">Contact</a>
</div>
""", unsafe_allow_html=True)



# Set page background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1c1c1c;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Typing animation HTML
components.html("""
<div id="typed-text-container" style="display: flex; justify-content: center; margin-top: 0; margin-bottom: 0;">
  <div id="typed-text" style="
      font-family: 'Helvetica Neue', sans-serif;
      font-weight: 700;
      text-align: center;
      color: white;
      max-width: 90%;
      line-height: 1.4;
      word-break: break-word;
  "></div>
</div>

<!-- Spacer to push buttons down on mobile -->
<div class="mobile-spacer"></div>

<script>
const letters = [
  "“","<br>",
  "<span style='font-size:28px;'>Y</span>",
  "<span style='font-size:28px;'>O</span>",
  "<span style='font-size:28px;'>U</span>",
  "<span style='font-size:28px;'>R</span>", " ",
  "<span style='font-size:28px; color:#fdbb2d;'>F</span>",
  "<span style='font-size:28px; color:#fdbb2d;'>U</span>",
  "<span style='font-size:28px; color:#fdbb2d;'>T</span>",
  "<span style='font-size:28px; color:#fdbb2d;'>U</span>",
  "<span style='font-size:28px; color:#fdbb2d;'>R</span>",
  "<span style='font-size:28px; color:#fdbb2d;'>E</span>", " ",
  "<span style='font-size:28px;'>I</span>",
  "<span style='font-size:28px;'>S</span>", " ",
  "<span style='font-size:28px;'>C</span>",
  "<span style='font-size:28px;'>R</span>",
  "<span style='font-size:28px;'>E</span>",
  "<span style='font-size:28px;'>A</span>",
  "<span style='font-size:28px;'>T</span>",
  "<span style='font-size:28px;'>E</span>",
  "<span style='font-size:28px;'>D</span>", " ",
  "<span style='font-size:28px;'>B</span>",
  "<span style='font-size:28px;'>Y</span>", " ",
  "<span style='font-size:28px;'>W</span>",
  "<span style='font-size:28px;'>H</span>",
  "<span style='font-size:28px;'>A</span>",
  "<span style='font-size:28px;'>T</span>", "<br>",
  "<span style='font-size:60px;'>Y</span>",
  "<span style='font-size:60px;'>O</span>",
  "<span style='font-size:60px;'>U</span>", " ",
  "<span style='font-size:60px;'>D</span>",
  "<span style='font-size:60px;'>O</span>", " ",
  "<span style='font-size:100px; color:#fdbb2d;'>{</span>", " ",
  "<span style='font-size:90px;'>T</span>",
  "<span style='font-size:90px;'>O</span>",
  "<span style='font-size:90px;'>D</span>",
  "<span style='font-size:90px;'>A</span>",
  "<span style='font-size:90px;'>Y</span>", " ",
  "<span style='font-size:100px; color:#fdbb2d;'>}</span>", "<br>",
  "<span style='font-size:28px; text-decoration: line-through;'>N</span>",
  "<span style='font-size:28px; text-decoration: line-through;'>O</span>",
  "<span style='font-size:28px; text-decoration: line-through;'>T</span>", " ",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>T</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>O</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>M</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>O</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>R</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>R</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>O</span>",
  "<span style='font-size:28px; color: grey; opacity: 0.5;'>W</span>",
  ".", "”"
];

let i = 0;
let output = "";

function typeLetter() {
    if (i < letters.length) {
        output += letters[i];
        document.getElementById("typed-text").innerHTML = output;
        i++;
        setTimeout(typeLetter, 40);
    } else {
        // Add spacing on mobile after animation
        document.querySelector(".mobile-spacer").style.height = "100px";
    }
}

window.onload = typeLetter;
</script>
""", height=500)

# Buttons below animation
cols = st.columns(2)
with cols[0]:
    if st.button("Apply Now", key="python_apply_wide", use_container_width=True):
        st.switch_page("pages/1_application.py")
with cols[1]:
    if st.button("LMS Login", key="ml_apply_wide", use_container_width=True):
        st.switch_page("pages/2_lms_portal.py")
        
# Features Section
st.markdown("<h2 style='display: flex; justify-content: center; text-align: center; margin-top: 20px; color: #fdbb2d;'>Why Choose Teqnitehub?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="feature-card">
        <img src="{get_image(IMAGE_URLS['coding'], 'coding')}" class="feature-img" alt="Hands-on Experience">
        <h3 style="color: white;">Hands-on Experience</h3>
        <p class="testimonial-text">Work on real-world projects with industry experts</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if lottie_student:
        st_lottie(lottie_student, height=200, key="student")
    else:
        st.image(get_image(IMAGE_URLS["team"], "team"), use_container_width=True)
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: white;">Unlock Your Potential</h3>
        <p class="testimonial-text">"Success doesn't come to you — you go to it."</p>
    </div>
""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="feature-card">
        <img src="{get_image(IMAGE_URLS['success'], 'success')}" class="feature-img" alt="Career Support">
        <h3 style="color: white;">Career Support</h3>
        <p class="testimonial-text">Resume building and interview preparation</p>
    </div>
    """, unsafe_allow_html=True)

# # Testimonials
st.markdown("<h2 style='text-align: center; color: #fdbb2d;'>What Our Students Say</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">"As an AI student, the projects and interactive content helped me truly understand complex topics like machine learning and neural networks. I now feel confident applying these skills in real-world scenarios."</p>
        <p class="testimonial-author">- Muhammad Arham, AI Student</p>
    </div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">"Learning Java here was a game-changer. The concepts were explained clearly, and the hands-on coding challenges helped me master OOP and data structures with confidence."</p>
        <p class="testimonial-author">- Aftab Malik, Java Developer Trainee</p>
    </div>
""", unsafe_allow_html=True)
    

col3,col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">"The hands-on projects and real-world examples helped me build a solid foundation in AI. It was a game-changer for my career."</p>
        <p class="testimonial-author">- Muhammad Furqan Adnan, AI Specialist</p>
    </div>
""", unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">"The Teqnitehub internship completely transformed my career. I went from knowing basics to landing a full-time developer role in just 3 months!"</p>
        <p class="testimonial-author">- Huzaifa Khan, Python Developer</p>
    </div>
    """, unsafe_allow_html=True)



# -------------------------------
# ABOUT SECTION
# -------------------------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='color: #fdbb2d;'>About Teqnitehub</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <p style="font-size: 18px; line-height: 1.6; color: rgba(255,255,255,0.85);">
        <strong style="color: white;">Teqnitehub</strong> started its journey back in 2020 with a simple belief:
        practical experience matters just as much as theory. Many students leave classrooms unsure of what comes next.
        We set out to fix that — by offering hands-on internships and real-world projects that prepare you for the tech industry.
    </p>

    <h3 style="color: #fdbb2d;">Our Mission</h3>
    <div class="custom-card">
        <p style="font-size: 18px; line-height: 1.6; margin: 0; color: rgba(255,255,255,0.85);">
            We aim to make tech learning accessible to everyone — no matter where you’re from. 
            It’s about building skills that last and opening doors to real opportunities.
        </p>
    </div>

    <h3 style="margin-top: 30px; color: #fdbb2d;">Meet the Team</h3>
    <p style="font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.8);">
        We're a small group of developers, mentors, and educators who believe in learning by doing. 
        Together, we're here to help you grow, build, and succeed.
    </p>
""", unsafe_allow_html=True)

    
with col2:
    st.image(
        "https://miro.medium.com/v2/resize:fit:1024/1*gQzkQ3uJ0SwJL51t16bivw.jpeg",
        use_container_width=True,
        caption="Our Dedicated Team"
    )

if lottie_services:
    st_lottie(lottie_services, height=300, key="about")

# -------------------------------
# COURSES SECTION
# -------------------------------
st.markdown('<div id="courses"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='color: #fdbb2d;'>Our Courses</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="custom-card" style="background: linear-gradient(135deg, rgba(30,42,120,0.7), rgba(178,31,31,0.7));">
        <h2>🐍 Python Developer</h2>
        <p><strong>Duration:</strong> 3 months</p>
        <ul>
            <li>Python fundamentals & OOP</li>
            <li>API development with Flask/Django</li>
            <li>Automation & scripting</li>
            <li>Testing & debugging</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # if st.button("Coming Soon"):
    st.info("This course is coming soon. Stay tuned!")


with col2:
    st.markdown("""
    <div class="custom-card" style="background: linear-gradient(135deg, rgba(38,50,56,0.7), rgba(253,187,45,0.7));">
        <h2>🤖 Machine Learning</h2>
        <p><strong>Duration:</strong> 3 months</p>
        <ul>
            <li>Supervised & unsupervised learning</li>
            <li>Model building with scikit-learn</li>
            <li>Feature engineering</li>
            <li>Model evaluation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # if st.button("Coming Soon", key="ml_apply_unique"):
    st.info("This course is coming soon. Stay tuned!")

# Course Benefits
st.markdown("<h2 style='text-align: center; margin-top: 50px; color: #fdbb2d;'>Course Benefits</h2>", unsafe_allow_html=True)

if lottie_learning:
    st_lottie(lottie_learning, height=300, key="learning")
else:
    st.image(get_image(IMAGE_URLS["success"], "success"), use_container_width=True)

benefits_col1, benefits_col2 = st.columns(2)
with benefits_col1:
    st.markdown("""
    <div class="custom-card">
        <h3>🎯 Project-Based Learning</h3>
        <p>Work on real-world projects that you can add to your portfolio</p>
    </div>
    """, unsafe_allow_html=True)

with benefits_col2:
    st.markdown("""
    <div class="custom-card">
        <h3>📜 Certification</h3>
        <p>Earn a recognized certificate upon completion</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# PROGRAMS SECTION
# -------------------------------
st.markdown('<div id="programs"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='color: #fdbb2d;'>Our Internship Programs</h1>", unsafe_allow_html=True)

rows = [
    ("🐍 Python Developer", "rgba(30,42,120,0.7)", "white", "python_dev"),
    ("🌐 Web Development", "rgba(51,51,51,0.7)", "white", "web_dev"),
    ("📱 Flutter Development", "rgba(55,71,79,0.7)", "white", "flutter_dev"),
    ("🔧 PHP - Laravel", "rgba(74,20,140,0.7)", "white", "php_dev"),
    ("🤖 Machine Learning", "rgba(38,50,56,0.7)", "white", "ml_dev"),
    ("🧠 AI", "rgba(49,27,146,0.7)", "white", "ai_dev"),
    ("📊 Data Science", "rgba(191,54,12,0.7)", "white", "ds_dev"),
    ("🛡️ CyberSecurity", "rgba(136,14,79,0.7)", "white", "cyber_dev")
]

descriptions = [
    "Python fundamentals & OOP, API development, automation, and error handling.",
    "HTML, CSS, JS, responsive web design, React.js, and dynamic websites.",
    "Dart basics, Flutter UI, state management, deploying apps.",
    "PHP fundamentals, Laravel basics, building REST APIs, MySQL.",
    "Supervised/unsupervised learning, scikit-learn, feature engineering.",
    "Neural networks, NLP, model deployment, real-world AI.",
    "Data cleaning, visualization, EDA, intro to ML models.",
    "Network security, vulnerabilities, ethical hacking, security tools."
]

for i in range(0, len(rows), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(rows):
            title, bg, btn_color, key = rows[i + j]
            desc = descriptions[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="custom-card" style="background: {bg};">
                    <h2>{title}</h2>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("Apply Now", key=f"{key}_apply"):
                    st.switch_page("pages/1_application.py")

# Program Highlights
st.markdown("<h2 style='text-align: center; margin-top: 50px; color: #fdbb2d;'>Program Highlights</h2>", unsafe_allow_html=True)

highlights = [
    ("📅", "Flexible Duration", "Choose between 1-6 month programs based on your availability"),
    ("👥", "Small Batch Sizes", "Limited to 15 students per batch for personalized attention"),
    ("💻", "Remote Friendly", "Learn from anywhere with our online platform"),
    ("🏆", "Hackathons", "Regular coding competitions with exciting prizes")
]

cols = st.columns(4)
for i, (icon, title, desc) in enumerate(highlights):
    with cols[i]:
        st.markdown(f"""
        <div class="custom-card" style="text-align: center;">
            <h1 style="font-size: 2.5rem; margin: 0; color: #fdbb2d;">{icon}</h1>
            <h3 style="color: white;">{title}</h3>
            <p style="color: rgba(255,255,255,0.8);">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# CONTACT SECTION
# -------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='color: #fdbb2d;'>Get In Touch</h1>", unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col2:
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name", placeholder="Enter your name")
    email = st.text_input("Your Email", placeholder="Enter your email address")
    message = st.text_area("Your Message", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        if name and email and message:
            st.success("Thank you for your message! We'll get back to you soon.")
        else:
            st.warning("Please fill in all fields.")



# with col1:
st.markdown("""
<div class="custom-card">
    <h3 style="color: white;">Contact Information</h3>
    <p style="color: rgba(255,255,255,0.8);">📧 <strong>Email:</strong> ahmeralishoukat.work@gmail.com</p>
    <p style="color: rgba(255,255,255,0.8);">📞 <strong>Phone:</strong> +92 3152661772</p>
    <p style="color: rgba(255,255,255,0.8);">📍 <strong>Address:</strong> Hyderabad, Sindh</p>
    <div style="margin-top: 20px;">
        <h3 style="color: white;">Follow Us</h3>
        <p style="color: rgba(255,255,255,0.8);">👉 <a href="https://www.linkedin.com/in/ahmer-ali-3933a4309/" target="_blank" style="color: #fdbb2d; text-decoration: none;">LinkedIn</a></p>
        <p style="color: rgba(255,255,255,0.8);">👉 <a href="https://instagram.com/ahmeralishoukat" target="_blank" style="color: #fdbb2d; text-decoration: none;">Instagram</a></p>
    </div>
</div>
""", unsafe_allow_html=True)
