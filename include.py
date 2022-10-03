import streamlit as st

def espace(n):
    """
    Cette fonction ne renvoie rien mais affiche n ligne vide
    dans une application streamlit.
    """
    for _ in range(n):
        st.write("")
    return None

def is_colorful(n):
    nb_string = str(n)
    N = len(nb_string)  
    if N == 1:
        return ([n], True)
    my_list_of_prod = [ int(x) for x in nb_string ]
    #---------------------------------------------------------------------------
    # We will add the products of 2 consecutive digits, of 3 consecutive 
    # digits, ... and the last product with all the digits in n.
    #--------------------------------------------------------------------------- 
    for nb_of_dig in range(2, N+1):
        for start in range(0, N-nb_of_dig+1):
            product = 1
            for k in range(start, start+nb_of_dig):
                product *= int(nb_string[k])
            my_list_of_prod.append(product)
    my_set_of_prod = set(my_list_of_prod)
    my_bool = (len(my_set_of_prod) == len(my_list_of_prod))
    return (my_list_of_prod, my_bool)

