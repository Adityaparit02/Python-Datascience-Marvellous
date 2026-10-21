import streamlit as st
st.set_page_config(page_title="Temperature Lab", page_icon="🌡️", layout="centered")
st.markdown("""<style>
.stApp{background:#ECFEFF;color:#164E63}.block-container{max-width:760px;padding-top:2.5rem}.temp-header{display:flex;align-items:center;gap:18px;padding:10px 0 22px;border-bottom:1px solid #A5F3FC;margin-bottom:24px}
.thermo{background:#CFFAFE;border-radius:18px;width:76px;height:76px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;flex-shrink:0}.temp-header h1{color:#155E75!important;margin:0;font-size:2rem}.temp-header p{color:#0E7490!important;margin:.35rem 0 0}
.field-label{color:#155E75;font-weight:900;font-size:.9rem;margin-bottom:8px}div[data-testid="stNumberInput"] input{background:white!important;color:#164E63!important;-webkit-text-fill-color:#164E63!important;border:1px solid #67E8F9!important;border-radius:14px!important;font-size:1.1rem!important}div[data-testid="stNumberInput"] button{color:#155E75!important}
div[data-testid="stForm"]{background:white;padding:24px;border:1px solid #A5F3FC;border-radius:22px}div[data-testid="stFormSubmitButton"] button{background:#0891B2;color:white!important;border:0;border-radius:14px;font-weight:900;min-height:3.2rem}
.convert-result{margin-top:22px;background:#155E75;border-radius:22px;padding:28px;color:white;text-align:center}.convert-result .overline{color:#A5F3FC;font-weight:900;font-size:.78rem;letter-spacing:.14em}.convert-result .temperature{color:white;font-size:2.8rem;font-weight:900;margin:.35rem 0}.convert-result .equation{color:#CFFAFE}
.scale-row{display:flex;justify-content:space-between;gap:10px;margin-top:16px}.scale{flex:1;background:#CFFAFE;border-radius:12px;padding:12px;text-align:center;color:#155E75}.scale b{display:block;font-size:1.1rem}
</style>""",unsafe_allow_html=True)
st.markdown('<div class="temp-header"><div class="thermo">🌡</div><div><h1>Temperature Lab</h1><p>Celsius → Fahrenheit conversion</p></div></div>',unsafe_allow_html=True)
with st.form("temperature_form"):
    st.markdown('<div class="field-label">TEMPERATURE IN CELSIUS (°C)</div>',unsafe_allow_html=True)
    celsius=st.number_input("Celsius temperature",value=25.0,step=1.0,format="%.2f",label_visibility="collapsed")
    convert=st.form_submit_button("Convert temperature  →",use_container_width=True)
if convert:
    fahrenheit=(celsius*9/5)+32
    st.markdown(f'<div class="convert-result"><div class="overline">CONVERTED TEMPERATURE</div><div class="temperature">{fahrenheit:.2f} °F</div><div class="equation">({celsius:.2f} × 9/5) + 32</div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="scale-row"><div class="scale"><span>CELSIUS</span><b>{celsius:.2f} °C</b></div><div class="scale"><span>FAHRENHEIT</span><b>{fahrenheit:.2f} °F</b></div></div>',unsafe_allow_html=True)
else: st.info("Type a temperature in Celsius, then select Convert temperature.")
st.markdown('<p style="text-align:center;color:#0E7490;font-size:.78rem;margin-top:30px">TEMPERATURE LAB · ASSIGNMENT 05</p>',unsafe_allow_html=True)
