import streamlit as st

st.set_page_config(
    page_title="CV_MuhammadRaihanPermadi",
    layout="wide"
)

#column

st.markdown(
    '''
    <style>
    div[data-testid="stHorizontalBlock"] > div:first-of-type {
        background-color: #d6a467;
        padding: 5px
    }
    </style>
    ''',
    unsafe_allow_html=True
)

col_1, col_2 = st.columns([1.1,3.5])

with col_1:
    #foto
    with st.container(border=True):
        img_path = st.secrets.path_configuration['path_image']
        berkas_foto = "pasfoto.jpg"
        st.image(image=f"{img_path}{berkas_foto}")
    
    #nama
    with st.container(border=True):
        original_tittle = '<p style="font-family:Times New Roman; color:Black; font-size: 20px; font-weight: bold">Muhammad Raihan Permadi</p>'
        st.markdown(original_tittle, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">raihanpermadi18@gmail.com</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">linkedin.com/in/muhammadraihanpermadi/</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">+62 857-7600-3005</p>', unsafe_allow_html=True)
    
    #about_me
    with st.container(border=True):
        original_tittle = '<p style="font-family:Times New Roman; color:Black; font-size: 20px; font-weight: bold">About Me</p>'
        st.markdown(original_tittle, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">I am a fresh graduate third diploma degree of mechanical engineering at the State University of Jakarta. I have completed the fi eld work practice and the fi nal project as a requirement for graduation. I did fi eld work practice at PT. Mercindo Autorama as mechanic helper. In my fi nal project, I created a tool with the title "The Process of Making Refrigerators Using Solar Energy." My personality are discipline, meticulous, high curiosity level, quick learner, and can work under pressure. I can also work in groups or independent.</p>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown('<p style="font-family:Times New Roman; color:black; font-size: 16px;">📍Kebon Jeruk, West Jakarta City, Jakarta 11530, Indonesia</p>', unsafe_allow_html=True)

with col_2:
    #work_experiences
    with st.container(border=True):
        original_tittle = '<p style="font-family:Times New Roman; color:Grey; font-size: 20px; font-weight: bold">Work Experiences</p>'
        st.markdown(original_tittle, unsafe_allow_html=True)
        
        #kerja_1
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold">Promotion Staff • PT. Nuansa Bening Cipta (Next Communication) | South Jakarta, DKI Jakarta, Indonesia</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">July 2018 - August 2018</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- Photo session and editing products</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- Create content to promote products on social media</p>', unsafe_allow_html=True)
        
        #kerja_2
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold">Mechanic Helper • PT. Mercindo Autorama | South Jakarta, DKI Jakarta, Indonesia</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">February 2020 - March 2020</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- Helping the mechanic for maintenance for Mercedes Benz cars</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- Repairing mechanical and electrical damage for Mercedes Benz cars</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- Handle routine service for Mercedes Benz cars</p>', unsafe_allow_html=True)

        #kerja_3
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold">Quality Control • PT. Edico Utama (Teikin) | East Jakarta, DKI Jakarta, Indonesia</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">August 2022 - October 2022</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">- check the piston using a screw micrometer and indicator dial after going through the smooth oversize process</p>', unsafe_allow_html=True)

    
    #educations
    with st.container(border=True):
        original_tittle = '<p style="font-family:Times New Roman; color:Grey; font-size: 20px; font-weight: bold">Educations</p>'
        st.markdown(original_tittle, unsafe_allow_html=True)
        
        #sma
        with st.container():
            col_0, col_1, col_2 = st.columns([0.5,10,20])
            col_1.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">July 2014 - May 2017</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold;">SMA Negeri 85 Jakarta | Jakarta, DKI Jakarta, Indonesia</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">Natural Science</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">Activity : Martial Arts, Choir extracurricular</p>', unsafe_allow_html=True)

        #kuliah
        with st.container():
            col_0, col_1, col_2 = st.columns([0.5,10,20])
            col_1.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">August 2017 - March 2022</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold;">Universitas Negeri Jakarta | Jakarta, DKI Jakarta, Indonesia</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">Diploma Degree Mechanical Engineering</p>', unsafe_allow_html=True)
            col_2.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px;">Activity : Automotive Racing Team, Mechanical engineering student association</p>', unsafe_allow_html=True)

    #skills
    with st.container(border=True):
        original_tittle = '<p style="font-family:Times New Roman; color:Grey; font-size: 20px; font-weight: bold">Skills</p>'
        st.markdown(original_tittle, unsafe_allow_html=True)

        #soft_skills
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold">• Soft Skills</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px">Verbal Communication, Adaptive Positive Attitude, Self-Discipline, Focused, Meticulous, High Curiosity, Quick Learner, Work Under Pressure</p>', unsafe_allow_html=True)

        #soft_skills
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px; font-weight: bold">• Hard Skills</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 16px">Microsoft Office, AutoCAD, Adobe Premiere Pro, Adobe Photoshop, Welding SMAW, Computer Numerical Control (CNC), English Language</p>', unsafe_allow_html=True)
