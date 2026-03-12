import streamlit as st
import requests

st.title("⚰️ De Doodlijn")
st.write("De binaire autoriteit op het gebied van BN-status.")

# Invoerveld
naam = st.text_input("Voer de naam van een BN'er in:")

if st.button("Check Status"):
    if naam:
        
        # Zoek op Wikidata
        url = "https://www.wikidata.org/w/api.php"
        params = {"action": "wbsearchentities", "language": "nl", "format": "json", "search": naam}
        
        # Voeg dit toe om de Mac-blokkade te omzeilen:
        headers = {'User-Agent': 'DoodlijnApp/1.0 (contact: info@doodlijn.nl)'}
        
        res = requests.get(url, params=params, headers=headers).json()
        
        if res.get('search'):
            id = res['search'][0]['id']
            # Haal details op
            # Haal details op (met de headers voor legitimatie)
            data_url = f"https://www.wikidata.org/wiki/Special:EntityData/{id}.json"
            data = requests.get(data_url, headers=headers).json()
            claims = data['entities'][id].get('claims', {})
            if 'P570' in claims:
                st.error(f"STATUS: OVERLEDEN")
            else:
                st.success(f"STATUS: IN LEVEN")
        else:
            st.warning("Geen data gevonden.")