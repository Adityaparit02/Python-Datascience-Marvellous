import streamlit as st
st.set_page_config(page_title="Interest Planner", page_icon="₹", layout="centered")
st.markdown("""<style>
.stApp{background:#F0F8F3;color:#163A2A}.block-container{max-width:820px;padding-top:2.2rem}.finance-head{background:#174D37;color:white;padding:28px;border-radius:8px 8px 8px 28px;margin-bottom:22px}
.finance-head .tag{color:#A7F3D0;font-size:.76rem;font-weight:800;letter-spacing:.16em}.finance-head h1{color:white!important;margin:.45rem 0;font-size:2.15rem}.finance-head p{color:#D1FAE5!important;margin:0}
.field-label{color:#174D37;font-size:.88rem;font-weight:800;margin-bottom:7px}div[data-testid="stNumberInput"] input{background:white!important;color:#163A2A!important;-webkit-text-fill-color:#163A2A!important;border:1px solid #A7CDB8!important;border-radius:8px!important}div[data-testid="stNumberInput"] button{color:#174D37!important}
div[data-testid="stForm"]{background:white;padding:24px;border:1px solid #CDE5D6;border-radius:14px}div[data-testid="stFormSubmitButton"] button{background:#19734E;color:white!important;border:0;border-radius:8px;font-weight:800;min-height:3rem}
.summary{background:#174D37;color:white;padding:23px;border-radius:14px;margin-top:20px}.summary .caption{color:#A7F3D0;text-transform:uppercase;font-size:.76rem;font-weight:800;letter-spacing:.12em}.summary .amount{color:white;font-size:2.45rem;font-weight:900}.summary p{color:#D1FAE5!important;margin-bottom:0}
.stApp [data-testid="stMetricLabel"],.stApp [data-testid="stMetricLabel"] p{color:#426653!important}.stApp [data-testid="stMetricValue"],.stApp [data-testid="stMetricValue"] div{color:#174D37!important}
</style>""",unsafe_allow_html=True)
st.markdown('<div class="finance-head"><div class="tag">PERSONAL FINANCE · TOOL 03</div><h1>Simple Interest Planner</h1><p>Estimate interest and the final amount using a fixed annual rate.</p></div>',unsafe_allow_html=True)
with st.form("interest_form"):
    st.markdown('<div class="field-label">PRINCIPAL AMOUNT (₹)</div>',unsafe_allow_html=True)
    principal=st.number_input("Principal amount",min_value=0.0,value=10000.0,step=500.0,format="%.2f",label_visibility="collapsed")
    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="field-label">ANNUAL RATE (%)</div>',unsafe_allow_html=True)
        rate=st.number_input("Annual rate",min_value=0.0,value=7.5,step=0.25,format="%.2f",label_visibility="collapsed")
    with c2:
        st.markdown('<div class="field-label">TIME PERIOD (YEARS)</div>',unsafe_allow_html=True)
        years=st.number_input("Time period",min_value=0.0,value=2.0,step=0.5,format="%.2f",label_visibility="collapsed")
    calculate=st.form_submit_button("Calculate return  →",use_container_width=True)
if calculate:
    interest=principal*rate*years/100; total=principal+interest
    st.markdown(f'<div class="summary"><div class="caption">Calculated simple interest</div><div class="amount">₹{interest:,.2f}</div><p>Principal × Rate × Time ÷ 100</p></div>',unsafe_allow_html=True)
    c1,c2=st.columns(2); c1.metric("Principal",f"₹{principal:,.2f}"); c2.metric("Final amount",f"₹{total:,.2f}")
else: st.caption("Simple interest does not compound interest on previously earned interest.")
st.markdown('<p style="text-align:center;color:#648574;font-size:.78rem;margin-top:28px">INTEREST PLANNER · ASSIGNMENT 03</p>',unsafe_allow_html=True)
