# import streamlit as st
# import hashlib
# from reportlab.lib.units import inch
# from datetime import datetime, date, timedelta
# import requests
# import json
# import io
# import zipfile
# import base64
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # -----------------------
# # Streamlit Config (MUST BE FIRST)
# # -----------------------
# st.set_page_config(
#     page_title="TEQNITEHUB LMS Portal",
#     page_icon="🎓",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# def inject_custom_css():
#     st.markdown("""
#     <style>
#         /* Remove all sidebar elements */
#         section[data-testid="stSidebar"] {
#             display: none !important;
#         }
        
#         /* Remove the main sidebar toggle button (hamburger) */
#         button[title="View fullscreen"] {
#             display: none !important;
#         }
        
#         /* Remove the arrow icon (expand/collapse button) */
#         div[data-testid="stToolbar"] {
#             display: none !important;
#         }
        
#         /* Remove the resize handle */
#         div[data-testid="stDecoration"] {
#             display: none !important;
#         }
        
#         /* Adjust main content padding */
#         .stApp {
#             padding: 0 !important;
#             margin: 0 !important;
#         }
        
#         /* Remove Streamlit's default header/footer */
#         header[data-testid="stHeader"], footer[data-testid="stFooter"] {
#             display: none !important;
#         }
        
#         /* Base Styles */
#         body, .stApp {
#             background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
#             color: #e0e0e0;
#             font-family: 'Segoe UI', sans-serif;
#         }
        
#         /* Modern Navbar */
#         .navbar-container {
#             display: flex;
#             flex-direction: column;
#             padding: 15px 5%;
#             margin: -1rem -1rem 30px -1rem;
#             background: linear-gradient(135deg, #0f0c29, #302b63, #24243e) !important;
#             box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
#             position: sticky;
#             top: 0;
#             z-index: 1000;
#             backdrop-filter: blur(5px);
#             border-bottom: 1px solid rgba(255, 255, 255, 0.1);
#         }
        
#         .navbar-content {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             flex-wrap: wrap;
#         }
        
#         .navbar-title {
#             font-size: 2.2rem;
#             margin: 0;
#             font-weight: 800;
#             display: flex;
#             align-items: center;
#             gap: 10px;
#             text-shadow: 0 2px 10px rgba(0,0,0,0.3);
#             background: linear-gradient(to right, #ffffff, #f9f9f9);
#             -webkit-background-clip: text;
#             background-clip: text;
#             -webkit-text-fill-color: transparent;
#             padding: 10px 0;
#             width: 100%;
#             text-align: center;
#         }
        
#         .navbar-tabs {
#             display: flex;
#             gap: 15px;
#             width: 100%;
#             justify-content: center;
#             flex-wrap: wrap;
#             margin-top: 10px;
#         }
        
#         .navbar-tab {
#             justify-content: center;
#             padding: 8px 20px;
#             color: rgba(255, 255, 255, 0.9);
#             text-decoration: none;
#             font-weight: 600;
#             transition: all 0.3s ease;
#             font-size: 1rem;
#             position: relative;
#             white-space: nowrap;
#             border-radius: 50px;
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(5px);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#         }
        
#         .navbar-tab:hover {
#             color: #000 !important;
#             background: #fdbb2d !important;
#             transform: translateY(-2px);
#             box-shadow: 0 5px 15px rgba(0,0,0,0.2);
#         }
        
#         .navbar-tab.active {
#             color: white;
#             background: rgba(255, 255, 255, 0.3);
#             font-weight: 700;
#         }
        
#         .navbar-tab.active::after {
#             content: '';
#             position: absolute;
#             bottom: -5px;
#             left: 50%;
#             transform: translateX(-50%);
#             width: 60%;
#             height: 3px;
#             background: white;
#             border-radius: 3px;
#         }
        
#         /* Hero Section */
#         .hero-section {
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#             padding: 10px 40px;
#             border-radius: 16px;
#             text-align: center;
#             margin-top: 0;
#             margin-bottom: 50px;
#             box-shadow: 0 8px 32px rgba(0,0,0,0.3);
#             position: relative;
#             overflow: hidden;
#             border: 1px solid rgba(255, 255, 255, 0.15);
#         }
        
#         .hero-content {
#             position: relative;
#             z-index: 2;
#         }
        
#         .hero-header {
#             font-size: 3.5rem;
#             font-weight: 800;
#             margin-bottom: 20px;
#             text-shadow: 0 2px 10px rgba(0,0,0,0.3);
#             background: linear-gradient(to right, #ffffff, #f9f9f9);
#             -webkit-background-clip: text;
#             background-clip: text;
#         }
        
#         .hero-subtitle {
#             font-size: 22px;
#             color: rgba(255,255,255,0.9);
#             margin-bottom: 30px;
#         }
        
#         /* Cards */
#         .custom-card {
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#             border-radius: 16px;
#             padding: 30px;
#             box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#             margin-bottom: 25px;
#             height: 100%;
#             border: 1px solid rgba(255, 255, 255, 0.2);
#         }
        
#         .custom-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 12px 28px rgba(0,0,0,0.2);
#             border-color: rgba(255, 255, 255, 0.4);
#         }
        
#         .custom-card h2 {
#             color: white;
#             margin-top: 0;
#         }
        
#         .custom-card p {
#             color: rgba(255,255,255,0.8);
#         }
        
#         .custom-card ul {
#             padding-left: 20px;
#             color: rgba(255,255,255,0.8);
#         }
        
#         /* Buttons - Updated to use #fdbb2d color */
#         .stButton>button {
#         border-radius: 50px;
#         padding: 12px 28px;
#         font-weight: 700;
#         background: rgba(255, 255, 255, 0.08) !important;
#         color: white !important;
#         border: 1px solid rgba(255, 255, 255, 0.2) !important;
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#         letter-spacing: 0.5px;
#     }
    
#     .stButton>button:hover {
#         background: #fdbb2d !important;
#         color: #000 !important;
#         transform: translateY(-2px);
#         box-shadow: 0 5px 15px rgba(0,0,0,0.2);
#     }
    
#     .stButton>button:active {
#         transform: translateY(0);
#         background: rgba(255, 255, 255, 0.05) !important;
#     }
    
#     .stButton>button::after {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -100%;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(
#             90deg,
#             transparent,
#             rgba(255, 255, 255, 0.1),
#             transparent
#         );
#         transition: 0.5s;
#     }
    
#     .stButton>button:hover::after {
#         left: 100%;
#     }
        
#         /* Form submit button specific styling */
#         .stButton>button[type="submit"] {
#             width: 100%;
#             margin-top: 10px;
#         }
        
#         /* Images */
#         .feature-img {
#             border-radius: 16px;
#             box-shadow: 0 8px 32px rgba(0,0,0,0.3);
#             transition: all 0.3s ease;
#             margin-bottom: 25px;
#             width: 100%;
#             height: 250px;
#             object-fit: cover;
#         }
        
#         .feature-img:hover {
#             transform: scale(1.02);
#         }
        
#         /* Testimonials */
#         .testimonial-card {
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#             padding: 30px;
#             border-radius: 16px;
#             box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#             margin: 25px 0;
#             border-left: 4px solid #fdbb2d;
#         }
        
#         .testimonial-text {
#             font-style: italic;
#             color: rgba(255,255,255,0.9);
#             margin-bottom: 20px;
#         }
        
#         .testimonial-author {
#             font-weight: 700;
#             color: white;
#         }
        
#         /* Feature Cards */
#         .feature-card {
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#             padding: 30px;
#             border-radius: 16px;
#             box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#             margin: 25px 0;
#             border-left: 4px solid #5f2c82;
#             transition: all 0.3s ease;
#             text-align: center;
#         }
        
#         .feature-card:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 12px 28px rgba(0,0,0,0.2);
#             border-color: rgba(255, 255, 255, 0.4);
#         }
        
#         /* Stats */
#         .stats-card {
#             background: rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#             padding: 30px;
#             border-radius: 16px;
#             text-align: center;
#             margin: 15px 0;
#             border: 1px solid rgba(255, 255, 255, 0.2);
#         }
        
#         /* Task Styles */
#         .task-container {
#             padding: 15px;
#             margin: 10px 0;
#             border-radius: 8px;
#             border: 1px solid #ddd;
#             background-color: rgba(253, 187, 45, 0.1);
#         }
#         .completed-task-container {
#             background-color: rgba(46, 204, 113, 0.1);
#         }
#         .late-task-container {
#             background-color: rgba(231, 76, 60, 0.1);
#         }
#         .submitted-task-container {
#             background-color: rgba(241, 196, 15, 0.1);
#         }
#         .pending-task-container {
#             background-color: rgba(149, 165, 166, 0.1);
#         }
#         .task-header {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             margin-bottom: 10px;
#         }
#         .task-header h4 {
#             margin: 0;
#             color: #2c3e50;
#         }
#         .task-due {
#             font-weight: bold;
#             color: #e67e22;
#         }
#         .task-status {
#             font-weight: bold;
#             margin-top: 10px;
#         }
#         .task-status.late {
#             color: #e74c3c;
#         }
#         .task-status.completed {
#             color: #2ecc71;
#         }
#         .task-status.submitted {
#             color: #f39c12;
#         }
        
#         /* Responsive */
#         @media (max-width: 768px) {
#             .navbar-container {
#                 padding: 10px;
#             }
            
#             .navbar-content {
#                 flex-direction: column;
#             }
            
#             .navbar-title {
#                 font-size: 1.8rem;
#                 padding: 5px 0;
#                 margin-bottom: 10px;
#             }
            
#             .navbar-tabs {
#                 gap: 8px;
#                 margin-top: 5px;
#             }
            
#             .navbar-tab {
#                 padding: 6px 12px;
#                 font-size: 0.85rem;
#             }
            
#             .hero-header {
#                 font-size: 2.5rem;
#             }
            
#             .hero-subtitle {
#                 font-size: 18px;
#             }
            
#             .custom-card {
#                 padding: 20px;
#             }
            
#             .feature-img {
#                 height: 200px;
#             }
            
#             /* Stack columns on mobile */
#             [data-testid="column"] {
#                 width: 100% !important;
#                 padding: 0 !important;
#                 margin-bottom: 20px;
#             }
            
#             /* Adjust typing animation container */
#             #typed-text {
#                 font-size: 1.5rem;
#                 line-height: 1.3;
#                 margin-top: -100px;
#             }
            
#             /* Adjust button sizes */
#             .stButton>button {
#                 width: 100%;
#                 margin-bottom: 10px;
#             }
            
#             /* Adjust testimonial layout */
#             .testimonial-card {
#                 margin: 10px 0;
#                 padding: 20px;
#             }
            
#             /* Make sure images don't overflow */
#             img {
#                 max-width: 100%;
#                 height: auto;
#             }
            
#             /* Adjust program cards */
#             .custom-card h2 {
#                 font-size: 1.5rem;
#             }
            
#             /* Reduce padding in about section */
#             .hero-section {
#                 padding: 20px;
#             }
#         }
#         @media (max-width: 768px) {
#             /* Navbar responsive styles */
#             .st-emotion-cache-1kyxreq {
#                 flex-direction: column !important;
#                 gap: 10px !important;
#             }
            
#             h1 {
#                 width: 100% !important;
#                 text-align: center !important;
#                 margin-bottom: 10px !important;
#                 font-size: 1.8rem !important;
#             }
            
#             .navbar-tabs {
#                 width: 100% !important;
#                 justify-content: center !important;
#                 flex-wrap: wrap !important;
#                 gap: 8px !important;
#             }
            
#             .navbar-tab {
#                 padding: 6px 12px !important;
#                 font-size: 0.85rem !important;
#             }
#         }
#         html, body, .stApp {
#             overflow-x: hidden;
#         }

#         /* Only show spacer on small screens */
#         .mobile-spacer {
#             display: none;
#         }

#         @media (max-width: 768px) {
#             .mobile-spacer {
#                 display: block;
#                 height: 0px;
#                 transition: height 0.3s ease;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)

# inject_custom_css()

# # -----------------------
# # Firebase Configuration
# # -----------------------
# FIREBASE_PROJECT_ID = "teqnitehub"
# FIREBASE_DB_URL = f"https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents"

# # -----------------------
# # Session State Initialization
# # -----------------------
# if 'users_db' not in st.session_state:
#     st.session_state.users_db = {}

# if 'logged_in_user' not in st.session_state:
#     st.session_state.logged_in_user = None

# if 'initialized' not in st.session_state:
#     # First run - fetch users and check for persisted login
#     try:
#         response = requests.get(f"{FIREBASE_DB_URL}/applications")
#         if response.status_code == 200:
#             documents = response.json().get('documents', [])
#             users_db = {}
#             for doc in documents:
#                 fields = doc.get('fields', {})
#                 email = fields.get('email', {}).get('stringValue', '').lower().strip()
#                 if email:
#                     users_db[email] = {
#                         "first_name": fields.get('first_name', {}).get('stringValue', ''),
#                         "last_name": fields.get('last_name', {}).get('stringValue', ''),
#                         "email": email,
#                         "phone": fields.get('phone', {}).get('stringValue', ''),
#                         "university": fields.get('university', {}).get('stringValue', ''),
#                         "degree": fields.get('degree', {}).get('stringValue', ''),
#                         "major": fields.get('major', {}).get('stringValue', ''),
#                         "program": fields.get('program', {}).get('stringValue', 'N/A'),
#                         "graduation_year": int(fields.get('graduation_year', {}).get('integerValue', 0)),
#                         "password": fields.get('password_hash', {}).get('stringValue', ''),
#                         "status": fields.get('status', {}).get('stringValue', 'pending'),
#                         "role": fields.get('role', {}).get('stringValue', 'student'),
#                         "total_marks": int(fields.get('total_marks', {}).get('integerValue', 0)),
#                         "tasks": [],
#                         "programming_languages": [lang['stringValue'] for lang in fields.get('programming_languages', {}).get('arrayValue', {}).get('values', [])],
#                         "project_description": fields.get('project_description', {}).get('stringValue', ''),
#                         "internship_duration": fields.get('internship_duration', {}).get('stringValue', '3 Months')
#                     }
#                     if 'tasks' in fields:
#                         tasks = fields['tasks'].get('arrayValue', {}).get('values', [])
#                         for t in tasks:
#                             task_data = {
#                                 "name": t.get('mapValue', {}).get('fields', {}).get('name', {}).get('stringValue', ''),
#                                 "description": t.get('mapValue', {}).get('fields', {}).get('description', {}).get('stringValue', ''),
#                                 "due_date": t.get('mapValue', {}).get('fields', {}).get('due_date', {}).get('stringValue', ''),
#                                 "max_marks": int(t.get('mapValue', {}).get('fields', {}).get('max_marks', {}).get('integerValue', 0)),
#                                 "assigned_date": t.get('mapValue', {}).get('fields', {}).get('assigned_date', {}).get('stringValue', ''),
#                                 "completed": t.get('mapValue', {}).get('fields', {}).get('completed', {}).get('booleanValue', False),
#                                 "submitted": t.get('mapValue', {}).get('fields', {}).get('submitted', {}).get('booleanValue', False),
#                                 "submission_date": t.get('mapValue', {}).get('fields', {}).get('submission_date', {}).get('stringValue', ''),
#                                 "marks": int(t.get('mapValue', {}).get('fields', {}).get('marks', {}).get('integerValue', 0)),
#                                 "remarks": t.get('mapValue', {}).get('fields', {}).get('remarks', {}).get('stringValue', ''),
#                                 "late": t.get('mapValue', {}).get('fields', {}).get('late', {}).get('booleanValue', False)
#                             }
#                             if 'submission_file' in t.get('mapValue', {}).get('fields', {}):
#                                 task_data["submission_file"] = t['mapValue']['fields']['submission_file']['stringValue']
#                             users_db[email]['tasks'].append(task_data)
#             st.session_state.users_db = users_db
#     except Exception as e:
#         st.error(f"Initialization error: {str(e)}")
    
#     st.session_state.initialized = True

#     # Check for persisted login from query params
#     query_params = st.query_params.to_dict()
#     if 'auth_token' in query_params:
#         try:
#             auth_token = query_params['auth_token']
#             if isinstance(auth_token, list):
#                 auth_token = auth_token[0]
#             email, token = auth_token.split('|')
#             if email in st.session_state.users_db:
#                 user = st.session_state.users_db[email]
#                 if user['password'] == token:
#                     st.session_state.logged_in_user = email
#         except Exception as e:
#             st.error(f"Login error: {str(e)}")

# # -----------------------
# # Firestore Utilities
# # -----------------------
# def update_user_in_firestore(user_data):
#     """Store application in Firestore"""
#     doc_path = f"applications/{user_data['email']}"
#     url = f"{FIREBASE_DB_URL}/{doc_path}"
    
#     # Prepare tasks for Firestore
#     tasks_data = []
#     for task in user_data.get("tasks", []):
#         task_map = {
#             "name": {"stringValue": task["name"]},
#             "description": {"stringValue": task["description"]},
#             "due_date": {"stringValue": task["due_date"]},
#             "max_marks": {"integerValue": str(task["max_marks"])},
#             "assigned_date": {"stringValue": task["assigned_date"]},
#             "completed": {"booleanValue": task["completed"]},
#             "submitted": {"booleanValue": task["submitted"]},
#             "late": {"booleanValue": task.get("late", False)},
#         }
#         if "submission_file" in task:
#             task_map["submission_file"] = {"stringValue": task["submission_file"]}
#         if "submission_date" in task:
#             task_map["submission_date"] = {"stringValue": task["submission_date"]}
#         if "marks" in task:
#             task_map["marks"] = {"integerValue": str(task["marks"])}
#         if "remarks" in task:
#             task_map["remarks"] = {"stringValue": task["remarks"]}
        
#         tasks_data.append({"mapValue": {"fields": task_map}})

#     # Prepare the base firestore data
#     firestore_data = {
#         "fields": {
#             "first_name": {"stringValue": user_data["first_name"]},
#             "last_name": {"stringValue": user_data["last_name"]},
#             "email": {"stringValue": user_data["email"]},
#             "phone": {"stringValue": user_data["phone"]},
#             "university": {"stringValue": user_data["university"]},
#             "degree": {"stringValue": user_data["degree"]},
#             "major": {"stringValue": user_data["major"]},
#             "program": {"stringValue": user_data["program"]},
#             "internship_duration": {"stringValue": user_data.get("internship_duration", "3 Months")},
#             "graduation_year": {"integerValue": str(user_data["graduation_year"])},
#             "password_hash": {"stringValue": user_data["password"]},
#             "status": {"stringValue": user_data["status"]},
#             "role": {"stringValue": user_data.get("role", "student")},
#             "total_marks": {"integerValue": str(user_data.get("total_marks", 0))},
#             "tasks": {
#                 "arrayValue": {
#                     "values": tasks_data
#                 }
#             },
#             "programming_languages": {
#                 "arrayValue": {
#                     "values": [{"stringValue": lang} for lang in user_data.get("programming_languages", [])]
#                 }
#             },
#             "project_description": {"stringValue": user_data.get("project_description", "")}
#         }
#     }

#     # Add optional fields if they exist
#     if "application_date" in user_data:
#         firestore_data["fields"]["application_date"] = {"stringValue": user_data["application_date"]}

#     response = requests.patch(url, json=firestore_data)
#     if response.status_code == 200:
#         # Refresh the users data after update
#         response = requests.get(f"{FIREBASE_DB_URL}/applications")
#         if response.status_code == 200:
#             documents = response.json().get('documents', [])
#             for doc in documents:
#                 fields = doc.get('fields', {})
#                 email = fields.get('email', {}).get('stringValue', '').lower().strip()
#                 if email in st.session_state.users_db:
#                     st.session_state.users_db[email].update({
#                         "status": fields.get('status', {}).get('stringValue', 'pending'),
#                         "total_marks": int(fields.get('total_marks', {}).get('integerValue', 0)),
#                         "tasks": [],
#                         "programming_languages": [lang['stringValue'] for lang in fields.get('programming_languages', {}).get('arrayValue', {}).get('values', [])],
#                         "project_description": fields.get('project_description', {}).get('stringValue', ''),
#                         "internship_duration": fields.get('internship_duration', {}).get('stringValue', '3 Months')
#                     })
#                     if 'tasks' in fields:
#                         tasks = fields['tasks'].get('arrayValue', {}).get('values', [])
#                         st.session_state.users_db[email]['tasks'] = []
#                         for t in tasks:
#                             task_data = {
#                                 "name": t.get('mapValue', {}).get('fields', {}).get('name', {}).get('stringValue', ''),
#                                 "description": t.get('mapValue', {}).get('fields', {}).get('description', {}).get('stringValue', ''),
#                                 "due_date": t.get('mapValue', {}).get('fields', {}).get('due_date', {}).get('stringValue', ''),
#                                 "max_marks": int(t.get('mapValue', {}).get('fields', {}).get('max_marks', {}).get('integerValue', 0)),
#                                 "assigned_date": t.get('mapValue', {}).get('fields', {}).get('assigned_date', {}).get('stringValue', ''),
#                                 "completed": t.get('mapValue', {}).get('fields', {}).get('completed', {}).get('booleanValue', False),
#                                 "submitted": t.get('mapValue', {}).get('fields', {}).get('submitted', {}).get('booleanValue', False),
#                                 "submission_date": t.get('mapValue', {}).get('fields', {}).get('submission_date', {}).get('stringValue', ''),
#                                 "marks": int(t.get('mapValue', {}).get('fields', {}).get('marks', {}).get('integerValue', 0)),
#                                 "remarks": t.get('mapValue', {}).get('fields', {}).get('remarks', {}).get('stringValue', ''),
#                                 "late": t.get('mapValue', {}).get('fields', {}).get('late', {}).get('booleanValue', False)
#                             }
#                             if 'submission_file' in t.get('mapValue', {}).get('fields', {}):
#                                 task_data["submission_file"] = t['mapValue']['fields']['submission_file']['stringValue']
#                             st.session_state.users_db[email]['tasks'].append(task_data)
#         return True
#     else:
#         st.error(f"Error updating user: {response.text}")
#         return False

# def delete_task_from_firestore(email, task_name):
#     """Delete a task from a student's record in Firestore"""
#     student = st.session_state.users_db[email]
#     student['tasks'] = [t for t in student['tasks'] if t['name'] != task_name]
#     return update_user_in_firestore(student)

# def block_student_in_firestore(email):
#     """Block a student by changing their status"""
#     student = st.session_state.users_db[email]
#     student['status'] = 'blocked'
#     return update_user_in_firestore(student)

# def unblock_student_in_firestore(email):
#     """Unblock a student by changing their status"""
#     student = st.session_state.users_db[email]
#     student['status'] = 'approved'
#     return update_user_in_firestore(student)

# def is_task_late(due_date_str):
#     """Check if task is overdue and return boolean"""
#     due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
#     return date.today() > due_date

# # -----------------------
# # Certificate Generation
# # -----------------------
# def generate_certificate(user_data, completion_date, program_duration):
#     """Generate a certificate PDF for the student"""
#     buffer = io.BytesIO()
#     c = canvas.Canvas(buffer, pagesize=letter)
    
#     # Certificate design
#     c.setFillColor(colors.darkblue)
#     c.rect(0, 0, letter[0], letter[1], fill=True, stroke=False)
    
#     # Border
#     c.setStrokeColor(colors.gold)
#     c.setLineWidth(5)
#     c.rect(0.5*inch, 0.5*inch, letter[0]-inch, letter[1]-inch, fill=False, stroke=True)
    
#     # Logo placeholder
#     try:
#         c.drawImage("logo.png", 2.5*inch, 6.5*inch, width=2*inch, height=2*inch, preserveAspectRatio=True)
#     except:
#         pass
    
#     # Title
#     c.setFillColor(colors.gold)
#     c.setFont("Helvetica-Bold", 28)
#     c.drawCentredString(letter[0]/2, 6.2*inch, "CERTIFICATE OF COMPLETION")
    
#     # Subtitle
#     c.setFont("Helvetica", 16)
#     c.drawCentredString(letter[0]/2, 5.8*inch, "This is to certify that")
    
#     # Student name
#     c.setFont("Helvetica-Bold", 24)
#     c.setFillColor(colors.white)
#     c.drawCentredString(letter[0]/2, 5.2*inch, f"{user_data['first_name']} {user_data['last_name']}")
    
#     # Program details
#     c.setFont("Helvetica", 14)
#     c.setFillColor(colors.gold)
#     c.drawCentredString(letter[0]/2, 4.8*inch, f"has successfully completed the {program_duration} program in")
#     c.setFont("Helvetica-Bold", 16)
#     c.setFillColor(colors.white)
#     c.drawCentredString(letter[0]/2, 4.5*inch, user_data.get('program', 'N/A'))
    
#     # Dates
#     c.setFont("Helvetica", 12)
#     c.setFillColor(colors.gold)
#     c.drawString(1*inch, 3.5*inch, f"Completed on: {completion_date}")
#     c.drawString(1*inch, 3.2*inch, f"University: {user_data.get('university', 'N/A')}")
    
#     # Performance summary
#     total_tasks = len(user_data.get('tasks', []))
#     completed_tasks = len([t for t in user_data.get('tasks', []) if t.get('completed')])
#     total_marks = sum(t.get('marks', 0) for t in user_data.get('tasks', []) if t.get('completed'))
#     max_possible = sum(t.get('max_marks', 0) for t in user_data.get('tasks', []))
#     percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
    
#     c.drawString(1*inch, 2.8*inch, f"Completion Rate: {completed_tasks}/{total_tasks} tasks ({percentage:.1f}%)")
    
#     # Grading
#     if percentage >= 80:
#         grade = "A1 (Excellent)"
#     elif percentage >= 70:
#         grade = "A (Very Good)"
#     elif percentage >= 60:
#         grade = "B (Good)"
#     elif percentage >= 50:
#         grade = "C (Satisfactory)"
#     else:
#         grade = "FAIL (Needs Improvement)"
    
#     c.drawString(1*inch, 2.5*inch, f"Overall Grade: {grade}")
    
#     # Verification code
#     verification_code = hashlib.sha256(f"{user_data['email']}{completion_date}".encode()).hexdigest()[:12].upper()
#     c.drawString(1*inch, 2.2*inch, f"Verification Code: {verification_code}")
    
#     # Signature lines
#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(1*inch, 1.5*inch, "_________________________")
#     c.drawString(4*inch, 1.5*inch, "_________________________")
#     c.setFont("Helvetica", 10)
#     c.drawString(1*inch, 1.3*inch, "Director, TEQNITEHUB Academy")
#     c.drawString(4*inch, 1.3*inch, "Date")
    
#     c.showPage()
#     c.save()
    
#     buffer.seek(0)
#     return buffer

# # -----------------------
# # Performance Visualization
# # -----------------------
# def plot_performance_chart(user_data):
#     """Generate performance visualization charts"""
#     if not user_data.get('tasks'):
#         return None
    
#     # Prepare data
#     tasks = user_data['tasks']
#     completed_tasks = [t for t in tasks if t.get('completed')]
#     pending_tasks = [t for t in tasks if not t.get('completed') and not t.get('submitted')]
#     submitted_tasks = [t for t in tasks if t.get('submitted') and not t.get('completed')]
    
#     # Completion chart
#     fig1, ax1 = plt.subplots(figsize=(8, 4))
#     ax1.pie(
#         [len(completed_tasks), len(submitted_tasks), len(pending_tasks)],
#         labels=['Completed', 'Submitted', 'Pending'],
#         colors=['#2ecc71', '#f39c12', '#e74c3c'],
#         autopct='%1.1f%%',
#         startangle=90
#     )
#     ax1.axis('equal')
#     ax1.set_title('Task Completion Status')
    
#     # Performance over time
#     if completed_tasks:
#         fig2, ax2 = plt.subplots(figsize=(10, 4))
#         dates = [datetime.strptime(t['submission_date'], "%Y-%m-%d") for t in completed_tasks]
#         marks = [t['marks'] for t in completed_tasks]
#         max_marks = [t['max_marks'] for t in completed_tasks]
#         percentages = [(m/mm)*100 for m, mm in zip(marks, max_marks)]
        
#         dates, marks, percentages = zip(*sorted(zip(dates, marks, percentages)))
        
#         ax2.plot(dates, percentages, marker='o', color='#3498db', label='Performance %')
#         ax2.axhline(y=50, color='r', linestyle='--', label='Passing Threshold')
#         ax2.set_ylim(0, 110)
#         ax2.set_ylabel('Performance (%)')
#         ax2.set_title('Performance Over Time')
#         ax2.legend()
#         ax2.grid(True)
#         plt.xticks(rotation=45)
        
#         return fig1, fig2
    
#     return fig1, None

# # -----------------------
# # Student Profile
# # -----------------------
# def show_user_profile(user_data):
#     """Display comprehensive user profile information"""
#     with st.expander("👤 Profile Information", expanded=True):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("### Personal Information")
#             st.write(f"**Full Name:** {user_data['first_name']} {user_data['last_name']}")
#             st.write(f"**Email:** {user_data['email']}")
#             st.write(f"**Contact:** {user_data.get('phone', 'N/A')}")
#             st.write(f"**Status:** {user_data.get('status', 'N/A').capitalize()}")
#             st.write(f"**Program Duration:** {user_data.get('internship_duration', 'N/A')}")
            
#         with col2:
#             st.markdown("### Academic Information")
#             st.write(f"**University:** {user_data.get('university', 'N/A')}")
#             st.write(f"**Degree Program:** {user_data.get('degree', 'N/A')} in {user_data.get('major', 'N/A')}")
#             st.write(f"**Graduation Year:** {user_data.get('graduation_year', 'N/A')}")
#             st.write(f"**TEQNITEHUB Program:** {user_data.get('program', 'N/A')}")
        
#         st.markdown("---")
#         st.markdown("### Skills & Technologies")
        
#         if user_data.get('programming_languages'):
#             st.write("**Programming Languages:**")
#             cols = st.columns(4)
#             for i, lang in enumerate(user_data['programming_languages']):
#                 cols[i%4].markdown(f"- {lang}")
#         else:
#             st.info("No programming languages specified")
        
#         st.markdown("---")
#         st.markdown("### About Me")
#         st.write(user_data.get('project_description', 'No description provided'))

# # -----------------------
# # Performance Report
# # -----------------------
# def show_performance_report(user_data):
#     """Display detailed performance analytics for the student"""
#     with st.expander("📊 Performance Analytics", expanded=True):
#         # Calculate metrics
#         tasks = user_data.get('tasks', [])
#         total_tasks = len(tasks)
#         completed_tasks = [t for t in tasks if t.get('completed')]
#         pending_tasks = [t for t in tasks if not t.get('completed') and not t.get('submitted')]
#         submitted_tasks = [t for t in tasks if t.get('submitted') and not t.get('completed')]
#         late_submissions = len([t for t in tasks if t.get('late', False)])
        
#         total_marks = sum(t.get('marks', 0) for t in completed_tasks)
#         max_possible = sum(t.get('max_marks', 0) for t in tasks)
#         percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
        
#         # Metrics Display
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("Overall Completion", 
#                      f"{len(completed_tasks)}/{total_tasks} tasks", 
#                      f"{len(completed_tasks)/total_tasks*100:.1f}%" if total_tasks > 0 else "0%")
#             st.metric("Total Marks Earned", 
#                      f"{total_marks}/{max_possible}", 
#                      f"{percentage:.1f}%" if max_possible > 0 else "0%")
        
#         with col2:
#             avg_score = total_marks/len(completed_tasks) if completed_tasks else 0
#             st.metric("Average Score", 
#                      f"{avg_score:.1f}" if completed_tasks else "N/A")
#             st.metric("Late Submissions", late_submissions)
        
#         with col3:
#             # Progress circle visualization
#             st.markdown(f"""
#             <div style="text-align: center;">
#                 <svg width="120" height="120">
#                     <circle cx="60" cy="60" r="50" fill="none" stroke="#ddd" stroke-width="10"/>
#                     <circle cx="60" cy="60" r="50" fill="none" stroke="#fdbb2d" stroke-width="10" 
#                         stroke-dasharray="314" stroke-dashoffset="{314 * (1 - (percentage/100 if percentage > 0 else 0))}"/>
#                     <text x="60" y="60" text-anchor="middle" dominant-baseline="middle" 
#                         font-size="20" font-weight="bold" fill="#fdbb2d">{percentage:.1f}%</text>
#                 </svg>
#                 <p style="margin-top: -10px; font-size: 14px;">Overall Performance</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         # Visualizations
#         st.markdown("### Performance Visualizations")
        
#         # Generate charts
#         fig1, fig2 = None, None
        
#         if tasks:
#             # Completion pie chart
#             fig1, ax1 = plt.subplots(figsize=(8, 4))
#             if completed_tasks or submitted_tasks or pending_tasks:
#                 sizes = [len(completed_tasks), len(submitted_tasks), len(pending_tasks)]
#                 labels = ['Completed', 'Submitted', 'Pending']
#                 colors = ['#2ecc71', '#f39c12', '#e74c3c']
                
#                 # Only show categories that have values
#                 sizes = [s for s in sizes if s > 0]
#                 labels = [l for i, l in enumerate(labels) if sizes[i] > 0] if len(sizes) == len(labels) else labels[:len(sizes)]
#                 colors = colors[:len(sizes)]
                
#                 ax1.pie(
#                     sizes,
#                     labels=labels,
#                     colors=colors,
#                     autopct='%1.1f%%',
#                     startangle=90
#                 )
#                 ax1.axis('equal')
#                 ax1.set_title('Task Completion Status')
#             else:
#                 ax1.text(0.5, 0.5, 'No task data available', 
#                         ha='center', va='center', fontsize=12)
#                 ax1.axis('off')
            
#             # Performance over time line chart
#             if completed_tasks:
#                 fig2, ax2 = plt.subplots(figsize=(10, 4))
#                 try:
#                     dates = [datetime.strptime(t['submission_date'], "%Y-%m-%d") for t in completed_tasks]
#                     marks = [t.get('marks', 0) for t in completed_tasks]
#                     max_marks = [t.get('max_marks', 1) for t in completed_tasks]
#                     percentages = [(m/mm)*100 for m, mm in zip(marks, max_marks)]
                    
#                     # Sort by date
#                     dates, percentages = zip(*sorted(zip(dates, percentages)))
                    
#                     ax2.plot(dates, percentages, marker='o', color='#3498db', label='Performance %')
#                     ax2.axhline(y=50, color='r', linestyle='--', label='Passing Threshold')
#                     ax2.set_ylim(0, 110)
#                     ax2.set_ylabel('Performance (%)')
#                     ax2.set_title('Performance Over Time')
#                     ax2.legend()
#                     ax2.grid(True)
#                     plt.xticks(rotation=45)
#                 except Exception as e:
#                     st.warning(f"Could not generate performance chart: {str(e)}")
#                     fig2 = None
        
#         # Display charts
#         if fig1:
#             st.pyplot(fig1)
#             plt.close(fig1)
#         else:
#             st.info("No task data available for visualization")
            
#         if fig2:
#             st.pyplot(fig2)
#             plt.close(fig2)
        
#         st.markdown("---")
        
#         # Task performance breakdown
#         st.markdown("### Task Performance Breakdown")
#         if tasks:
#             task_data = []
#             for task in tasks:
#                 if task.get('completed'):
#                     task_percentage = (task.get('marks', 0)/task.get('max_marks', 1))*100
#                     task_data.append({
#                         "Task": task['name'],
#                         "Status": "✅ Completed",
#                         "Marks": f"{task.get('marks', 0)}/{task['max_marks']}",
#                         "Percentage": task_percentage,
#                         "Remarks": task.get('remarks', 'N/A')
#                     })
#                 elif task.get('submitted'):
#                     task_data.append({
#                         "Task": task['name'],
#                         "Status": "📤 Submitted",
#                         "Marks": "Pending",
#                         "Percentage": None,
#                         "Remarks": "Awaiting evaluation"
#                     })
#                 else:
#                     task_data.append({
#                         "Task": task['name'],
#                         "Status": "📝 Pending",
#                         "Marks": "Not submitted",
#                         "Percentage": None,
#                         "Remarks": "Not submitted"
#                     })
            
#             # Create DataFrame for display
#             df = pd.DataFrame(task_data)
            
#             # Display with progress bars for percentages
#             st.dataframe(
#                 df,
#                 column_config={
#                     "Percentage": st.column_config.ProgressColumn(
#                         "Completion",
#                         help="Task completion percentage",
#                         format="%.1f%%",
#                         min_value=0,
#                         max_value=100,
#                     ),
#                 },
#                 hide_index=True,
#                 use_container_width=True,
#                 height=min(400, 50 * len(df) + 50)  # Dynamic height based on rows
#             )
#         else:
#             st.info("No tasks available for performance analysis")
            
#         # Grade Summary
#         st.markdown("---")
#         st.markdown("### Grade Summary")
        
#         if percentage >= 80:
#             grade = "A1 (Excellent)"
#             feedback = "Outstanding performance! You've demonstrated excellent understanding of all concepts."
#         elif percentage >= 70:
#             grade = "A (Very Good)"
#             feedback = "Strong performance! You've shown a very good grasp of the material."
#         elif percentage >= 60:
#             grade = "B (Good)"
#             feedback = "Good work! You have a solid understanding of most concepts."
#         elif percentage >= 50:
#             grade = "C (Satisfactory)"
#             feedback = "You've met the basic requirements. Consider reviewing areas of difficulty."
#         elif total_tasks > 0:
#             grade = "FAIL (Needs Improvement)"
#             feedback = "Additional work is needed to demonstrate competency. Please review the material and resubmit."
#         else:
#             grade = "N/A"
#             feedback = "No tasks have been graded yet."
        
#         st.markdown(f"**Current Grade:** {grade}")  
#         st.markdown(f"**Feedback:** {feedback}")

# # -----------------------
# # Admin Dashboard
# # -----------------------
# def display_tasks(task_list, student_email, tab_name=""):
#     student = st.session_state.users_db[student_email]
#     for task_idx, task in enumerate(task_list):
#         with st.container(border=True):
#             cols = st.columns([4, 1])
#             cols[0].markdown(f"**{task['name']}**")
            
#             # Generate unique keys including tab_name
#             edit_key = f"edit_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
#             delete_key = f"delete_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
#             editing_key = f"editing_task_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
            
#             # Editing form (only shown when editing)
#             if st.session_state.get(editing_key, False):
#                 with st.form(key=f"edit_form_{student['email']}_{task['name']}_{tab_name}_{task_idx}"):
#                     new_name = st.text_input("Task Name", value=task['name'])
#                     new_desc = st.text_area("Description", value=task['description'])
#                     new_due_date = st.date_input("Due Date", 
#                                                value=datetime.strptime(task['due_date'], "%Y-%m-%d").date())
#                     new_max_marks = st.number_input("Max Marks", 
#                                                   min_value=1, 
#                                                   value=task['max_marks'])
                    
#                     # Add field for editing obtained marks if task is completed
#                     if task.get('completed'):
#                         new_marks = st.number_input("Obtained Marks",
#                                                    min_value=0,
#                                                    max_value=task['max_marks'],  # Ensure marks don't exceed max
#                                                    value=task.get('marks', 0))
#                     else:
#                         new_marks = task.get('marks', 0)
                    
#                     col1, col2 = st.columns(2)
#                     if col1.form_submit_button("Save Changes"):
#                         # Validate marks don't exceed max marks
#                         if new_marks > new_max_marks:
#                             st.error("Obtained marks cannot exceed maximum marks!")
#                         else:
#                             task['name'] = new_name
#                             task['description'] = new_desc
#                             task['due_date'] = new_due_date.strftime("%Y-%m-%d")
#                             task['max_marks'] = new_max_marks
#                             if task.get('completed'):
#                                 task['marks'] = new_marks
                            
#                             # Recalculate total_marks
#                             student['total_marks'] = sum(
#                                 t.get('marks', 0) 
#                                 for t in student['tasks'] 
#                                 if t.get('completed')
#                             )
                            
#                             if update_user_in_firestore(student):
#                                 st.success("Task updated successfully!")
#                                 st.session_state[editing_key] = False
#                                 st.rerun()
                    
#                     if col2.form_submit_button("Cancel"):
#                         st.session_state[editing_key] = False
#                         st.rerun()

#             # Rest of the task display remains the same...
#             status = "✅ Completed" if task.get('completed') else "📝 Pending"
#             if task.get('submitted') and not task.get('completed'):
#                 status = "📤 Submitted"
            
#             cols[1].markdown(f"**Status:** {status}")
            
#             st.write(f"**Description:** {task['description']}")
#             st.write(f"**Due Date:** {task['due_date']}")
#             st.write(f"**Assigned on:** {task['assigned_date']}")
#             st.write(f"**Max Marks:** {task['max_marks']}")
            
#             if task.get('completed'):
#                 st.write(f"**Obtained Marks:** {task.get('marks', 0)}")
            
#             if task.get('submitted'):
#                 st.success("📤 Task submitted for review")
#                 st.write(f"**Submitted on:** {task['submission_date']}")
                
#                 col1, col2, col3, col4 = st.columns(4)
#                 with col1:
#                     if task.get('submission_file'):
#                         download_key = f"download_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
                        
#                         # First button to initiate download
#                         if st.button("⬇️ Download Submission", key=f"btn_{download_key}"):
#                             st.session_state[download_key] = True
                        
#                         # Actual download happens here if state is True
#                         if st.session_state.get(download_key, False):
#                             try:
#                                 file_bytes = base64.b64decode(task['submission_file'])
#                                 st.download_button(
#                                     label="⬇️ Click to Download",
#                                     data=file_bytes,
#                                     file_name=f"{student['first_name']}_{student['last_name']}_{task['name']}.zip",
#                                     mime="application/zip",
#                                     key=f"dl_{download_key}"
#                                 )
#                                 # Reset the state after download
#                                 st.session_state[download_key] = False
#                             except Exception as e:
#                                 st.error(f"Error preparing file for download: {str(e)}")
                
#                 if col3.button("✏️ Edit", key=edit_key):
#                     st.session_state[editing_key] = True
                
#                 if col4.button("🗑️ Delete", key=delete_key):
#                     if delete_task_from_firestore(student['email'], task['name']):
#                         st.success("Task deleted successfully!")
#                         st.rerun()
                
#                 if not task['completed']:
#                     grade_form_key = f"grade_form_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
#                     with st.form(key=grade_form_key):
#                         marks_key = f"marks_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
#                         marks = st.number_input(
#                             "Assign Marks",
#                             min_value=0,
#                             max_value=task['max_marks'],  # Ensure marks don't exceed max
#                             value=task.get('marks', 0),
#                             key=marks_key
#                         )
#                         remarks_key = f"remarks_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
#                         remarks = st.text_area(
#                             "Remarks",
#                             value=task.get('remarks', ''),
#                             key=remarks_key
#                         )
                        
#                         if st.form_submit_button("Grade Task"):
#                             # Validation is already handled by the number_input with max_value
#                             task['marks'] = marks
#                             task['remarks'] = remarks
#                             task['completed'] = True
                            
#                             # Recalculate total_marks
#                             student['total_marks'] = sum(
#                                 t.get('marks', 0) 
#                                 for t in student['tasks'] 
#                                 if t.get('completed')
#                             )
                            
#                             if update_user_in_firestore(student):
#                                 st.success("Task graded successfully!")
#                                 st.rerun()
#             else:
#                 st.info("Task not submitted yet")

# def show_admin_dashboard():
#     admin = st.session_state.users_db[st.session_state.logged_in_user]

#     st.markdown(f"""
#     <div class="admin-header">
#         <h1 style="color: #fdbb2d; display: flex; margin-top: -80px;">👑 Admin Dashboard</h1>
#         <p>Welcome back, {admin['first_name']} {admin['last_name']}</p>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color:#fdbb2d;">Total Students</h3>
#                 <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('role') != 'admin'])}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col2:
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color:#fdbb2d;">Pending Applications</h3>
#                 <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'pending'])}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col3:
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color:#fdbb2d;">Active Students</h3>
#                 <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'approved' and u.get('role') != 'admin'])}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col4:
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color:#fdbb2d;">Blocked Students</h3>
#                 <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'blocked'])}</p>
#             </div>
#         """, unsafe_allow_html=True)

#     # Main container for user management
#     with st.container():
#         st.markdown("## User Management")
#         tab1, tab2 = st.tabs(["Pending Approvals", "All Students"])

#         with tab1:
#             pending_users = [u for u in st.session_state.users_db.values() if u.get('status') == 'pending']
#             if not pending_users:
#                 st.info("No pending applications.")
#             else:
#                 for user in pending_users:
#                     with st.container(border=True):
#                         cols = st.columns([3, 2, 2, 2])
#                         cols[0].write(f"**{user['first_name']} {user['last_name']}** ({user['email']})")
#                         cols[1].write(user.get('program', 'N/A'))
#                         if cols[2].button("✅ Approve", key=f"approve_{user['email']}"):
#                             user['status'] = "approved"
#                             update_user_in_firestore(user)
#                             st.rerun()
#                         if cols[3].button("❌ Reject", key=f"reject_{user['email']}"):
#                             requests.delete(f"{FIREBASE_DB_URL}/applications/{user['email']}")
#                             del st.session_state.users_db[user['email']]
#                             st.rerun()

#         with tab2:
#             all_students = [u for u in st.session_state.users_db.values() if u.get('role') != 'admin']
#             if not all_students:
#                 st.info("No students registered.")
#             else:
#                 for student in all_students:
#                     with st.container(border=True):
#                         cols = st.columns([3, 1, 1, 1, 1])  # Added extra column for delete button
#                         cols[0].markdown(
#                             f"""
#                             <span style='color: #fdbb2d; font-size: 24px; font-weight: bold;'>
#                                 {student['first_name']} {student['last_name']} - {student.get('program', 'N/A')}
#                             </span>
#                             """,
#                             unsafe_allow_html=True
#                         )

#                         if cols[1].button("📊 View Details", key=f"details_{student['email']}"):
#                             st.session_state[f"show_details_{student['email']}"] = not st.session_state.get(f"show_details_{student['email']}", False)
                        
#                         if cols[2].button("📋 View Tasks", key=f"tasks_{student['email']}"):
#                             st.session_state[f"show_tasks_{student['email']}"] = not st.session_state.get(f"show_tasks_{student['email']}", False)
                        
#                         if cols[3].button(f"{'🔓 Unblock' if student.get('status') == 'blocked' else '🚫 Block'}", 
#                                          key=f"block_{student['email']}"):
#                             if student.get('status') == 'blocked':
#                                 if unblock_student_in_firestore(student['email']):
#                                     st.success("Student unblocked successfully!")
#                                     st.rerun()
#                             else:
#                                 if block_student_in_firestore(student['email']):
#                                     st.success("Student blocked successfully!")
#                                     st.rerun()
                        
#                         # Delete user button with confirmation
#                         if cols[4].button("🗑️ Delete", key=f"delete_{student['email']}"):
#                             st.session_state[f"confirm_delete_{student['email']}"] = True
                        
#                         if st.session_state.get(f"confirm_delete_{student['email']}", False):
#                             st.warning(f"Are you sure you want to permanently delete {student['first_name']} {student['last_name']}?")
#                             confirm_cols = st.columns(2)
#                             if confirm_cols[0].button("✅ Confirm Delete", key=f"confirm_delete_btn_{student['email']}"):
#                                 if delete_user_from_firestore(student['email']):
#                                     del st.session_state.users_db[student['email']]
#                                     st.success(f"User {student['email']} deleted successfully!")
#                                     st.rerun()
#                                 else:
#                                     st.error("Failed to delete user from database")
                        
#                         # Student Details Section
#                         if st.session_state.get(f"show_details_{student['email']}", False):
#                             with st.container(border=True):
#                                 st.markdown("#### Student Details")
#                                 col1, col2 = st.columns(2)
#                                 with col1:
#                                     st.write(f"**Full Name:** {student['first_name']} {student['last_name']}")
#                                     st.write(f"**Email:** {student['email']}")
#                                     st.write(f"**Contact:** {student.get('phone', 'N/A')}")
#                                     st.write(f"**Status:** {student.get('status', 'N/A').capitalize()}")
#                                     st.write(f"**Program Duration:** {student.get('internship_duration', 'N/A')}")
                                    
#                                 with col2:
#                                     st.write(f"**University:** {student.get('university', 'N/A')}")
#                                     st.write(f"**Degree Program:** {student.get('degree', 'N/A')} in {student.get('major', 'N/A')}")
#                                     st.write(f"**Graduation Year:** {student.get('graduation_year', 'N/A')}")
#                                     st.write(f"**TEQNITEHUB Program:** {student.get('program', 'N/A')}")
                                
#                                 st.markdown("---")
#                                 st.markdown("#### Skills & Technologies")
#                                 if student.get('programming_languages'):
#                                     st.write("**Programming Languages:**")
#                                     cols = st.columns(4)
#                                     for i, lang in enumerate(student['programming_languages']):
#                                         cols[i%4].markdown(f"- {lang}")
#                                 else:
#                                     st.info("No programming languages specified")
                                
#                                 st.markdown("---")
#                                 st.markdown("#### About Me")
#                                 st.write(student.get('project_description', 'No description provided'))

#                         # Task Management Section
#                         if st.session_state.get(f"show_tasks_{student['email']}", False):
#                             with st.container(border=True):
#                                 st.markdown("<h4 style='color: #fdbb2d;'>Task Management</h4>", unsafe_allow_html=True)
                                
#                                 if 'tasks' in student and student['tasks']:
#                                     completed_tasks = [t for t in student['tasks'] if t.get('completed')]
#                                     pending_tasks = [t for t in student['tasks'] if not t.get('completed') and not t.get('submitted')]
#                                     submitted_tasks = [t for t in student['tasks'] if t.get('submitted') and not t.get('completed')]
#                                     overdue_tasks = [t for t in student['tasks'] if datetime.strptime(t['due_date'], "%Y-%m-%d").date() < date.today() and not t.get('completed')]
#                                     total_marks_possible = sum(t['max_marks'] for t in student['tasks'])
#                                     marks_earned = sum(t.get('marks', 0) for t in student['tasks'] if t.get('completed'))
                                    
#                                     tab_summary, tab_all, tab_completed, tab_pending, tab_submitted, tab_overdue, tab_assign = st.tabs([
#                                         "📊 Summary",
#                                         "All Tasks", 
#                                         f"✅ Completed ({len(completed_tasks)})", 
#                                         f"📝 Pending ({len(pending_tasks)})",
#                                         f"📤 Submitted ({len(submitted_tasks)})",
#                                         f"⚠️ Overdue ({len(overdue_tasks)})",
#                                         "➕ Assign Task"
#                                     ])
                                    
#                                     with tab_summary:
#                                         st.markdown("### Task Summary")
#                                         cols = st.columns(3)
#                                         cols[0].metric("Total Tasks", len(student['tasks']))
#                                         cols[1].metric("Completed Tasks", len(completed_tasks))
#                                         cols[2].metric("Pending Tasks", len(pending_tasks))
#                                         cols[0].metric("Submitted Tasks", len(submitted_tasks))
#                                         cols[1].metric("Overdue Tasks", len(overdue_tasks))
#                                         cols[2].metric("Completion Rate", f"{len(completed_tasks)/len(student['tasks'])*100:.1f}%" if len(student['tasks']) > 0 else "0%")
                                        
#                                         st.markdown("---")
#                                         st.markdown("### Marks Summary")
#                                         cols = st.columns(2)
#                                         cols[0].metric("Total Possible Marks", total_marks_possible)
#                                         cols[1].metric("Marks Earned", marks_earned)
#                                         st.progress(marks_earned/total_marks_possible if total_marks_possible > 0 else 0)
#                                         percentage = (marks_earned/total_marks_possible)*100
#                                         st.caption(f"Percentage: {percentage:.1f}%")
                                        
#                                         if percentage >= 80:
#                                             st.caption("Grade: A1")
#                                         elif percentage >= 70:
#                                             st.caption("Grade: A")
#                                         elif percentage >= 60:
#                                             st.caption("Grade: B")
#                                         elif percentage >= 50:
#                                             st.caption("Grade: C")
#                                         else:
#                                             st.caption("Grade: FAIL")
                                    
#                                     with tab_all:
#                                         if student['tasks']:
#                                             display_tasks(student['tasks'], student['email'], "all")
#                                         else:
#                                             st.info("No tasks found in this category")
                                    
#                                     with tab_completed:
#                                         if completed_tasks:
#                                             display_tasks(completed_tasks, student['email'], "completed")
#                                         else:
#                                             st.info("No completed tasks found")
                                    
#                                     with tab_pending:
#                                         if pending_tasks:
#                                             display_tasks(pending_tasks, student['email'], "pending")
#                                         else:
#                                             st.info("No pending tasks found")
                                    
#                                     with tab_submitted:
#                                         if submitted_tasks:
#                                             display_tasks(submitted_tasks, student['email'], "submitted")
#                                         else:
#                                             st.info("No submitted tasks found")
                                    
#                                     with tab_overdue:
#                                         if overdue_tasks:
#                                             display_tasks(overdue_tasks, student['email'], "overdue")
#                                         else:
#                                             st.info("No overdue tasks found")
                                    
#                                     with tab_assign:
#                                         with st.form(key=f"assign_task_form_{student['email']}"):
#                                             st.write("**Assign New Task**")
#                                             task_name = st.text_input("Task Name", key=f"task_name_{student['email']}")
#                                             task_desc = st.text_area("Description", key=f"task_desc_{student['email']}")
#                                             due_date = st.date_input("Due Date", value=date.today(), key=f"due_date_{student['email']}")
#                                             max_marks = st.selectbox("Max Marks", [10, 20, 30, 50, 100], key=f"max_marks_{student['email']}")
                                            
#                                             if st.form_submit_button("Assign Task"):
#                                                 if task_name:
#                                                     new_task = {
#                                                         "name": task_name,
#                                                         "description": task_desc,
#                                                         "due_date": due_date.strftime("%Y-%m-%d"),
#                                                         "max_marks": max_marks,
#                                                         "assigned_date": datetime.now().strftime("%Y-%m-%d"),
#                                                         "completed": False,
#                                                         "submitted": False,
#                                                         "submission_file": "",
#                                                         "submission_date": "",
#                                                         "marks": 0,
#                                                         "remarks": "",
#                                                         "late": False
#                                                     }
#                                                     if 'tasks' not in student:
#                                                         student['tasks'] = []
#                                                     student['tasks'].append(new_task)
#                                                     if update_user_in_firestore(student):
#                                                         st.success(f"Task '{task_name}' assigned to {student['first_name']} {student['last_name']}.")
#                                                         st.rerun()
#                                                     else:
#                                                         st.error("Failed to assign task")
#                                                 else:
#                                                     st.warning("Please enter a task name")
#                                 else:
#                                     with st.form(key=f"assign_task_form_{student['email']}"):
#                                         st.write("**Assign New Task**")
#                                         task_name = st.text_input("Task Name", key=f"task_name_{student['email']}")
#                                         task_desc = st.text_area("Description", key=f"task_desc_{student['email']}")
#                                         due_date = st.date_input("Due Date", value=date.today(), key=f"due_date_{student['email']}")
#                                         max_marks = st.selectbox("Max Marks", [10, 20, 30, 50, 100], key=f"max_marks_{student['email']}")
                                        
#                                         if st.form_submit_button("Assign Task"):
#                                             if task_name:
#                                                 new_task = {
#                                                     "name": task_name,
#                                                     "description": task_desc,
#                                                     "due_date": due_date.strftime("%Y-%m-%d"),
#                                                     "max_marks": max_marks,
#                                                     "assigned_date": datetime.now().strftime("%Y-%m-%d"),
#                                                     "completed": False,
#                                                     "submitted": False,
#                                                     "submission_file": "",
#                                                     "submission_date": "",
#                                                     "marks": 0,
#                                                     "remarks": "",
#                                                     "late": False
#                                                 }
#                                                 if 'tasks' not in student:
#                                                     student['tasks'] = []
#                                                 student['tasks'].append(new_task)
#                                                 if update_user_in_firestore(student):
#                                                     st.success(f"Task '{task_name}' assigned to {student['first_name']} {student['last_name']}.")
#                                                     st.rerun()
#                                                 else:
#                                                     st.error("Failed to assign task")
#                                     st.info("No tasks assigned to this student")
                                    
                                    
# def delete_user_from_firestore(email):
#     """Delete a user from Firestore"""
#     try:
#         doc_path = f"applications/{email}"
#         url = f"{FIREBASE_DB_URL}/{doc_path}"
        
#         response = requests.delete(url)
#         return response.status_code == 200
#     except Exception as e:
#         st.error(f"Error deleting user: {str(e)}")
#         return False
    
# # -----------------------
# # User Dashboard
# # -----------------------
# def show_user_dashboard():
#     user = st.session_state.users_db[st.session_state.logged_in_user]
    
#     st.markdown(f"""
#         <div class="user-header">
#             <h1 style="color: #fdbb2d; display: flex; margin-top: -80px;" >👤 Student Dashboard</h1>
#             <p>Welcome back, {user['first_name']} {user['last_name']}</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # Quick stats cards
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         completed_tasks = len([t for t in user.get('tasks', []) if t.get('completed')])
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color: #fdbb2d;" >Completed Tasks</h3>
#                 <p style="font-size:2rem;">{completed_tasks}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col2:
#         pending_tasks = len([t for t in user.get('tasks', []) if not t.get('completed')])
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color: #fdbb2d;" >Pending Tasks</h3>
#                 <p style="font-size:2rem;">{pending_tasks}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col3:
#         total_marks = user.get('total_marks', 0)
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color: #fdbb2d;" >Total Marks</h3>
#                 <p style="font-size:2rem;">{total_marks}</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with col4:
#         max_possible = sum(t.get('max_marks', 0) for t in user.get('tasks', []))
#         percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
#         st.markdown(f"""
#             <div class="stats-card">
#                 <h3 style="color: #fdbb2d;" >Overall Grade</h3>
#                 <p style="font-size:2rem;">{percentage:.1f}%</p>
#             </div>
#         """, unsafe_allow_html=True)

#     # Main content tabs
#     tab1, tab2, tab3, tab4 = st.tabs(["📋 Tasks", "📊 Performance", "🏆 Certificates", "👤 Profile"])
    
#     with tab1:
#         st.markdown("### Your Tasks")
#         if 'tasks' not in user or not user['tasks']:
#             st.info("You have no tasks assigned.")
#         else:
#             for task_idx, task in enumerate(user['tasks']):
#                 with st.expander(f"Task {task_idx + 1}: {task['name']}"):
#                     container_class = "task-container "
#                     if task.get('completed'):
#                         container_class += "completed-task-container"
#                     elif is_task_late(task['due_date']):
#                         container_class += "late-task-container"
#                         task['late'] = True
#                     elif task.get('submitted'):
#                         container_class += "submitted-task-container"
#                     else:
#                         container_class += "pending-task-container"

#                     st.markdown(f"""
#                     <div class="{container_class}">
#                         <div class="task-header">
#                             <h4 style='color: #fdbb2d;'>{task['name']}</h4>
#                             <span class="task-due">Due: {task['due_date']}</span>
#                         </div>
#                         <div class="task-content">
#                             <p><strong>Description:</strong> {task['description']}</p>
#                             <p><strong>Max Marks:</strong> {task['max_marks']}</p>
#                             <p><strong>Assigned on:</strong> {task['assigned_date']}</p>
#                     """, unsafe_allow_html=True)

#                     if task.get('late'):
#                         st.markdown('<p class="task-status late">⚠️ This task is overdue!</p>', unsafe_allow_html=True)

#                     if not task['completed']:
#                         if task.get('submitted'):
#                             st.markdown('<p class="task-status submitted">📤 Task submitted - awaiting review</p>', unsafe_allow_html=True)
#                             st.write(f"**Submitted on:** {task['submission_date']}")
#                             if task.get('submission_file'):
#                                 download_key = f"download_my_{task_idx}"
                                
#                                 # First button to initiate download
#                                 if st.button("⬇️ Download My Submission", key=f"btn_{download_key}"):
#                                     st.session_state[download_key] = True
                                
#                                 # Actual download happens here if state is True
#                                 if st.session_state.get(download_key, False):
#                                     try:
#                                         file_bytes = base64.b64decode(task['submission_file'])
#                                         st.download_button(
#                                             label="⬇️ Click to Download",
#                                             data=file_bytes,
#                                             file_name=f"my_submission_{task['name']}.zip",
#                                             mime="application/zip",
#                                             key=f"dl_{download_key}"
#                                         )
#                                         # Reset the state after download
#                                         st.session_state[download_key] = False
#                                     except Exception as e:
#                                         st.error(f"Error preparing file for download: {str(e)}")
#                         else:
#                             st.markdown("### Submit Task")
#                             uploaded_file = st.file_uploader(
#                                 "Upload your solution (.zip)", 
#                                 type=["zip"],
#                                 key=f"upload_{task_idx}"
#                             )
                            
#                             if uploaded_file is not None:
#                                 if st.button(f"Submit Task {task_idx + 1}", key=f"submit_{task_idx}"):
#                                     try:
#                                         with zipfile.ZipFile(io.BytesIO(uploaded_file.read())) as test_zip:
#                                             if test_zip.testzip() is None:
#                                                 uploaded_file.seek(0)
#                                                 file_content = uploaded_file.read()
#                                                 task['submission_file'] = base64.b64encode(file_content).decode('utf-8')
#                                                 task['submission_date'] = datetime.now().strftime("%Y-%m-%d")
#                                                 task['submitted'] = True
#                                                 if update_user_in_firestore(user):
#                                                     st.success("Task submitted successfully!")
#                                                     st.rerun()
#                                                 else:
#                                                     st.error("Failed to submit task")
#                                             else:
#                                                 st.error("Invalid ZIP file - corrupted or empty")
#                                     except zipfile.BadZipFile:
#                                         st.error("Invalid file format - please upload a valid ZIP file")
#                                     except Exception as e:
#                                         st.error(f"Error processing file: {str(e)}")
#                     else:
#                         st.markdown('<p class="task-status completed">✅ Task Completed</p>', unsafe_allow_html=True)
#                         if task.get('marks') is not None:
#                             st.write(f"**Marks Obtained:** {task['marks']}/{task['max_marks']}")
#                             st.write(f"**Remarks:** {task.get('remarks', 'No remarks')}")
#                         if task.get('submission_file'):
#                             download_key = f"download_completed_{task_idx}"
                            
#                             # First button to initiate download
#                             if st.button("⬇️ Download My Submission", key=f"btn_{download_key}"):
#                                 st.session_state[download_key] = True
                            
#                             # Actual download happens here if state is True
#                             if st.session_state.get(download_key, False):
#                                 try:
#                                     file_bytes = base64.b64decode(task['submission_file'])
#                                     st.download_button(
#                                         label="⬇️ Click to Download",
#                                         data=file_bytes,
#                                         file_name=f"my_submission_{task['name']}.zip",
#                                         mime="application/zip",
#                                         key=f"dl_{download_key}"
#                                     )
#                                     # Reset the state after download
#                                     st.session_state[download_key] = False
#                                 except Exception as e:
#                                     st.error(f"Error preparing file for download: {str(e)}")

#                     st.markdown("</div></div>", unsafe_allow_html=True)
#                     st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)
    
#     with tab2:
#         show_performance_report(user)
    
#     with tab3:
#         st.markdown("### Your Certificates")
        
#         # Check if student has completed all tasks and internship duration is over
#         total_tasks = len(user.get('tasks', []))
#         completed_tasks = len([t for t in user.get('tasks', []) if t.get('completed')])
        
#         # Get internship duration (assuming format like "3 Months" or "6 Months")
#         internship_duration = user.get('internship_duration', '3 Months')
#         duration_months = int(internship_duration.split()[0])
        
#         # Calculate end date (assuming assigned_date is when internship started)
#         if user.get('tasks'):
#             assigned_date = min(
#                 datetime.strptime(t['assigned_date'], "%Y-%m-%d") 
#                 for t in user['tasks']
#             )
#             end_date = assigned_date + timedelta(days=duration_months*30)
#             is_internship_completed = date.today() >= end_date.date()
#         else:
#             is_internship_completed = False
        
#         if total_tasks > 0 and completed_tasks == total_tasks and is_internship_completed:
#             st.success("🎉 Congratulations! You've successfully completed your TEQNITEHUB internship program!")
            
#             # Generate certificate
#             completion_date = datetime.now().strftime("%B %d, %Y")
#             program_duration = user.get('internship_duration', '3 Months')
            
#             certificate_pdf = generate_certificate(user, completion_date, program_duration)
            
#             # Certificate download with two-step process
#             cert_download_key = "certificate_download_trigger"
            
#             # First button to initiate download
#             if st.button("📄 Download Completion Certificate", key=f"btn_{cert_download_key}"):
#                 st.session_state[cert_download_key] = True
            
#             # Actual download happens here if state is True
#             if st.session_state.get(cert_download_key, False):
#                 st.download_button(
#                     label="📄 Click to Download Certificate",
#                     data=certificate_pdf,
#                     file_name=f"TEQNITEHUB_Certificate_{user['first_name']}_{user['last_name']}.pdf",
#                     mime="application/pdf",
#                     key="certificate_download"
#                 )
#                 # Reset the state after download
#                 st.session_state[cert_download_key] = False
            
#             st.markdown("---")
#             st.markdown("#### Certificate Verification")
#             st.info("Your certificate includes a unique verification code that can be used to validate its authenticity.")
#         else:
#             # Show progress status
#             if total_tasks == 0:
#                 st.warning("You don't have any tasks assigned yet.")
#             else:
#                 progress = completed_tasks / total_tasks
#                 st.warning(f"""
#                 🔍 Your internship progress:
#                 - Completed {completed_tasks} out of {total_tasks} tasks ({progress:.0%})
#                 - Internship duration: {user.get('internship_duration', 'N/A')}
#                 """)
                
#                 # Progress bar
#                 st.progress(progress)
                
#                 # Specific feedback
#                 if completed_tasks < total_tasks:
#                     st.error("You need to complete all assigned tasks to earn your certificate.")
#                 elif not is_internship_completed:
#                     if user.get('tasks'):
#                         assigned_date = min(
#                             datetime.strptime(t['assigned_date'], "%Y-%m-%d") 
#                             for t in user['tasks']
#                         )
#                         days_remaining = (end_date.date() - date.today()).days
#                         if days_remaining > 0:
#                             st.info(f"Your internship will be completed in {days_remaining} days on {end_date.strftime('%B %d, %Y')}")
#                         else:
#                             st.info("Your internship period is complete! Please wait for final review.")
#                     else:
#                         st.info("Your internship period is not yet complete.")
                
#                 st.markdown("---")
#                 st.markdown("#### Certificate Requirements")
#                 st.write("To earn your TEQNITEHUB certificate, you must:")
#                 st.write("- Complete all assigned tasks")
#                 st.write("- Complete the full internship duration")
#                 st.write("- Achieve a passing grade (50% or higher)")
                
#     with tab4:
#         show_user_profile(user)

# # -----------------------
# # Login Page
# # -----------------------
# def show_login():
#     st.markdown("""
#         <h1 style="text-align: center; color: #fdbb2d; font-family: 'Helvetica Neue'; font-weight: bold;">
#             🎓 TEQNITEHUB LMS Portal
#         </h1>
#     """, unsafe_allow_html=True)

#     with st.form("login_form"):
#         st.markdown("""
#         <style>
#         div[data-testid="stForm"] {
#             background: rgba(255, 255, 255, 0.05);
#             border-radius: 15px;
#             padding: 30px;
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
#         }
#         .form-section {
#             margin-bottom: 25px;
#         }
#         .section-title {
#             color: #fdbb2d;
#             font-size: 18px;
#             font-weight: 600;
#             margin: 20px 0 10px 0;
#             padding-bottom: 5px;
#             border-bottom: 1px solid rgba(75, 139, 255, 0.3);
#         }
#         </style>
#         """, unsafe_allow_html=True)
#         email = st.text_input("Email")
#         password = st.text_input("Password", type="password")

#         if st.form_submit_button("Login"):
#             if email in st.session_state.users_db:
#                 user = st.session_state.users_db[email]
#                 hashed_password = hashlib.sha256(password.encode()).hexdigest()
#                 if user["password"] == hashed_password:
#                     if user.get("status") == "approved":
#                         st.session_state.logged_in_user = email
#                         st.query_params["auth_token"] = f"{email}|{hashed_password}"
#                         if user.get("role") == "admin":
#                             st.success("Admin login successful!")
#                         else:
#                             st.success("Student login successful!")
#                         st.rerun()
#                     elif user.get("status") == "blocked":
#                         st.error("Your account has been blocked. Please contact the administrator.")
#                     else:
#                         st.error("Your application is pending approval.")
#                 else:
#                     st.error("Invalid password.")
#             else:
#                 st.error("Account not found.")
                
#     if st.button("Back To Home"):
#         st.switch_page("app.py")

# # -----------------------
# # Main App Logic
# # -----------------------
# if st.session_state.logged_in_user:
#     user = st.session_state.users_db[st.session_state.logged_in_user]
#     if user.get("role") == "admin":
#         show_admin_dashboard()
#     else:
#         show_user_dashboard()

#     if st.button("Logout", key="logout_btn"):
#         st.session_state.logged_in_user = None
#         st.query_params.clear()
#         st.rerun()
# else:
#     show_login()



import streamlit as st
import hashlib
from reportlab.lib.units import inch
from datetime import datetime, date, timedelta
import requests
import json
import io
import zipfile
import base64
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -----------------------
# Streamlit Config (MUST BE FIRST)
# -----------------------
st.set_page_config(
    page_title="TEQNITEHUB LMS Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
        
        /* Task Styles */
        .task-container {
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ddd;
            background-color: rgba(253, 187, 45, 0.1);
        }
        .completed-task-container {
            background-color: rgba(46, 204, 113, 0.1);
        }
        .late-task-container {
            background-color: rgba(231, 76, 60, 0.1);
        }
        .submitted-task-container {
            background-color: rgba(241, 196, 15, 0.1);
        }
        .pending-task-container {
            background-color: rgba(149, 165, 166, 0.1);
        }
        .task-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .task-header h4 {
            margin: 0;
            color: #2c3e50;
        }
        .task-due {
            font-weight: bold;
            color: #e67e22;
        }
        .task-status {
            font-weight: bold;
            margin-top: 10px;
        }
        .task-status.late {
            color: #e74c3c;
        }
        .task-status.completed {
            color: #2ecc71;
        }
        .task-status.submitted {
            color: #f39c12;
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
                height: 0px;
                transition: height 0.3s ease;
            }
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# -----------------------
# Firebase Configuration
# -----------------------
FIREBASE_PROJECT_ID = "teqnitehub"
FIREBASE_DB_URL = f"https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents"

# -----------------------
# Session State Initialization
# -----------------------
if 'users_db' not in st.session_state:
    st.session_state.users_db = {}

if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

if 'initialized' not in st.session_state:
    # First run - fetch users and check for persisted login
    try:
        response = requests.get(f"{FIREBASE_DB_URL}/applications")
        if response.status_code == 200:
            documents = response.json().get('documents', [])
            users_db = {}
            for doc in documents:
                fields = doc.get('fields', {})
                email = fields.get('email', {}).get('stringValue', '').lower().strip()
                if email:
                    users_db[email] = {
                        "first_name": fields.get('first_name', {}).get('stringValue', ''),
                        "last_name": fields.get('last_name', {}).get('stringValue', ''),
                        "email": email,
                        "phone": fields.get('phone', {}).get('stringValue', ''),
                        "university": fields.get('university', {}).get('stringValue', ''),
                        "degree": fields.get('degree', {}).get('stringValue', ''),
                        "major": fields.get('major', {}).get('stringValue', ''),
                        "program": fields.get('program', {}).get('stringValue', 'N/A'),
                        "graduation_year": int(fields.get('graduation_year', {}).get('integerValue', 0)),
                        "password": fields.get('password_hash', {}).get('stringValue', ''),
                        "status": fields.get('status', {}).get('stringValue', 'pending'),
                        "role": fields.get('role', {}).get('stringValue', 'student'),
                        "total_marks": int(fields.get('total_marks', {}).get('integerValue', 0)),
                        "tasks": [],
                        "programming_languages": [lang['stringValue'] for lang in fields.get('programming_languages', {}).get('arrayValue', {}).get('values', [])],
                        "project_description": fields.get('project_description', {}).get('stringValue', ''),
                        "internship_duration": fields.get('internship_duration', {}).get('stringValue', '3 Months')
                    }
                    if 'tasks' in fields:
                        tasks = fields['tasks'].get('arrayValue', {}).get('values', [])
                        for t in tasks:
                            task_data = {
                                "name": t.get('mapValue', {}).get('fields', {}).get('name', {}).get('stringValue', ''),
                                "description": t.get('mapValue', {}).get('fields', {}).get('description', {}).get('stringValue', ''),
                                "due_date": t.get('mapValue', {}).get('fields', {}).get('due_date', {}).get('stringValue', ''),
                                "max_marks": int(t.get('mapValue', {}).get('fields', {}).get('max_marks', {}).get('integerValue', 0)),
                                "assigned_date": t.get('mapValue', {}).get('fields', {}).get('assigned_date', {}).get('stringValue', ''),
                                "completed": t.get('mapValue', {}).get('fields', {}).get('completed', {}).get('booleanValue', False),
                                "submitted": t.get('mapValue', {}).get('fields', {}).get('submitted', {}).get('booleanValue', False),
                                "submission_date": t.get('mapValue', {}).get('fields', {}).get('submission_date', {}).get('stringValue', ''),
                                "marks": int(t.get('mapValue', {}).get('fields', {}).get('marks', {}).get('integerValue', 0)),
                                "remarks": t.get('mapValue', {}).get('fields', {}).get('remarks', {}).get('stringValue', ''),
                                "late": t.get('mapValue', {}).get('fields', {}).get('late', {}).get('booleanValue', False)
                            }
                            if 'submission_file' in t.get('mapValue', {}).get('fields', {}):
                                task_data["submission_file"] = t['mapValue']['fields']['submission_file']['stringValue']
                            users_db[email]['tasks'].append(task_data)
            st.session_state.users_db = users_db
    except Exception as e:
        st.error(f"Initialization error: {str(e)}")
    
    st.session_state.initialized = True

    # Check for persisted login from query params
    query_params = st.query_params.to_dict()
    if 'auth_token' in query_params:
        try:
            auth_token = query_params['auth_token']
            if isinstance(auth_token, list):
                auth_token = auth_token[0]
            email, token = auth_token.split('|')
            if email in st.session_state.users_db:
                user = st.session_state.users_db[email]
                if user['password'] == token:
                    st.session_state.logged_in_user = email
        except Exception as e:
            st.error(f"Login error: {str(e)}")

# -----------------------
# Firestore Utilities
# -----------------------
def update_user_in_firestore(user_data):
    """Store application in Firestore"""
    doc_path = f"applications/{user_data['email']}"
    url = f"{FIREBASE_DB_URL}/{doc_path}"
    
    # Prepare tasks for Firestore
    tasks_data = []
    for task in user_data.get("tasks", []):
        task_map = {
            "name": {"stringValue": task["name"]},
            "description": {"stringValue": task["description"]},
            "due_date": {"stringValue": task["due_date"]},
            "max_marks": {"integerValue": str(task["max_marks"])},
            "assigned_date": {"stringValue": task["assigned_date"]},
            "completed": {"booleanValue": task["completed"]},
            "submitted": {"booleanValue": task["submitted"]},
            "late": {"booleanValue": task.get("late", False)},
        }
        if "submission_file" in task:
            task_map["submission_file"] = {"stringValue": task["submission_file"]}
        if "submission_date" in task:
            task_map["submission_date"] = {"stringValue": task["submission_date"]}
        if "marks" in task:
            task_map["marks"] = {"integerValue": str(task["marks"])}
        if "remarks" in task:
            task_map["remarks"] = {"stringValue": task["remarks"]}
        
        tasks_data.append({"mapValue": {"fields": task_map}})

    # Prepare the base firestore data
    firestore_data = {
        "fields": {
            "first_name": {"stringValue": user_data["first_name"]},
            "last_name": {"stringValue": user_data["last_name"]},
            "email": {"stringValue": user_data["email"]},
            "phone": {"stringValue": user_data["phone"]},
            "university": {"stringValue": user_data["university"]},
            "degree": {"stringValue": user_data["degree"]},
            "major": {"stringValue": user_data["major"]},
            "program": {"stringValue": user_data["program"]},
            "internship_duration": {"stringValue": user_data.get("internship_duration", "3 Months")},
            "graduation_year": {"integerValue": str(user_data["graduation_year"])},
            "password_hash": {"stringValue": user_data["password"]},
            "status": {"stringValue": user_data["status"]},
            "role": {"stringValue": user_data.get("role", "student")},
            "total_marks": {"integerValue": str(user_data.get("total_marks", 0))},
            "tasks": {
                "arrayValue": {
                    "values": tasks_data
                }
            },
            "programming_languages": {
                "arrayValue": {
                    "values": [{"stringValue": lang} for lang in user_data.get("programming_languages", [])]
                }
            },
            "project_description": {"stringValue": user_data.get("project_description", "")}
        }
    }

    # Add optional fields if they exist
    if "application_date" in user_data:
        firestore_data["fields"]["application_date"] = {"stringValue": user_data["application_date"]}

    response = requests.patch(url, json=firestore_data)
    if response.status_code == 200:
        # Refresh the users data after update
        response = requests.get(f"{FIREBASE_DB_URL}/applications")
        if response.status_code == 200:
            documents = response.json().get('documents', [])
            for doc in documents:
                fields = doc.get('fields', {})
                email = fields.get('email', {}).get('stringValue', '').lower().strip()
                if email in st.session_state.users_db:
                    st.session_state.users_db[email].update({
                        "status": fields.get('status', {}).get('stringValue', 'pending'),
                        "total_marks": int(fields.get('total_marks', {}).get('integerValue', 0)),
                        "tasks": [],
                        "programming_languages": [lang['stringValue'] for lang in fields.get('programming_languages', {}).get('arrayValue', {}).get('values', [])],
                        "project_description": fields.get('project_description', {}).get('stringValue', ''),
                        "internship_duration": fields.get('internship_duration', {}).get('stringValue', '3 Months')
                    })
                    if 'tasks' in fields:
                        tasks = fields['tasks'].get('arrayValue', {}).get('values', [])
                        st.session_state.users_db[email]['tasks'] = []
                        for t in tasks:
                            task_data = {
                                "name": t.get('mapValue', {}).get('fields', {}).get('name', {}).get('stringValue', ''),
                                "description": t.get('mapValue', {}).get('fields', {}).get('description', {}).get('stringValue', ''),
                                "due_date": t.get('mapValue', {}).get('fields', {}).get('due_date', {}).get('stringValue', ''),
                                "max_marks": int(t.get('mapValue', {}).get('fields', {}).get('max_marks', {}).get('integerValue', 0)),
                                "assigned_date": t.get('mapValue', {}).get('fields', {}).get('assigned_date', {}).get('stringValue', ''),
                                "completed": t.get('mapValue', {}).get('fields', {}).get('completed', {}).get('booleanValue', False),
                                "submitted": t.get('mapValue', {}).get('fields', {}).get('submitted', {}).get('booleanValue', False),
                                "submission_date": t.get('mapValue', {}).get('fields', {}).get('submission_date', {}).get('stringValue', ''),
                                "marks": int(t.get('mapValue', {}).get('fields', {}).get('marks', {}).get('integerValue', 0)),
                                "remarks": t.get('mapValue', {}).get('fields', {}).get('remarks', {}).get('stringValue', ''),
                                "late": t.get('mapValue', {}).get('fields', {}).get('late', {}).get('booleanValue', False)
                            }
                            if 'submission_file' in t.get('mapValue', {}).get('fields', {}):
                                task_data["submission_file"] = t['mapValue']['fields']['submission_file']['stringValue']
                            st.session_state.users_db[email]['tasks'].append(task_data)
        return True
    else:
        st.error(f"Error updating user: {response.text}")
        return False

def delete_task_from_firestore(email, task_name):
    """Delete a task from a student's record in Firestore"""
    student = st.session_state.users_db[email]
    student['tasks'] = [t for t in student['tasks'] if t['name'] != task_name]
    
    # Recalculate total marks after deletion
    student['total_marks'] = sum(
        t.get('marks', 0) 
        for t in student['tasks'] 
        if t.get('completed')
    )
    
    return update_user_in_firestore(student)

def block_student_in_firestore(email):
    """Block a student by changing their status"""
    student = st.session_state.users_db[email]
    student['status'] = 'blocked'
    return update_user_in_firestore(student)

def unblock_student_in_firestore(email):
    """Unblock a student by changing their status"""
    student = st.session_state.users_db[email]
    student['status'] = 'approved'
    return update_user_in_firestore(student)

def is_task_late(due_date_str):
    """Check if task is overdue and return boolean"""
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    return date.today() > due_date

# -----------------------
# Certificate Generation
# -----------------------
def generate_certificate(user_data, completion_date, program_duration):
    """Generate a certificate PDF for the student"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(8.5*inch, 11*inch))
    
    # Certificate design
    c.setFillColor(colors.darkblue)
    c.rect(0, 0, 8.5*inch, 11*inch, fill=True, stroke=False)
    
    # Border
    c.setStrokeColor(colors.gold)
    c.setLineWidth(5)
    c.rect(0.5*inch, 0.5*inch, 7.5*inch, 10*inch, fill=False, stroke=True)
    
    # Logo placeholder
    try:
        c.drawImage("logo.png", 2.5*inch, 6.5*inch, width=2*inch, height=2*inch, preserveAspectRatio=True)
    except:
        pass
    
    # Title
    c.setFillColor(colors.gold)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(4.25*inch, 6.2*inch, "CERTIFICATE OF COMPLETION")
    
    # Subtitle
    c.setFont("Helvetica", 16)
    c.drawCentredString(4.25*inch, 5.8*inch, "This is to certify that")
    
    # Student name
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.white)
    c.drawCentredString(4.25*inch, 5.2*inch, f"{user_data['first_name']} {user_data['last_name']}")
    
    # Program details
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.gold)
    c.drawCentredString(4.25*inch, 4.8*inch, f"has successfully completed the {program_duration} program in")
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.white)
    c.drawCentredString(4.25*inch, 4.5*inch, user_data.get('program', 'N/A'))
    
    # Dates
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.gold)
    c.drawString(1*inch, 3.5*inch, f"Completed on: {completion_date}")
    c.drawString(1*inch, 3.2*inch, f"University: {user_data.get('university', 'N/A')}")
    
    # Performance summary
    total_tasks = len(user_data.get('tasks', []))
    completed_tasks = len([t for t in user_data.get('tasks', []) if t.get('completed')])
    total_marks = sum(t.get('marks', 0) for t in user_data.get('tasks', []) if t.get('completed'))
    max_possible = sum(t.get('max_marks', 0) for t in user_data.get('tasks', []))
    percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
    
    c.drawString(1*inch, 2.8*inch, f"Completion Rate: {completed_tasks}/{total_tasks} tasks ({percentage:.1f}%)")
    
    # Grading
    if percentage >= 80:
        grade = "A1 (Excellent)"
    elif percentage >= 70:
        grade = "A (Very Good)"
    elif percentage >= 60:
        grade = "B (Good)"
    elif percentage >= 50:
        grade = "C (Satisfactory)"
    else:
        grade = "FAIL (Needs Improvement)"
    
    c.drawString(1*inch, 2.5*inch, f"Overall Grade: {grade}")
    
    # Verification code
    verification_code = hashlib.sha256(f"{user_data['email']}{completion_date}".encode()).hexdigest()[:12].upper()
    c.drawString(1*inch, 2.2*inch, f"Verification Code: {verification_code}")
    
    # Signature lines
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, 1.5*inch, "_________________________")
    c.drawString(4*inch, 1.5*inch, "_________________________")
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 1.3*inch, "Director, TEQNITEHUB Academy")
    c.drawString(4*inch, 1.3*inch, "Date")
    
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer

# -----------------------
# Performance Visualization
# -----------------------
def plot_performance_chart(user_data):
    """Generate performance visualization charts"""
    if not user_data.get('tasks'):
        return None
    
    # Prepare data
    tasks = user_data['tasks']
    completed_tasks = [t for t in tasks if t.get('completed')]
    pending_tasks = [t for t in tasks if not t.get('completed') and not t.get('submitted')]
    submitted_tasks = [t for t in tasks if t.get('submitted') and not t.get('completed')]
    
    # Completion chart
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.pie(
        [len(completed_tasks), len(submitted_tasks), len(pending_tasks)],
        labels=['Completed', 'Submitted', 'Pending'],
        colors=['#2ecc71', '#f39c12', '#e74c3c'],
        autopct='%1.1f%%',
        startangle=90
    )
    ax1.axis('equal')
    ax1.set_title('Task Completion Status')
    
    # Performance over time
    if completed_tasks:
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        dates = [datetime.strptime(t['submission_date'], "%Y-%m-%d") for t in completed_tasks]
        marks = [t['marks'] for t in completed_tasks]
        max_marks = [t['max_marks'] for t in completed_tasks]
        percentages = [(m/mm)*100 for m, mm in zip(marks, max_marks)]
        
        dates, marks, percentages = zip(*sorted(zip(dates, marks, percentages)))
        
        ax2.plot(dates, percentages, marker='o', color='#3498db', label='Performance %')
        ax2.axhline(y=50, color='r', linestyle='--', label='Passing Threshold')
        ax2.set_ylim(0, 110)
        ax2.set_ylabel('Performance (%)')
        ax2.set_title('Performance Over Time')
        ax2.legend()
        ax2.grid(True)
        plt.xticks(rotation=45)
        
        return fig1, fig2
    
    return fig1, None

# -----------------------
# Student Profile
# -----------------------
def show_user_profile(user_data):
    """Display comprehensive user profile information"""
    with st.expander("👤 Profile Information", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Personal Information")
            st.write(f"**Full Name:** {user_data['first_name']} {user_data['last_name']}")
            st.write(f"**Email:** {user_data['email']}")
            st.write(f"**Contact:** {user_data.get('phone', 'N/A')}")
            st.write(f"**Status:** {user_data.get('status', 'N/A').capitalize()}")
            st.write(f"**Program Duration:** {user_data.get('internship_duration', 'N/A')}")
            
        with col2:
            st.markdown("### Academic Information")
            st.write(f"**University:** {user_data.get('university', 'N/A')}")
            st.write(f"**Degree Program:** {user_data.get('degree', 'N/A')} in {user_data.get('major', 'N/A')}")
            st.write(f"**Graduation Year:** {user_data.get('graduation_year', 'N/A')}")
            st.write(f"**TEQNITEHUB Program:** {user_data.get('program', 'N/A')}")
        
        st.markdown("---")
        st.markdown("### Skills & Technologies")
        
        if user_data.get('programming_languages'):
            st.write("**Programming Languages:**")
            cols = st.columns(4)
            for i, lang in enumerate(user_data['programming_languages']):
                cols[i%4].markdown(f"- {lang}")
        else:
            st.info("No programming languages specified")
        
        st.markdown("---")
        st.markdown("### About Me")
        st.write(user_data.get('project_description', 'No description provided'))

# -----------------------
# Performance Report
# -----------------------
def show_performance_report(user_data):
    """Display detailed performance analytics for the student"""
    with st.expander("📊 Performance Analytics", expanded=True):
        # Calculate metrics
        tasks = user_data.get('tasks', [])
        total_tasks = len(tasks)
        completed_tasks = [t for t in tasks if t.get('completed')]
        pending_tasks = [t for t in tasks if not t.get('completed') and not t.get('submitted')]
        submitted_tasks = [t for t in tasks if t.get('submitted') and not t.get('completed')]
        late_submissions = len([t for t in tasks if t.get('late', False)])
        
        total_marks = sum(t.get('marks', 0) for t in completed_tasks)
        max_possible = sum(t.get('max_marks', 0) for t in tasks)
        percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
        
        # Metrics Display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Overall Completion", 
                     f"{len(completed_tasks)}/{total_tasks} tasks", 
                     f"{len(completed_tasks)/total_tasks*100:.1f}%" if total_tasks > 0 else "0%")
            st.metric("Total Marks Earned", 
                     f"{total_marks}/{max_possible}", 
                     f"{percentage:.1f}%" if max_possible > 0 else "0%")
        
        with col2:
            avg_score = total_marks/len(completed_tasks) if completed_tasks else 0
            st.metric("Average Score", 
                     f"{avg_score:.1f}" if completed_tasks else "N/A")
            st.metric("Late Submissions", late_submissions)
        
        with col3:
            # Progress circle visualization
            st.markdown(f"""
            <div style="text-align: center;">
                <svg width="120" height="120">
                    <circle cx="60" cy="60" r="50" fill="none" stroke="#ddd" stroke-width="10"/>
                    <circle cx="60" cy="60" r="50" fill="none" stroke="#fdbb2d" stroke-width="10" 
                        stroke-dasharray="314" stroke-dashoffset="{314 * (1 - (percentage/100 if percentage > 0 else 0))}"/>
                    <text x="60" y="60" text-anchor="middle" dominant-baseline="middle" 
                        font-size="20" font-weight="bold" fill="#fdbb2d">{percentage:.1f}%</text>
                </svg>
                <p style="margin-top: -10px; font-size: 14px;">Overall Performance</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Visualizations
        st.markdown("### Performance Visualizations")
        
        # Generate charts
        fig1, fig2 = None, None
        
        if tasks:
            # Completion pie chart
            fig1, ax1 = plt.subplots(figsize=(8, 4))
            if completed_tasks or submitted_tasks or pending_tasks:
                sizes = [len(completed_tasks), len(submitted_tasks), len(pending_tasks)]
                labels = ['Completed', 'Submitted', 'Pending']
                colors = ['#2ecc71', '#f39c12', '#e74c3c']
                
                # Only show categories that have values
                sizes = [s for s in sizes if s > 0]
                labels = [l for i, l in enumerate(labels) if sizes[i] > 0] if len(sizes) == len(labels) else labels[:len(sizes)]
                colors = colors[:len(sizes)]
                
                ax1.pie(
                    sizes,
                    labels=labels,
                    colors=colors,
                    autopct='%1.1f%%',
                    startangle=90
                )
                ax1.axis('equal')
                ax1.set_title('Task Completion Status')
            else:
                ax1.text(0.5, 0.5, 'No task data available', 
                        ha='center', va='center', fontsize=12)
                ax1.axis('off')
            
            # Performance over time line chart
            if completed_tasks:
                fig2, ax2 = plt.subplots(figsize=(10, 4))
                try:
                    dates = [datetime.strptime(t['submission_date'], "%Y-%m-%d") for t in completed_tasks]
                    marks = [t.get('marks', 0) for t in completed_tasks]
                    max_marks = [t.get('max_marks', 1) for t in completed_tasks]
                    percentages = [(m/mm)*100 for m, mm in zip(marks, max_marks)]
                    
                    # Sort by date
                    dates, percentages = zip(*sorted(zip(dates, percentages)))
                    
                    ax2.plot(dates, percentages, marker='o', color='#3498db', label='Performance %')
                    ax2.axhline(y=50, color='r', linestyle='--', label='Passing Threshold')
                    ax2.set_ylim(0, 110)
                    ax2.set_ylabel('Performance (%)')
                    ax2.set_title('Performance Over Time')
                    ax2.legend()
                    ax2.grid(True)
                    plt.xticks(rotation=45)
                except Exception as e:
                    st.warning(f"Could not generate performance chart: {str(e)}")
                    fig2 = None
        
        # Display charts
        if fig1:
            st.pyplot(fig1)
            plt.close(fig1)
        else:
            st.info("No task data available for visualization")
            
        if fig2:
            st.pyplot(fig2)
            plt.close(fig2)
        
        st.markdown("---")
        
        # Task performance breakdown
        st.markdown("### Task Performance Breakdown")
        if tasks:
            task_data = []
            for task in tasks:
                if task.get('completed'):
                    task_percentage = (task.get('marks', 0)/task.get('max_marks', 1))*100
                    task_data.append({
                        "Task": task['name'],
                        "Status": "✅ Completed",
                        "Marks": f"{task.get('marks', 0)}/{task['max_marks']}",
                        "Percentage": task_percentage,
                        "Remarks": task.get('remarks', 'N/A')
                    })
                elif task.get('submitted'):
                    task_data.append({
                        "Task": task['name'],
                        "Status": "📤 Submitted",
                        "Marks": "Pending",
                        "Percentage": None,
                        "Remarks": "Awaiting evaluation"
                    })
                else:
                    task_data.append({
                        "Task": task['name'],
                        "Status": "📝 Pending",
                        "Marks": "Not submitted",
                        "Percentage": None,
                        "Remarks": "Not submitted"
                    })
            
            # Create DataFrame for display
            df = pd.DataFrame(task_data)
            
            # Display with progress bars for percentages
            st.dataframe(
                df,
                column_config={
                    "Percentage": st.column_config.ProgressColumn(
                        "Completion",
                        help="Task completion percentage",
                        format="%.1f%%",
                        min_value=0,
                        max_value=100,
                    ),
                },
                hide_index=True,
                use_container_width=True,
                height=min(400, 50 * len(df) + 50)  # Dynamic height based on rows
            )
        else:
            st.info("No tasks available for performance analysis")
            
        # Grade Summary
        st.markdown("---")
        st.markdown("### Grade Summary")
        
        if percentage >= 80:
            grade = "A1 (Excellent)"
            feedback = "Outstanding performance! You've demonstrated excellent understanding of all concepts."
        elif percentage >= 70:
            grade = "A (Very Good)"
            feedback = "Strong performance! You've shown a very good grasp of the material."
        elif percentage >= 60:
            grade = "B (Good)"
            feedback = "Good work! You have a solid understanding of most concepts."
        elif percentage >= 50:
            grade = "C (Satisfactory)"
            feedback = "You've met the basic requirements. Consider reviewing areas of difficulty."
        elif total_tasks > 0:
            grade = "FAIL (Needs Improvement)"
            feedback = "Additional work is needed to demonstrate competency. Please review the material and resubmit."
        else:
            grade = "N/A"
            feedback = "No tasks have been graded yet."
        
        st.markdown(f"**Current Grade:** {grade}")  
        st.markdown(f"**Feedback:** {feedback}")

# -----------------------
# Admin Dashboard
# -----------------------
def display_tasks(task_list, student_email, tab_name=""):
    student = st.session_state.users_db[student_email]
    for task_idx, task in enumerate(task_list):
        with st.container(border=True):
            cols = st.columns([4, 1])
            cols[0].markdown(f"**{task['name']}**")
            
            # Generate unique keys including tab_name
            edit_key = f"edit_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
            delete_key = f"delete_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
            editing_key = f"editing_task_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
            
            # Editing form (only shown when editing)
            if st.session_state.get(editing_key, False):
                with st.form(key=f"edit_form_{student['email']}_{task['name']}_{tab_name}_{task_idx}"):
                    new_name = st.text_input("Task Name", value=task['name'])
                    new_desc = st.text_area("Description", value=task['description'])
                    new_due_date = st.date_input("Due Date", 
                                               value=datetime.strptime(task['due_date'], "%Y-%m-%d").date())
                    new_max_marks = st.number_input("Max Marks", 
                                                  min_value=1, 
                                                  value=task['max_marks'])
                    
                    # Add field for editing obtained marks if task is completed
                    if task.get('completed'):
                        new_marks = st.number_input("Obtained Marks",
                                                   min_value=0,
                                                   max_value=task['max_marks'],  # Ensure marks don't exceed max
                                                   value=task.get('marks', 0))
                    else:
                        new_marks = task.get('marks', 0)
                    
                    col1, col2 = st.columns(2)
                    if col1.form_submit_button("Save Changes"):
                        # Validate marks don't exceed max marks
                        if new_marks > new_max_marks:
                            st.error("Obtained marks cannot exceed maximum marks!")
                        else:
                            task['name'] = new_name
                            task['description'] = new_desc
                            task['due_date'] = new_due_date.strftime("%Y-%m-%d")
                            task['max_marks'] = new_max_marks
                            if task.get('completed'):
                                task['marks'] = new_marks
                            
                            # Recalculate total_marks
                            student['total_marks'] = sum(
                                t.get('marks', 0) 
                                for t in student['tasks'] 
                                if t.get('completed')
                            )
                            
                            if update_user_in_firestore(student):
                                st.success("Task updated successfully!")
                                st.session_state[editing_key] = False
                                st.rerun()
                    
                    if col2.form_submit_button("Cancel"):
                        st.session_state[editing_key] = False
                        st.rerun()

            # Rest of the task display remains the same...
            status = "✅ Completed" if task.get('completed') else "📝 Pending"
            if task.get('submitted') and not task.get('completed'):
                status = "📤 Submitted"
            
            cols[1].markdown(f"**Status:** {status}")
            
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Due Date:** {task['due_date']}")
            st.write(f"**Assigned on:** {task['assigned_date']}")
            st.write(f"**Max Marks:** {task['max_marks']}")
            
            if task.get('completed'):
                st.write(f"**Obtained Marks:** {task.get('marks', 0)}")
            
            if task.get('submitted'):
                st.success("📤 Task submitted for review")
                st.write(f"**Submitted on:** {task['submission_date']}")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    if task.get('submission_file'):
                        download_key = f"download_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
                        
                        # First button to initiate download
                        if st.button("⬇️ Download Submission", key=f"btn_{download_key}"):
                            st.session_state[download_key] = True
                        
                        # Actual download happens here if state is True
                        if st.session_state.get(download_key, False):
                            try:
                                file_bytes = base64.b64decode(task['submission_file'])
                                st.download_button(
                                    label="⬇️ Click to Download",
                                    data=file_bytes,
                                    file_name=f"{student['first_name']}_{student['last_name']}_{task['name']}.zip",
                                    mime="application/zip",
                                    key=f"dl_{download_key}"
                                )
                                # Reset the state after download
                                st.session_state[download_key] = False
                            except Exception as e:
                                st.error(f"Error preparing file for download: {str(e)}")
                
                if col3.button("✏️ Edit", key=edit_key):
                    st.session_state[editing_key] = True
                
                if col4.button("🗑️ Delete", key=delete_key):
                    if delete_task_from_firestore(student['email'], task['name']):
                        st.success("Task deleted successfully!")
                        st.rerun()
                
                if not task['completed']:
                    grade_form_key = f"grade_form_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
                    with st.form(key=grade_form_key):
                        marks_key = f"marks_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
                        marks = st.number_input(
                            "Assign Marks",
                            min_value=0,
                            max_value=task['max_marks'],  # Ensure marks don't exceed max
                            value=task.get('marks', 0),
                            key=marks_key
                        )
                        remarks_key = f"remarks_{student['email']}_{task['name']}_{tab_name}_{task_idx}"
                        remarks = st.text_area(
                            "Remarks",
                            value=task.get('remarks', ''),
                            key=remarks_key
                        )
                        
                        if st.form_submit_button("Grade Task"):
                            # Validation is already handled by the number_input with max_value
                            task['marks'] = marks
                            task['remarks'] = remarks
                            task['completed'] = True
                            
                            # Recalculate total_marks
                            student['total_marks'] = sum(
                                t.get('marks', 0) 
                                for t in student['tasks'] 
                                if t.get('completed')
                            )
                            
                            if update_user_in_firestore(student):
                                st.success("Task graded successfully!")
                                st.rerun()
            else:
                st.info("Task not submitted yet")

def show_admin_dashboard():
    admin = st.session_state.users_db[st.session_state.logged_in_user]

    st.markdown(f"""
    <div class="admin-header">
        <h1 style="color: #fdbb2d; display: flex; margin-top: -80px;">👑 Admin Dashboard</h1>
        <p>Welcome back, {admin['first_name']} {admin['last_name']}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color:#fdbb2d;">Total Students</h3>
                <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('role') != 'admin'])}</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color:#fdbb2d;">Pending Applications</h3>
                <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'pending'])}</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color:#fdbb2d;">Active Students</h3>
                <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'approved' and u.get('role') != 'admin'])}</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color:#fdbb2d;">Blocked Students</h3>
                <p style="font-size:2rem;">{len([u for u in st.session_state.users_db.values() if u.get('status') == 'blocked'])}</p>
            </div>
        """, unsafe_allow_html=True)

    # Main container for user management
    with st.container():
        st.markdown("## User Management")
        tab1, tab2 = st.tabs(["Pending Approvals", "All Students"])

        with tab1:
            pending_users = [u for u in st.session_state.users_db.values() if u.get('status') == 'pending']
            if not pending_users:
                st.info("No pending applications.")
            else:
                for user in pending_users:
                    with st.container(border=True):
                        cols = st.columns([3, 2, 2, 2])
                        cols[0].write(f"**{user['first_name']} {user['last_name']}** ({user['email']})")
                        cols[1].write(user.get('program', 'N/A'))
                        if cols[2].button("✅ Approve", key=f"approve_{user['email']}"):
                            user['status'] = "approved"
                            update_user_in_firestore(user)
                            st.rerun()
                        if cols[3].button("❌ Reject", key=f"reject_{user['email']}"):
                            requests.delete(f"{FIREBASE_DB_URL}/applications/{user['email']}")
                            del st.session_state.users_db[user['email']]
                            st.rerun()

        with tab2:
            all_students = [u for u in st.session_state.users_db.values() if u.get('role') != 'admin']
            if not all_students:
                st.info("No students registered.")
            else:
                for student in all_students:
                    with st.container(border=True):
                        cols = st.columns([3, 1, 1, 1, 1])  # Added extra column for delete button
                        cols[0].markdown(
                            f"""
                            <span style='color: #fdbb2d; font-size: 24px; font-weight: bold;'>
                                {student['first_name']} {student['last_name']} - {student.get('program', 'N/A')}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )

                        if cols[1].button("📊 View Details", key=f"details_{student['email']}"):
                            st.session_state[f"show_details_{student['email']}"] = not st.session_state.get(f"show_details_{student['email']}", False)
                        
                        if cols[2].button("📋 View Tasks", key=f"tasks_{student['email']}"):
                            st.session_state[f"show_tasks_{student['email']}"] = not st.session_state.get(f"show_tasks_{student['email']}", False)
                        
                        if cols[3].button(f"{'🔓 Unblock' if student.get('status') == 'blocked' else '🚫 Block'}", 
                                         key=f"block_{student['email']}"):
                            if student.get('status') == 'blocked':
                                if unblock_student_in_firestore(student['email']):
                                    st.success("Student unblocked successfully!")
                                    st.rerun()
                            else:
                                if block_student_in_firestore(student['email']):
                                    st.success("Student blocked successfully!")
                                    st.rerun()
                        
                        # Delete user button with confirmation
                        if cols[4].button("🗑️ Delete", key=f"delete_{student['email']}"):
                            st.session_state[f"confirm_delete_{student['email']}"] = True
                        
                        if st.session_state.get(f"confirm_delete_{student['email']}", False):
                            st.warning(f"Are you sure you want to permanently delete {student['first_name']} {student['last_name']}?")
                            confirm_cols = st.columns(2)
                            if confirm_cols[0].button("✅ Confirm Delete", key=f"confirm_delete_btn_{student['email']}"):
                                if delete_user_from_firestore(student['email']):
                                    del st.session_state.users_db[student['email']]
                                    st.success(f"User {student['email']} deleted successfully!")
                                    st.rerun()
                                else:
                                    st.error("Failed to delete user from database")
                        
                        # Student Details Section
                        if st.session_state.get(f"show_details_{student['email']}", False):
                            with st.container(border=True):
                                st.markdown("#### Student Details")
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.write(f"**Full Name:** {student['first_name']} {student['last_name']}")
                                    st.write(f"**Email:** {student['email']}")
                                    st.write(f"**Contact:** {student.get('phone', 'N/A')}")
                                    st.write(f"**Status:** {student.get('status', 'N/A').capitalize()}")
                                    st.write(f"**Program Duration:** {student.get('internship_duration', 'N/A')}")
                                    
                                with col2:
                                    st.write(f"**University:** {student.get('university', 'N/A')}")
                                    st.write(f"**Degree Program:** {student.get('degree', 'N/A')} in {student.get('major', 'N/A')}")
                                    st.write(f"**Graduation Year:** {student.get('graduation_year', 'N/A')}")
                                    st.write(f"**TEQNITEHUB Program:** {student.get('program', 'N/A')}")
                                
                                st.markdown("---")
                                st.markdown("#### Skills & Technologies")
                                if student.get('programming_languages'):
                                    st.write("**Programming Languages:**")
                                    cols = st.columns(4)
                                    for i, lang in enumerate(student['programming_languages']):
                                        cols[i%4].markdown(f"- {lang}")
                                else:
                                    st.info("No programming languages specified")
                                
                                st.markdown("---")
                                st.markdown("#### About Me")
                                st.write(student.get('project_description', 'No description provided'))

                        # Task Management Section
                        if st.session_state.get(f"show_tasks_{student['email']}", False):
                            with st.container(border=True):
                                st.markdown("<h4 style='color: #fdbb2d;'>Task Management</h4>", unsafe_allow_html=True)
                                
                                if 'tasks' in student and student['tasks']:
                                    completed_tasks = [t for t in student['tasks'] if t.get('completed')]
                                    pending_tasks = [t for t in student['tasks'] if not t.get('completed') and not t.get('submitted')]
                                    submitted_tasks = [t for t in student['tasks'] if t.get('submitted') and not t.get('completed')]
                                    overdue_tasks = [t for t in student['tasks'] if datetime.strptime(t['due_date'], "%Y-%m-%d").date() < date.today() and not t.get('completed')]
                                    total_marks_possible = sum(t['max_marks'] for t in student['tasks'])
                                    marks_earned = sum(t.get('marks', 0) for t in student['tasks'] if t.get('completed'))
                                    
                                    tab_summary, tab_all, tab_completed, tab_pending, tab_submitted, tab_overdue, tab_assign = st.tabs([
                                        "📊 Summary",
                                        "All Tasks", 
                                        f"✅ Completed ({len(completed_tasks)})", 
                                        f"📝 Pending ({len(pending_tasks)})",
                                        f"📤 Submitted ({len(submitted_tasks)})",
                                        f"⚠️ Overdue ({len(overdue_tasks)})",
                                        "➕ Assign Task"
                                    ])
                                    
                                    with tab_summary:
                                        st.markdown("### Task Summary")
                                        cols = st.columns(3)
                                        cols[0].metric("Total Tasks", len(student['tasks']))
                                        cols[1].metric("Completed Tasks", len(completed_tasks))
                                        cols[2].metric("Pending Tasks", len(pending_tasks))
                                        cols[0].metric("Submitted Tasks", len(submitted_tasks))
                                        cols[1].metric("Overdue Tasks", len(overdue_tasks))
                                        cols[2].metric("Completion Rate", f"{len(completed_tasks)/len(student['tasks'])*100:.1f}%" if len(student['tasks']) > 0 else "0%")
                                        
                                        st.markdown("---")
                                        st.markdown("### Marks Summary")
                                        cols = st.columns(2)
                                        cols[0].metric("Total Possible Marks", total_marks_possible)
                                        cols[1].metric("Marks Earned", marks_earned)
                                        st.progress(marks_earned/total_marks_possible if total_marks_possible > 0 else 0)
                                        percentage = (marks_earned/total_marks_possible)*100
                                        st.caption(f"Percentage: {percentage:.1f}%")
                                        
                                        if percentage >= 80:
                                            st.caption("Grade: A1")
                                        elif percentage >= 70:
                                            st.caption("Grade: A")
                                        elif percentage >= 60:
                                            st.caption("Grade: B")
                                        elif percentage >= 50:
                                            st.caption("Grade: C")
                                        else:
                                            st.caption("Grade: FAIL")
                                    
                                    with tab_all:
                                        if student['tasks']:
                                            display_tasks(student['tasks'], student['email'], "all")
                                        else:
                                            st.info("No tasks found in this category")
                                    
                                    with tab_completed:
                                        if completed_tasks:
                                            display_tasks(completed_tasks, student['email'], "completed")
                                        else:
                                            st.info("No completed tasks found")
                                    
                                    with tab_pending:
                                        if pending_tasks:
                                            display_tasks(pending_tasks, student['email'], "pending")
                                        else:
                                            st.info("No pending tasks found")
                                    
                                    with tab_submitted:
                                        if submitted_tasks:
                                            display_tasks(submitted_tasks, student['email'], "submitted")
                                        else:
                                            st.info("No submitted tasks found")
                                    
                                    with tab_overdue:
                                        if overdue_tasks:
                                            display_tasks(overdue_tasks, student['email'], "overdue")
                                        else:
                                            st.info("No overdue tasks found")
                                    
                                    with tab_assign:
                                        with st.form(key=f"assign_task_form_{student['email']}"):
                                            st.write("**Assign New Task**")
                                            task_name = st.text_input("Task Name", key=f"task_name_{student['email']}")
                                            task_desc = st.text_area("Description", key=f"task_desc_{student['email']}")
                                            due_date = st.date_input("Due Date", value=date.today(), key=f"due_date_{student['email']}")
                                            max_marks = st.selectbox("Max Marks", [10, 20, 30, 50, 100], key=f"max_marks_{student['email']}")
                                            
                                            if st.form_submit_button("Assign Task"):
                                                if task_name:
                                                    new_task = {
                                                        "name": task_name,
                                                        "description": task_desc,
                                                        "due_date": due_date.strftime("%Y-%m-%d"),
                                                        "max_marks": max_marks,
                                                        "assigned_date": datetime.now().strftime("%Y-%m-%d"),
                                                        "completed": False,
                                                        "submitted": False,
                                                        "submission_file": "",
                                                        "submission_date": "",
                                                        "marks": 0,
                                                        "remarks": "",
                                                        "late": False
                                                    }
                                                    if 'tasks' not in student:
                                                        student['tasks'] = []
                                                    student['tasks'].append(new_task)
                                                    if update_user_in_firestore(student):
                                                        st.success(f"Task '{task_name}' assigned to {student['first_name']} {student['last_name']}.")
                                                        st.rerun()
                                                    else:
                                                        st.error("Failed to assign task")
                                                else:
                                                    st.warning("Please enter a task name")
                                else:
                                    with st.form(key=f"assign_task_form_{student['email']}"):
                                        st.write("**Assign New Task**")
                                        task_name = st.text_input("Task Name", key=f"task_name_{student['email']}")
                                        task_desc = st.text_area("Description", key=f"task_desc_{student['email']}")
                                        due_date = st.date_input("Due Date", value=date.today(), key=f"due_date_{student['email']}")
                                        max_marks = st.selectbox("Max Marks", [10, 20, 30, 50, 100], key=f"max_marks_{student['email']}")
                                        
                                        if st.form_submit_button("Assign Task"):
                                            if task_name:
                                                new_task = {
                                                    "name": task_name,
                                                    "description": task_desc,
                                                    "due_date": due_date.strftime("%Y-%m-%d"),
                                                    "max_marks": max_marks,
                                                    "assigned_date": datetime.now().strftime("%Y-%m-%d"),
                                                    "completed": False,
                                                    "submitted": False,
                                                    "submission_file": "",
                                                    "submission_date": "",
                                                    "marks": 0,
                                                    "remarks": "",
                                                    "late": False
                                                }
                                                if 'tasks' not in student:
                                                    student['tasks'] = []
                                                student['tasks'].append(new_task)
                                                if update_user_in_firestore(student):
                                                    st.success(f"Task '{task_name}' assigned to {student['first_name']} {student['last_name']}.")
                                                    st.rerun()
                                                else:
                                                    st.error("Failed to assign task")
                                    st.info("No tasks assigned to this student")
                                    
                                    
def delete_user_from_firestore(email):
    """Delete a user from Firestore"""
    try:
        doc_path = f"applications/{email}"
        url = f"{FIREBASE_DB_URL}/{doc_path}"
        
        response = requests.delete(url)
        return response.status_code == 200
    except Exception as e:
        st.error(f"Error deleting user: {str(e)}")
        return False
    
# -----------------------
# User Dashboard
# -----------------------
def show_user_dashboard():
    user = st.session_state.users_db[st.session_state.logged_in_user]
    
    st.markdown(f"""
        <div class="user-header">
            <h1 style="color: #fdbb2d; display: flex; margin-top: -80px;" >👤 Student Dashboard</h1>
            <p>Welcome back, {user['first_name']} {user['last_name']}</p>
        </div>
    """, unsafe_allow_html=True)

    # Quick stats cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        completed_tasks = len([t for t in user.get('tasks', []) if t.get('completed')])
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color: #fdbb2d;" >Completed Tasks</h3>
                <p style="font-size:2rem;">{completed_tasks}</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        pending_tasks = len([t for t in user.get('tasks', []) if not t.get('completed')])
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color: #fdbb2d;" >Pending Tasks</h3>
                <p style="font-size:2rem;">{pending_tasks}</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        total_marks = user.get('total_marks', 0)
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color: #fdbb2d;" >Total Marks</h3>
                <p style="font-size:2rem;">{total_marks}</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        max_possible = sum(t.get('max_marks', 0) for t in user.get('tasks', []))
        percentage = (total_marks/max_possible)*100 if max_possible > 0 else 0
        st.markdown(f"""
            <div class="stats-card">
                <h3 style="color: #fdbb2d;" >Overall Grade</h3>
                <p style="font-size:2rem;">{percentage:.1f}%</p>
            </div>
        """, unsafe_allow_html=True)

    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Tasks", "📊 Performance", "🏆 Certificates", "👤 Profile"])
    
    with tab1:
        st.markdown("### Your Tasks")
        if 'tasks' not in user or not user['tasks']:
            st.info("You have no tasks assigned.")
        else:
            for task_idx, task in enumerate(user['tasks']):
                with st.expander(f"Task {task_idx + 1}: {task['name']}"):
                    container_class = "task-container "
                    if task.get('completed'):
                        container_class += "completed-task-container"
                    elif is_task_late(task['due_date']):
                        container_class += "late-task-container"
                        task['late'] = True
                    elif task.get('submitted'):
                        container_class += "submitted-task-container"
                    else:
                        container_class += "pending-task-container"

                    st.markdown(f"""
                    <div class="{container_class}">
                        <div class="task-header">
                            <h4 style='color: #fdbb2d;'>{task['name']}</h4>
                            <span class="task-due">Due: {task['due_date']}</span>
                        </div>
                        <div class="task-content">
                            <p><strong>Description:</strong> {task['description']}</p>
                            <p><strong>Max Marks:</strong> {task['max_marks']}</p>
                            <p><strong>Assigned on:</strong> {task['assigned_date']}</p>
                    """, unsafe_allow_html=True)

                    if task.get('late'):
                        st.markdown('<p class="task-status late">⚠️ This task is overdue!</p>', unsafe_allow_html=True)

                    if not task['completed']:
                        if task.get('submitted'):
                            st.markdown('<p class="task-status submitted">📤 Task submitted - awaiting review</p>', unsafe_allow_html=True)
                            st.write(f"**Submitted on:** {task['submission_date']}")
                            if task.get('submission_file'):
                                download_key = f"download_my_{task_idx}"
                                
                                # First button to initiate download
                                if st.button("⬇️ Download My Submission", key=f"btn_{download_key}"):
                                    st.session_state[download_key] = True
                                
                                # Actual download happens here if state is True
                                if st.session_state.get(download_key, False):
                                    try:
                                        file_bytes = base64.b64decode(task['submission_file'])
                                        st.download_button(
                                            label="⬇️ Click to Download",
                                            data=file_bytes,
                                            file_name=f"my_submission_{task['name']}.zip",
                                            mime="application/zip",
                                            key=f"dl_{download_key}"
                                        )
                                        # Reset the state after download
                                        st.session_state[download_key] = False
                                    except Exception as e:
                                        st.error(f"Error preparing file for download: {str(e)}")
                        else:
                            st.markdown("### Submit Task")
                            uploaded_file = st.file_uploader(
                                "Upload your solution (.zip)", 
                                type=["zip"],
                                key=f"upload_{task_idx}"
                            )
                            
                            if uploaded_file is not None:
                                if st.button(f"Submit Task {task_idx + 1}", key=f"submit_{task_idx}"):
                                    try:
                                        with zipfile.ZipFile(io.BytesIO(uploaded_file.read())) as test_zip:
                                            if test_zip.testzip() is None:
                                                uploaded_file.seek(0)
                                                file_content = uploaded_file.read()
                                                task['submission_file'] = base64.b64encode(file_content).decode('utf-8')
                                                task['submission_date'] = datetime.now().strftime("%Y-%m-%d")
                                                task['submitted'] = True
                                                if update_user_in_firestore(user):
                                                    st.success("Task submitted successfully!")
                                                    st.rerun()
                                                else:
                                                    st.error("Failed to submit task")
                                            else:
                                                st.error("Invalid ZIP file - corrupted or empty")
                                    except zipfile.BadZipFile:
                                        st.error("Invalid file format - please upload a valid ZIP file")
                                    except Exception as e:
                                        st.error(f"Error processing file: {str(e)}")
                    else:
                        st.markdown('<p class="task-status completed">✅ Task Completed</p>', unsafe_allow_html=True)
                        if task.get('marks') is not None:
                            st.write(f"**Marks Obtained:** {task['marks']}/{task['max_marks']}")
                            st.write(f"**Remarks:** {task.get('remarks', 'No remarks')}")
                        if task.get('submission_file'):
                            download_key = f"download_completed_{task_idx}"
                            
                            # First button to initiate download
                            if st.button("⬇️ Download My Submission", key=f"btn_{download_key}"):
                                st.session_state[download_key] = True
                            
                            # Actual download happens here if state is True
                            if st.session_state.get(download_key, False):
                                try:
                                    file_bytes = base64.b64decode(task['submission_file'])
                                    st.download_button(
                                        label="⬇️ Click to Download",
                                        data=file_bytes,
                                        file_name=f"my_submission_{task['name']}.zip",
                                        mime="application/zip",
                                        key=f"dl_{download_key}"
                                    )
                                    # Reset the state after download
                                    st.session_state[download_key] = False
                                except Exception as e:
                                    st.error(f"Error preparing file for download: {str(e)}")

                    st.markdown("</div></div>", unsafe_allow_html=True)
                    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)
    
    with tab2:
        show_performance_report(user)
    
    with tab3:
        st.markdown("### Your Certificates")
        
        # Check if student has completed all tasks and internship duration is over
        total_tasks = len(user.get('tasks', []))
        completed_tasks = len([t for t in user.get('tasks', []) if t.get('completed')])
        
        # Get internship duration (assuming format like "3 Months" or "6 Months")
        internship_duration = user.get('internship_duration', '3 Months')
        duration_months = int(internship_duration.split()[0])
        
        # Calculate end date (assuming assigned_date is when internship started)
        if user.get('tasks'):
            assigned_date = min(
                datetime.strptime(t['assigned_date'], "%Y-%m-%d") 
                for t in user['tasks']
            )
            end_date = assigned_date + timedelta(days=duration_months*30)
            is_internship_completed = date.today() >= end_date.date()
        else:
            is_internship_completed = False
        
        if total_tasks > 0 and completed_tasks == total_tasks and is_internship_completed:
            st.success("🎉 Congratulations! You've successfully completed your TEQNITEHUB internship program!")
            
            # Generate certificate
            completion_date = datetime.now().strftime("%B %d, %Y")
            program_duration = user.get('internship_duration', '3 Months')
            
            certificate_pdf = generate_certificate(user, completion_date, program_duration)
            
            # Certificate download with two-step process
            cert_download_key = "certificate_download_trigger"
            
            # First button to initiate download
            if st.button("📄 Download Completion Certificate", key=f"btn_{cert_download_key}"):
                st.session_state[cert_download_key] = True
            
            # Actual download happens here if state is True
            if st.session_state.get(cert_download_key, False):
                st.download_button(
                    label="📄 Click to Download Certificate",
                    data=certificate_pdf,
                    file_name=f"TEQNITEHUB_Certificate_{user['first_name']}_{user['last_name']}.pdf",
                    mime="application/pdf",
                    key="certificate_download"
                )
                # Reset the state after download
                st.session_state[cert_download_key] = False
            
            st.markdown("---")
            st.markdown("#### Certificate Verification")
            st.info("Your certificate includes a unique verification code that can be used to validate its authenticity.")
        else:
            # Show progress status
            if total_tasks == 0:
                st.warning("You don't have any tasks assigned yet.")
            else:
                progress = completed_tasks / total_tasks
                st.warning(f"""
                🔍 Your internship progress:
                - Completed {completed_tasks} out of {total_tasks} tasks ({progress:.0%})
                - Internship duration: {user.get('internship_duration', 'N/A')}
                """)
                
                # Progress bar
                st.progress(progress)
                
                # Specific feedback
                if completed_tasks < total_tasks:
                    st.error("You need to complete all assigned tasks to earn your certificate.")
                elif not is_internship_completed:
                    if user.get('tasks'):
                        assigned_date = min(
                            datetime.strptime(t['assigned_date'], "%Y-%m-%d") 
                            for t in user['tasks']
                        )
                        days_remaining = (end_date.date() - date.today()).days
                        if days_remaining > 0:
                            st.info(f"Your internship will be completed in {days_remaining} days on {end_date.strftime('%B %d, %Y')}")
                        else:
                            st.info("Your internship period is complete! Please wait for final review.")
                    else:
                        st.info("Your internship period is not yet complete.")
                
                st.markdown("---")
                st.markdown("#### Certificate Requirements")
                st.write("To earn your TEQNITEHUB certificate, you must:")
                st.write("- Complete all assigned tasks")
                st.write("- Complete the full internship duration")
                st.write("- Achieve a passing grade (50% or higher)")
                
    with tab4:
        show_user_profile(user)

# -----------------------
# Login Page
# -----------------------
def show_login():
    st.markdown("""
        <h1 style="text-align: center; color: #fdbb2d; font-family: 'Helvetica Neue'; font-weight: bold;">
            🎓 TEQNITEHUB LMS Portal
        </h1>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        st.markdown("""
        <style>
        div[data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        }
        .form-section {
            margin-bottom: 25px;
        }
        .section-title {
            color: #fdbb2d;
            font-size: 18px;
            font-weight: 600;
            margin: 20px 0 10px 0;
            padding-bottom: 5px;
            border-bottom: 1px solid rgba(75, 139, 255, 0.3);
        }
        </style>
        """, unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            if email in st.session_state.users_db:
                user = st.session_state.users_db[email]
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if user["password"] == hashed_password:
                    if user.get("status") == "approved":
                        st.session_state.logged_in_user = email
                        st.query_params["auth_token"] = f"{email}|{hashed_password}"
                        if user.get("role") == "admin":
                            st.success("Admin login successful!")
                        else:
                            st.success("Student login successful!")
                        st.rerun()
                    elif user.get("status") == "blocked":
                        st.error("Your account has been blocked. Please contact the administrator.")
                    else:
                        st.error("Your application is pending approval.")
                else:
                    st.error("Invalid password.")
            else:
                st.error("Account not found.")
                
    if st.button("Back To Home"):
        st.switch_page("app.py")

# -----------------------
# Main App Logic
# -----------------------
if st.session_state.logged_in_user:
    user = st.session_state.users_db[st.session_state.logged_in_user]
    if user.get("role") == "admin":
        show_admin_dashboard()
    else:
        show_user_dashboard()

    if st.button("Logout", key="logout_btn"):
        st.session_state.logged_in_user = None
        st.query_params.clear()
        st.rerun()
else:
    show_login()