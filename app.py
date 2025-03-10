import re
import random
import string
import streamlit as st
import base64

# Set page title and icon
st.set_page_config(page_title="PASSWORD STRENGTH METER", page_icon="🔐")

# Custom CSS for the app background
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


image_base64 = get_base64_image("background.png") 
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
         background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Main Container
with st.container():
    st.markdown(
        """
        <style>
            div[data-testid="stVerticalBlock"] {
                background-color: #fcd7ed;
                padding: 8px 10px;
                border-radius: 10px;
                padding-right: 5px !important;

            }
            @media (max-width: 600px) {
                div[data-testid="stVerticalBlock"] {
                    padding: 5px 2px; 
                    border-radius: 5px; 
                    padding-right: 2px !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
        <style>
            /* password input background color */
            .stTextInput input {
                background-color: #f7c5e6 !important; 
                color: #333 !important; 
                border-radius: 5px;
                padding: 8px;
                border: 2px solid #ec78de;  
            }

            /* number input background color */
            .stNumberInput input {
                background-color: #f7c5e6 !important;
                color: #333 !important; 
                border-radius: 5px;
                padding: 8px;
                border: 10px solid #ec78de;  
            }
        </style>
    """, unsafe_allow_html=True)

    def check_password_strength(password):
        score = 0
        suggestions = []
        
        if len(password) >= 8:
            score += 1
        else:
            suggestions.append('<span style= "color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;">⚠️ Password should be at least 8 characters long.</span>')
        
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            suggestions.append('<span style="color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;">⚠️ Include at least one uppercase letter.</span>')
        
        if re.search(r'[a-z]', password):
            score += 1
        else:
            suggestions.append('<span style="color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;">⚠️ Include at least one lowercase letter.</span>')
        
        if re.search(r'\d', password):
            score += 1
        else:
            suggestions.append('<span style="color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;">⚠️ Include at least one digit (0-9).</span>')
        
        if re.search(r'[!@#$%^&*]', password):
            score += 1
        else:
            suggestions.append('<span style="color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;">⚠️ Include at least one special character (!@#$%^&*).</span>')
        
        common_passwords = ["password123", "123456", "qwerty", "abc123", "admin"]
        if password.lower() in common_passwords:
            return "Weak", ["<span style='color: red; background-color: #ffd0d0; padding: 8px; border-radius: 5px; animation: fastBlink 0.6s ease-in-out 1;'>⚠️ This password is too common. Choose a unique password.</span>"]
        
        
        if score <= 2:
            return "Weak", suggestions
        elif score <= 4:
            return "Moderate", suggestions
        else:
            return "Strong", []

    def generate_strong_password(length=12):
        if length < 4:
            return "Length should be at least 4 to include all character types."
        
        password_chars = [
            random.choice(string.ascii_lowercase),   
            random.choice(string.ascii_uppercase), 
            random.choice(string.digits),       
            random.choice("!@#$%^&*")       
        ]
        
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password_chars += random.choices(all_chars, k=length - 4)
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
     
    # Password Strength Meter Section 
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Changa:wght@400;700&display=swap');

            @keyframes gradientFlow {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .animated-heading {
                text-align: center;
                font-size: 45px !important; 
                text-transform: uppercase;
                background: linear-gradient(-45deg, rgb(255, 20, 147), rgb(255, 105, 180), rgb(255, 67, 95), rgb(219, 112, 147), rgb(255, 0, 127));
                background-size: 300% 300%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: gradientFlow 3s ease infinite;
                font-family: 'Changa', sans-serif !important;
            }

            @media screen and (max-width: 600px) {
                .animated-heading {
                    font-size: 19px !important;
                }
            }

            .animated-heading::before {
                content: "🔐";
                -webkit-text-fill-color: initial;
                mix-blend-mode: normal;
            }
        </style>
        
        <h1 class="animated-heading">Password Strength Meter</h1>
    """, unsafe_allow_html=True)


    # Little paragraph Custom text for password strength
    st.markdown("""
        <style>
            .custom-text {
                font-style: italic;
                text-align: center;
                color: #333333;
                font-size: 18px !important; 
            }

            @media screen and (max-width: 768px) {
                .custom-text {
                    font-size: 16px !important;
                }
            }

            /* Mobile View */
            @media screen and (max-width: 480px) {
                .custom-text {
                    font-size: 14px !important;
                }
            }  
        </style>
        
        <p class="custom-text">Check your password strength below. If it's weak, follow the suggestions to make it stronger</p>
    """, unsafe_allow_html=True)


    # Password input field
    password = st.text_input("Enter your password:", type="password")

    # Custom CSS for the button
    st.markdown(
        """
        <style>
        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .stButton>button {
            text-align: center;
            font-size: 1.2em;  
            font-weight: bold;
            text-transform: uppercase;
            padding: 10px 5vw;  
            border: none;
            border-radius: 8px;
            background: linear-gradient(45deg, #ff00cc, #ff33c9, #ff6bcb, #ff00a6, #ff00b7);
            background-size: 300% 300%;
            color: white !important;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            animation: gradientFlow 3s ease infinite;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            opacity: 0.9;
            color: white !important;
        }
        
        @media screen and (max-width: 768px) {
            .stButton>button {
                font-size: 1em;
                padding: 10px 4vw;
            }
        }
        @media screen and (max-width: 480px) {
            .stButton>button {
                font-size: 0.9em;
                padding: 8px 3vw;
            }
        }
        
        /* Custom styling for success message */
        .stSuccess {
            background-color: #d4edda; 
            color: #1a7555;  
            padding: 6px;
            border-radius: 5px;
            font-size: 1.2em;
        }
        @media (max-width: 480px) {
            .stSuccess {
                font-size: 1em;  
                padding: 1px;
                border-radius: 2px;
            }
        }
       
        /* Blinking animation for error message */
        @keyframes fastBlink {
            0% { opacity: 0; }
            25% { opacity: 1; }
            50% { opacity: 0; }
            75% { opacity: 1; }
            100% { opacity: 0; }
        }
        
        /* Custom styling for error message */
        .stError {
            background-color: #ffd0d0; 
            color: #ff0f0f;  
            padding: 10px;
            border-radius: 5px;
            animation: fastBlink 0.6s ease-in-out 1; 
        }
        @media (max-width: 480px) {
            .stError {
                font-size: 1em; 
                padding: 4px; 
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Check Password Strength Button
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Check Password Strength"):
            if password:
                strength, feedback = check_password_strength(password)
                if strength == "Strong":
                    st.markdown(f'<div class="stSuccess"><strong> ✔ Password Strength {strength}- Successfully Created</strong></div>', unsafe_allow_html=True)
                else:
                    st.warning(f"**Password Strength: {strength}**")
                    for suggestion in feedback:
                        st.markdown(suggestion, unsafe_allow_html=True)
            else:
                st.markdown('<div class="stError">Please enter a password to check its strength.</div>', unsafe_allow_html=True)

    # Password Generator Section
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Rowdies:wght@300;400;700&display=swap');

            @keyframes gradientFlow {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .animated-heading2 {
                margin-top: 25px !important;
                font-size: 24px !important; 
                text-transform: uppercase;
                background: linear-gradient(-45deg, rgb(255, 20, 147), rgb(255, 105, 180), rgb(255, 67, 95), rgb(219, 112, 147), rgb(255, 0, 127));
                background-size: 300% 300%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: gradientFlow 3s ease infinite;
                font-family: 'Rowdies', sans-serif !important;
            }

            @media screen and (max-width: 600px) {
                .animated-heading2 {
                    font-size: 14px !important;  
                }
            }
        </style>
        
        <link href="https://fonts.googleapis.com/css2?family=Rowdies:wght@300;400;700&display=swap" rel="stylesheet">
        
        <h1 class="animated-heading2">Automatically Generate a Strong Password</h1>
    """, unsafe_allow_html=True)

    # Number input for password length
    password_length = st.number_input("Select password length:", min_value=8, max_value=24, value=12, step=1)


    # Custom CSS for Code Generate BG
    st.markdown("""
        <style>
            pre {
                background-color: #c3c8d1 !important;  
                color: black !important;              
                border-radius: 5px;                   
                font-size: 16px !important;           
                padding: 10px !important;             
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Generate Strong Password Button
    col3, col4 = st.columns([2, 1])
    with col3:
        if st.button("Generate Strong Password"):
            strong_password = generate_strong_password(password_length)
            st.text("Suggested Strong Password:")
            st.code(strong_password)
            
           