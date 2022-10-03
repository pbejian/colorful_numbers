#-------------------------------------------------------------------------------
# Importation des modules

import streamlit as st
import include as inc

#-------------------------------------------------------------------------------
# Application principale

st.title("Colorful numbers")

st.write("""
    ### Test if an integer is "colorful" (see the GitHub repo for details) 
    """)

inc.espace(1)

n = int(st.text_input("Choose an integer n and validate : ", 1))
L, b = inc.is_colorful(n)

st.write(f"""
    The list of the products of subsequences of n is : {L}
"""
)

if b:
    st.write(f"No repetition: the integer {n} is **colorful**.")
else:
    st.write(f"There is a repetition: the integer {n} is not **colorful**.")    

#-------------------------------------------------------------------------------
# Conclusion avec le lien vers les sources sur GitHub

st.markdown("""
    <hr>
""", unsafe_allow_html=True)

inc.espace(2)

st.write("""
    📝 Sources of the app:
    [https://github.com/pbejian/colorful_numbers](https://github.com/pbejian/colorful_numbers)
""")
#-------------------------------------------------------------------------------