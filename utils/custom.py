css_code: str = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

    /* Hide Streamlit native headers, footers and menus to make it a standalone custom web app */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Global Typography & Font override (Outfit/Inter style) */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', sans-serif !important;
        background-color: #f4fcf7 !important;
    }

    /* Main background - Sleek Minimalist Light Mint Gray */
    .stApp {
        background-color: #f4fcf7 !important;
        background-image: radial-gradient(circle at 50% 50%, #ffffff 0%, #edf7f1 100%) !important;
        color: #052e16 !important;
    }

    /* Sidebar Custom Styling - Minimalist Solid White with thin mint border */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #dcfce7 !important;
        box-shadow: none !important;
    }

    /* Typography & Headers - Bold Forest Black */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        color: #042f1a !important;
        font-weight: 800 !important;
        letter-spacing: -0.75px !important;
    }

    /* Header Container & Subtitle */
    .header-container {
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 3.5rem;
    }
    .main-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: #042f1a !important;
        letter-spacing: -1.5px !important;
        margin-bottom: 0.5rem !important;
        background: linear-gradient(90deg, #059669 0%, #10b981 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    .subtitle-text {
        font-size: 1.02rem !important;
        color: #3f624c !important;
        font-weight: 400 !important;
        max-width: 600px;
        margin: 0 auto !important;
        line-height: 1.5 !important;
    }

    /* Section title styling */
    .section-title {
        font-size: 1.15rem !important;
        margin-top: 0 !important;
        margin-bottom: 1.2rem !important;
        border-bottom: 1px solid #dcfce7 !important;
        padding-bottom: 8px !important;
        color: #042f1a !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #059669 0%, #10b981 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }

    /* File Uploader styling - Clean white card with thin green border */
    [data-testid="stFileUploader"] {
        background: #ffffff !important;
        border: 1px solid #dcfce7 !important;
        border-radius: 12px !important;
        padding: 24px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.02) !important;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: #059669 !important;
        background: #fafdfb !important;
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.04) !important;
    }

    /* Input Image custom styling */
    [data-testid="stImage"] img {
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(5, 150, 105, 0.04) !important;
        transition: all 0.2s ease-in-out !important;
        border: 1px solid #dcfce7 !important;
    }
    
    [data-testid="stImage"] img:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(5, 150, 105, 0.08) !important;
    }

    /* Custom Result Cards - Matte White Cards with clean mint borders */
    .result-card {
        background: #ffffff !important;
        border: 1px solid #dcfce7 !important;
        border-radius: 12px !important;
        padding: 20px 24px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.02) !important;
        transition: all 0.2s ease-in-out !important;
    }

    .result-card:hover {
        border-color: #059669 !important;
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.05) !important;
        transform: translateY(-2px) !important;
    }

    /* Highlight Card (Story Output) */
    .highlight-card {
        background: #fafdfc !important;
        border: 1px solid #059669 !important;
    }

    .highlight-card:hover {
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.06) !important;
    }

    /* Card Labels */
    .card-label {
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        color: #059669 !important;
        margin-bottom: 6px !important;
        text-transform: uppercase !important;
    }

    /* Card Content Text */
    .card-text {
        font-size: 0.95rem !important;
        color: #052e16 !important;
        line-height: 1.6 !important;
    }

    /* Audio section title */
    .audio-title {
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        color: #059669 !important;
        margin-top: 20px !important;
        margin-bottom: 8px !important;
        letter-spacing: 0.5px !important;
    }

    /* Status Card Widget in Sidebar */
    .status-card {
        background: #f0fdf4 !important;
        border: 1px solid #dcfce7 !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        margin-top: 15px !important;
        transition: all 0.2s ease !important;
    }

    .status-card:hover {
        border-color: #059669 !important;
    }

    .status-label {
        font-size: 0.62rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        color: #3f624c !important;
        margin-bottom: 4px !important;
        text-transform: uppercase !important;
    }

    .status-dot {
        height: 6px;
        width: 6px;
        background-color: #10b981;
        border-radius: 50%;
        display: inline-block;
        animation: statusPulse 1.5s infinite;
    }

    .status-text {
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        color: #10b981 !important;
    }

    @keyframes statusPulse {
        0% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6);
        }
        70% {
            box-shadow: 0 0 0 6px rgba(16, 185, 129, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
        }
    }

    /* Override Streamlit Widget Colors Directly in CSS */
    
    /* 1. Sliders (Track & Handles) */
    div[data-testid="stSlider"] [role="slider"] {
        background-color: #059669 !important;
        border-color: #059669 !important;
    }
    div[data-testid="stSlider"] div[data-value] {
        color: #059669 !important;
    }
    div[data-testid="stSlider"] div[aria-valuenow] {
        background-color: #059669 !important;
    }
    div[data-testid="stSlider"] [style*="background-color: rgb"] {
        background-color: #059669 !important;
    }

    /* 2. Selectbox Active & Focus Border */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #dcfce7 !important;
        border-radius: 8px !important;
        color: #052e16 !important;
    }
    div[data-baseweb="select"] > div:hover {
        border-color: #059669 !important;
    }
    div[data-baseweb="select"] > div:focus-within {
        border-color: #059669 !important;
        box-shadow: 0 0 0 1px #059669 !important;
    }

    /* 3. Spinners and Progress Bars */
    .stSpinner > div {
        border-top-color: #059669 !important;
    }
    
    /* Audio Player custom styling */
    audio {
        border-radius: 20px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.04) !important;
        border: 1px solid #dcfce7 !important;
        background: #ffffff !important;
        transition: all 0.2s ease !important;
    }
    
    audio:hover {
        border-color: #059669 !important;
        box-shadow: 0 6px 16px rgba(5, 150, 105, 0.08) !important;
    }

    /* Custom divider line */
    hr {
        border-top: 1px solid #dcfce7 !important;
        margin: 20px 0 !important;
    }

    /* Info / Success message styling */
    .stAlert {
        background-color: #f0fdf4 !important;
        border: 1px solid #dcfce7 !important;
        border-radius: 8px !important;
        color: #052e16 !important;
    }
    </style>
"""