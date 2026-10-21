import streamlit as st
st.set_page_config(page_title="Student Scorecard", page_icon="🎓", layout="centered")
st.markdown("""<style>
.stApp{background:#FFF7ED;color:#432A1D}.block-container{max-width:850px;padding-top:2.2rem}.school-top{text-align:center;padding:10px 10px 22px;border-bottom:2px solid #FED7AA;margin-bottom:22px}
.school-top .badge{display:inline-block;background:#FFEDD5;color:#9A3412;padding:6px 12px;border-radius:99px;font-size:.75rem;font-weight:900;letter-spacing:.1em}.school-top h1{color:#7C2D12!important;margin:.7rem 0 .3rem;font-size:2.3rem}.school-top p{color:#9A6042!important;margin:0}
.field-label{color:#7C2D12;font-weight:800;font-size:.88rem;margin-bottom:7px}div[data-testid="stTextInput"] input,div[data-testid="stNumberInput"] input{background:white!important;color:#431407!important;-webkit-text-fill-color:#431407!important;border:1px solid #FDBA74!important;border-radius:10px!important}div[data-testid="stNumberInput"] button{color:#7C2D12!important}
div[data-testid="stForm"]{background:white;padding:24px;border:1px solid #FED7AA;border-radius:18px}div[data-testid="stFormSubmitButton"] button{background:#C2410C;color:white!important;border:0;border-radius:10px;font-weight:800;min-height:3rem}
.scorecard{background:white;border:1px solid #FDBA74;border-radius:18px;padding:22px;margin-top:20px}.scorecard h3{color:#7C2D12!important;margin-top:0}.pass{background:#DCFCE7;color:#166534;padding:13px 16px;border-radius:10px;font-weight:900}.fail{background:#FEE2E2;color:#991B1B;padding:13px 16px;border-radius:10px;font-weight:900}
.stApp [data-testid="stMetricLabel"],.stApp [data-testid="stMetricLabel"] p{color:#9A3412!important}.stApp [data-testid="stMetricValue"],.stApp [data-testid="stMetricValue"] div{color:#7C2D12!important}
</style>""",unsafe_allow_html=True)
st.markdown('<div class="school-top"><span class="badge">ACADEMIC RECORD · 04</span><h1>Student Scorecard</h1><p>Three subjects · 300 total marks · 40 marks minimum per subject</p></div>',unsafe_allow_html=True)
with st.form("student_form"):
    st.markdown('<div class="field-label">STUDENT NAME</div>',unsafe_allow_html=True)
    name=st.text_input("Student name",placeholder="Enter the student's full name",label_visibility="collapsed")
    st.markdown('<div class="field-label" style="margin-top:16px">SUBJECT MARKS (OUT OF 100)</div>',unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c1:
        st.markdown('<div class="field-label">SUBJECT 1</div>',unsafe_allow_html=True); m1=st.number_input("Subject 1 marks",min_value=0,max_value=100,value=0,step=1,label_visibility="collapsed")
    with c2:
        st.markdown('<div class="field-label">SUBJECT 2</div>',unsafe_allow_html=True); m2=st.number_input("Subject 2 marks",min_value=0,max_value=100,value=0,step=1,label_visibility="collapsed")
    with c3:
        st.markdown('<div class="field-label">SUBJECT 3</div>',unsafe_allow_html=True); m3=st.number_input("Subject 3 marks",min_value=0,max_value=100,value=0,step=1,label_visibility="collapsed")
    submit=st.form_submit_button("Generate scorecard  →",use_container_width=True)
if submit:
    if not name.strip(): st.error("Please enter the student's name.")
    else:
        total=m1+m2+m3; percentage=total/3; passed=min(m1,m2,m3)>=40
        st.markdown(f'<div class="scorecard"><h3>{name.strip()}</h3><p style="color:#9A6042">RESULT SUMMARY</p></div>',unsafe_allow_html=True)
        c1,c2=st.columns(2); c1.metric("Total marks",f"{total} / 300"); c2.metric("Percentage",f"{percentage:.2f}%")
        if passed: st.markdown('<div class="pass">PASS · Minimum marks achieved in all subjects</div>',unsafe_allow_html=True)
        else:
            failed=[f"Subject {i}" for i,mark in enumerate((m1,m2,m3),start=1) if mark<40]
            st.markdown(f'<div class="fail">FAIL · Below 40 marks in: {", ".join(failed)}</div>',unsafe_allow_html=True)
else: st.caption("A student must score at least 40/100 in every subject to pass.")
st.markdown('<p style="text-align:center;color:#B77952;font-size:.78rem;margin-top:28px">STUDENT SCORECARD · ASSIGNMENT 04</p>',unsafe_allow_html=True)
