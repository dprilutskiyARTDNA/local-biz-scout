import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Local Biz Website Scout")

st.sidebar.title("🔍 Scout Control Panel")
st.sidebar.write("Find local businesses missing a web presence.")

location = st.sidebar.text_input("Target Location / Zip Code", placeholder="e.g., Northridge")
industry = st.sidebar.selectbox(
    "Select Industry Niche", 
    ["Auto Repair", "Landscaping", "Roofing", "Salons", "Plumbing", "HVAC"]
)

scout_button = st.sidebar.button("🚀 Scout Area", use_container_width=True)

st.title("💼 Lead Generation & Website Builder Dashboard")
st.write("Manage your local business leads, generate prototypes, and track your pitches.")

if scout_button:
    st.subheader(f"📋 'No Website' Leads Found in {location or 'Your Area'} ({industry})")
    
    mock_leads = {
        "Business Name": ["Valley Auto Specialists", "818 Clean Cuts Landscaping", "SFV Roof Masters"],
        "Phone Number": ["(818) 555-0192", "(818) 555-0143", "(818) 555-0177"],
        "Address": ["Northridge, CA", "Reseda, CA", "Van Nuys, CA"],
        "Status": ["New", "New", "New"]
    }
    df = pd.DataFrame(mock_leads)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("⚡ Action Center")
        selected_biz = st.selectbox("Select a Lead to Target", df["Business Name"])
        st.write(f"Ready to generate a custom portfolio site for **{selected_biz}**?")
        generate_button = st.button("🔨 Generate Free Prototype Site", use_container_width=True)
        
        st.markdown("### 📞 Sales Pitch Quick-Notes")
        st.info(f"When calling, say: \n\n*'Hey, I noticed {selected_biz} doesn't have a modern landing page online. I actually went ahead and pre-built a custom layout for your shop. Want me to send over the link to look at for free?'*")

    with col2:
        st.subheader("🌐 Prototype Website Preview")
        if generate_button:
            st.success(f"Success! Generated custom site layout for {selected_biz}.")
            st.code(f"Shareable Link: https://yourplatform.com/preview/{selected_biz.lower().replace(' ', '-')}", language="text")
            st.markdown(
                f"""
                <div style="border: 2px solid #ddd; padding: 20px; border-radius: 10px; background-color: #f9f9f9; color: #333;">
                    <h1 style="color: #ff4b4b; text-align: center;">⚡ {selected_biz} ⚡</h1>
                    <p style="text-align: center; font-style: italic;">Premium {industry} Services in the San Fernando Valley</p>
                    <hr>
                    <h3>Our Services</h3>
                    <ul>
                        <li>Top-Tier Professional Quality</li>
                        <li>Local, Reliable, and Fast Service</li>
                        <li>100% Satisfaction Guaranteed</li>
                    </ul>
                    <hr>
                    <h4 style="text-align: center;">📞 Call Us Today! Placeholder Phone Number Layout</h4>
                </div>
                """, 
                unsafe_html=True
            )
        else:
            st.info("Select a business from the dropdown and click 'Generate' to see the mock web design render here.")
else:
    st.info("← Enter a target location in the sidebar panel and click 'Scout Area' to view your command center layout.")
  
