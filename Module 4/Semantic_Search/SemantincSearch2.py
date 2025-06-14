import streamlit as st
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import scipy.spatial






def main():
     # Settings
    st.set_page_config(layout="wide", page_title='Paris Hotel Finder', page_icon="🎈"   )
    from string import punctuation
    punctuation=punctuation+ '\n'
    
    from sentence_transformers import SentenceTransformer, util
    import torch
    import numpy as np
    import pandas as pd
    from sentence_transformers import SentenceTransformer
    import scipy.spatial

    from sentence_transformers import SentenceTransformer, util
    import torch
    
    @st.cache(allow_output_mutation=True)
    def load_model():
        return SentenceTransformer('all-MiniLM-L6-v2'),SentenceTransformer('multi-qa-MiniLM-L6-cos-v1'),CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    embedder,bi_encoder,cross_encoder = load_model()
    
    st.title("Hotel Search Engine")
    with st.expander("ℹ️ - About this app", expanded=True):
        st.write(
            """
            -   This is a hotel search engine that allows users to enter free text query to make the search result personalized to user preference as opposed to other travel websites where a user has to spend hours going through hotel list.
            -   We use natural language processing and big data to return results customized for your preferences.
            """
        )
        
    punctuation=punctuation+ '\n'
    
    def lower_case(input_str):
        input_str = input_str.lower()
        return input_str
    
    
    
    
    