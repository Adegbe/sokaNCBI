import streamlit as st
import requests
from Bio import Entrez

# Set email for NCBI Entrez
Entrez.email = "adegbesamson@gmail.com"

# Streamlit UI
st.title("🔬 NCBI Database Query Tool")
st.markdown("Query NCBI databases (nucleotide, protein, genome, pubmed, taxonomy) using accession numbers.")

# Sidebar Inputs
st.sidebar.header("Query Parameters")

# Database selection
database_options = ["nucleotide", "protein", "genome", "pubmed", "taxonomy"]
selected_db = st.sidebar.selectbox("Select a Database", database_options)

# Accession number input
accession = st.sidebar.text_input("Enter Accession Number", "NM_021803.4")

# Query button
if st.sidebar.button("Query NCBI"):
    if selected_db and accession:
        st.write(f"### Results for `{accession}` in `{selected_db}` database")
        try:
            with st.spinner("Fetching data from NCBI..."):
                handle = Entrez.efetch(db=selected_db, id=accession, rettype="gb", retmode="text")
                result = handle.read()
                handle.close()

            st.text_area("NCBI Result", result, height=400)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please select a database and enter an accession number.")
