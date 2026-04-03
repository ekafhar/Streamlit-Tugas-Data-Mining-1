import pickle
import streamlit as st
#membaca model
diabetes_model = pickle.load(open('prediksi_diabetes_svm.sav','rb'))
#Judul web
st.title('Data Mining Prediksi Diabetes')

#membuat kolom untuk menginpput data
col1, col2, col3, col4= st.columns(4)

with col1:
    Kehamilan = st.text_input ('Input Kehamilah')
with col1:
    Glukosa = st.text_input ('Input Glukosa')
with col2:
    Tekanan_Darah = st.text_input ('Input Tekanan Darah')
with col2:
    Ketebalan_Kulit = st.text_input ('Input Ketebalan Kulit')
with col3:
    Insulin = st.text_input ('Input insulin') 
with col3:
    BMI = st.text_input ('Input BMI')
with col4:
    Riwayat_Diabetes = st.text_input ('Input Riwayat Diabetes')
with col4:Umur = st.text_input ('Input Umur')
diabet = ''
#membuat printah untuk button     
if st.button('Prediksi Diabetes'):
    diabet = diabetes_model.predict([[Kehamilan, Glukosa, Tekanan_Darah, Ketebalan_Kulit, Insulin, BMI, Riwayat_Diabetes, Umur]])
    
    if(diabet[0] ==1 ):
        diabet ='Pasien Menderita Diabetes'
    else :
        diabet ='Pasien Tidak Menderita Diabetes'
    st.success(diabet)