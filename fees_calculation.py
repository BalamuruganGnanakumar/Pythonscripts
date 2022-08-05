import streamlit as st
a=10000
r=0.07
y=0
while(a<20000):
    a=a+a*0.07
    y=y+1
st.write("After",y,"Years the fees will be",a)
