import streamlit as st
st.set_page_config(page_title="Addition Studio", page_icon="➕", layout="centered")
st.markdown("""<style>
.stApp{background:#F2F7FF;color:#172B4D}.block-container{max-width:760px;padding-top:2.5rem}
.top{background:linear-gradient(120deg,#123B70,#2878C8);color:white;padding:30px;border-radius:20px;margin-bottom:24px}.top h1{color:white!important;margin:0;font-size:2.2rem}.top p{color:#DDEBFF!important;margin:.5rem 0 0}
.field-label{color:#17365D;font-weight:800;font-size:.95rem;margin:0 0 7px 2px}
div[data-testid="stNumberInput"] input{background:#fff!important;color:#102A43!important;-webkit-text-fill-color:#102A43!important;border:1px solid #9DBBE0!important;border-radius:12px!important}
div[data-testid="stNumberInput"] button{color:#17365D!important}div[data-testid="stForm"]{background:white;padding:24px;border:1px solid #D5E5F7;border-radius:18px}
div[data-testid="stFormSubmitButton"] button{background:#1769AA;color:white!important;border:0;border-radius:12px;font-weight:800;min-height:3rem}
.answer{background:white;border:1px solid #C7DDF7;border-radius:18px;padding:22px;margin-top:20px}.answer small{color:#52749B;font-weight:800;text-transform:uppercase;letter-spacing:.1em}.answer strong{display:block;color:#123B70;font-size:2.6rem;margin-top:5px;overflow-wrap:anywhere}
</style>""", unsafe_allow_html=True)
st.markdown('<div class="top"><h1>＋ Addition Studio</h1><p>Two numbers. One precise answer.</p></div>', unsafe_allow_html=True)
with st.form("addition_form"):
    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="field-label">FIRST NUMBER</div>',unsafe_allow_html=True)
        a=st.number_input("First number",value=12.0,step=1.0,label_visibility="collapsed",key="add_a")
    with c2:
        st.markdown('<div class="field-label">SECOND NUMBER</div>',unsafe_allow_html=True)
        b=st.number_input("Second number",value=8.0,step=1.0,label_visibility="collapsed",key="add_b")
    submitted=st.form_submit_button("Calculate sum  →",use_container_width=True)
if submitted:
    total=a+b
    shown=f"{total:,.4f}".rstrip("0").rstrip(".") if total%1 else f"{total:,.0f}"
    st.markdown(f'<div class="answer"><small>Final sum</small><strong>{shown}</strong><div>{a:g} + {b:g} = {shown}</div></div>',unsafe_allow_html=True)
else: st.caption("Enter your values above, then calculate the sum.")
st.markdown('<p style="text-align:center;color:#7892B2;font-size:.8rem;margin-top:28px">ADDITION STUDIO · ASSIGNMENT 01</p>',unsafe_allow_html=True)
