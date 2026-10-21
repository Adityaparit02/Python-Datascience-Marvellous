import streamlit as st
st.set_page_config(page_title="Parity Lab", page_icon="◐", layout="centered")
st.markdown("""<style>
.stApp{background:#17152B;color:#F5F3FF}.block-container{max-width:700px;padding-top:2.5rem}.lab-head{border-bottom:1px solid #454064;padding-bottom:20px;margin-bottom:24px}
.kicker{color:#B8A8FF;font-weight:800;letter-spacing:.18em;font-size:.75rem}.lab-head h1{color:white!important;font-size:2.35rem;margin:.35rem 0}.lab-head p{color:#C6C2DF!important}
.field-label{color:#E5DEFF;font-size:.9rem;font-weight:800;margin-bottom:8px}div[data-testid="stNumberInput"] input{background:#262342!important;color:white!important;-webkit-text-fill-color:white!important;border:1px solid #655B91!important;border-radius:12px!important}div[data-testid="stNumberInput"] button{color:white!important}
div[data-testid="stForm"]{background:#211E3A;border:1px solid #454064;padding:24px;border-radius:18px}div[data-testid="stFormSubmitButton"] button{background:#8B72F8;color:white!important;border:0;border-radius:12px;font-weight:800;min-height:3rem}
.result{margin-top:22px;padding:28px;border-radius:18px;text-align:center;background:#211E3A;border:1px solid #454064}.result .big{font-size:3.1rem;line-height:1.2;font-weight:900;color:#C4B5FD}.result .sub{color:#D4D0E8;margin-top:8px}div[data-testid="stAlert"]{background:#211E3A;color:white}
</style>""",unsafe_allow_html=True)
st.markdown('<div class="lab-head"><div class="kicker">NUMBER THEORY / LAB 02</div><h1>Parity Lab</h1><p>Investigate whether an integer is even or odd.</p></div>',unsafe_allow_html=True)
with st.form("parity_form"):
    st.markdown('<div class="field-label">INTEGER TO TEST</div>',unsafe_allow_html=True)
    number=st.number_input("Integer to test",value=17,step=1,format="%d",label_visibility="collapsed")
    check=st.form_submit_button("Analyse integer  ↗",use_container_width=True)
if check:
    n=int(number); kind="EVEN" if n%2==0 else "ODD"; explanation="Divisible by 2 with no remainder." if n%2==0 else "Leaves a remainder of 1 when divided by 2."
    st.markdown(f'<div class="result"><div class="kicker">RESULT FOR {n}</div><div class="big">{kind}</div><div class="sub">{explanation}</div></div>',unsafe_allow_html=True)
else: st.info("The result will appear here after analysis.")
st.markdown('<p style="text-align:center;color:#9992C4;font-size:.78rem;margin-top:30px">PARITY LAB · ASSIGNMENT 02</p>',unsafe_allow_html=True)
