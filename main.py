import streamlit as st

st.set_page_config(page_title="Pivot Calculator", layout="centered")
st.title("Pivot Point Calculator")

col1, col2, col3 = st.columns(3)
with col1:
    H = st.number_input("Enter High:", value=0.0, format="%.2f")
with col2:
    L = st.number_input("Enter Low:", value=0.0, format="%.2f")
with col3:
    C = st.number_input("Enter Close:", value=0.0, format="%.2f")

if H > 0 and L > 0 and C > 0:
    Pivot = (H + L + C) / 3
    R1 = (2 * Pivot) - L
    S1 = (2 * Pivot) - H
    X = H - L
    R2 = Pivot + X
    S2 = Pivot - X
    R3 = H + 2 * (Pivot - L)
    S3 = L - 2 * (H - Pivot)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pivot", f"{Pivot:.2f}")
    with col2:
        st.metric("R1", f"{R1:.2f}")
    with col3:
        st.metric("S1", f"{S1:.2f}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("R2", f"{R2:.2f}")
    with col2:
        st.metric("S2", f"{S2:.2f}")
    with col3:
        st.metric("S3", f"{S3:.2f}")
    
    st.metric("R3", f"{R3:.2f}")

S3 = L - 2*(H-Pivot)
print("Support 3: {:.2f}".format(S3))



