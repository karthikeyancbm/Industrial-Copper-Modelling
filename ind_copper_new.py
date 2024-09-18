import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from datetime import date

with open("Regression_Model.pkl","rb") as r1:
  regg_model=pickle.load(r1)

with open("model.pkl","rb") as ft:
    ml = pickle.load(ft)  


status_list = ['won','draft','to be approved','lost','not lost for am','wonderful','revised','offered','offerable']

item_list = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']


def sell_price(input_data):
    
    input_data_array = np.array([[input_data]])
    sell_price_pred = regg_model.predict(input_data)
    return sell_price_pred

def status_pred(user_data):
    user_data_array = np.array([[user_data]])
    stat_prediction = ml.predict(user_data)
    if stat_prediction[0] == 1:
        return "Won"
    else:
        return "Lost"
    

st.set_page_config(layout="wide")

title_text = '''<h1 style='font-size: 55px;text-align: center;color:purple;background-color: lightgrey;'>Industrial Copper Modelling</h1>'''
st.markdown(title_text, unsafe_allow_html=True)


with st.sidebar:
   
   select = option_menu("MAIN MENU",['HOME','ABOUT','PREDICTION'])

if select == 'HOME':

  col1,col2 = st.columns(2)

  with col1:

    st.write(" ")
    st.write(" ")   
    st.header(":blue[Copper - A Brief Overview]")

    with st.container(border=True):
      st.markdown('''<h5 style='color:#00ffff;font-size:21px'>Copper is a reddish-brown metal known for its high electrical and thermal conductivity.<br>
                    It is one of the oldest metals used by humans, with historical evidence dating back thousands of years.
                    Copper is malleable, ductile, and resistant to corrosion, making it useful in various industries, especially in electrical wiring, plumbing, and electronics.<br>
                    Due to its excellent conductivity, copper is a critical component in power generation and transmission systems.<br>
                    It is also used in alloys like bronze (copper and tin) and brass (copper and zinc) for various mechanical and aesthetic applications.<br>
                    Copper is widely mined across the world, with major producers including Chile, the U.S., and Peru.''', unsafe_allow_html=True)
    st.write(" ")
    st.header(":blue[Copper Usage:]")
    with st.container(border=True):     
      st.markdown('''<h6 style ='color:#ff1a66;font-size:21px'>Copper is widely used across multiple industries due to its excellent electrical and thermal conductivity, corrosion resistance, and malleability.<br>
                  Copper is used across various industries in the following approximate percentages:<br>
                  1.Electrical and Electronics Industry - 40%: This includes electrical wiring, power generation, transmission systems, and electronic components.<br>
                  2.Construction Industry - 30%: Copper is used in plumbing, roofing, cladding, and building infrastructure.<br>
                  3.Transportation Industry - 12%: Used in automobiles (wiring, radiators, motors), aircraft, and trains.<br>
                  4.Consumer Products - 12%: Includes appliances, cookware, and other household goods.<br>
                  5.Industrial Machinery - 6%: Used in machinery, heat exchangers, and industrial equipment.''',unsafe_allow_html=True)
  with col2:
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.image('copper_1.png')
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.video("https://www.youtube.com/watch?v=gqmkiPPIsUQ")

  
     
  st.link_button(":violet[** Copper Wikipedia Link**]",url="https://en.wikipedia.org/wiki/Copper",use_container_width=True)

if select == 'ABOUT':
   
    st.write(" " )
    st.write(" ")

    st.markdown('''<h6 style ='color:#ff1a66;font-size:31px'><br>Project Title : Industrial Copper Modelling''',unsafe_allow_html=True)

    
    st.markdown('''<h6 style ='color:#007acc;font-size:31px'><br>Domain : Manufacturing''',unsafe_allow_html=True)

    
    st.markdown('''<h6 style ='color:#b3b300;font-size:31px'><br>
                Take away Skills : <br>Python Scipting<br>Data Preprocessing<br>EDA<br>Model Building<br>Model Deployment in Streamlit''',unsafe_allow_html=True)

    st.markdown('''<h6 style ='color:#2d8659;font-size:31px'><br>Objective:<br>Build a Regression Model to predict the Selling Price<br>Build a Classfication
                Model to evaluate and classify the Leads''',unsafe_allow_html=True)

  

elif select == 'PREDICTION':

  title_text = '''<h1 style='font-size: 32px;text-align: center;color:#00ff80;'>Selling Price Prediction and Status Prediction</h1>'''
  st.markdown(title_text, unsafe_allow_html=True)

  st.markdown("""
<style>

	.stTabs [role="tab"] {font-size: 32px;
		gap: 2px;
    }

	.stTabs [role="tab"] {
		height: 40px;
        white-space: pre-wrap;
		background-color: #C0C0C0;
		border-radius: 4px 4px 0px 0px;
		gap: 10px;
    padding-top: 10px;
		padding-bottom: 10px;
    padding: 30px 40px;
    width: 800px
    }

	.stTabs [aria-selected="true"] {
  		background-color: #C0C0C0;
      color:red;font-weight:bold;
      font-size: 31px;
	}

</style>""", unsafe_allow_html=True)
  
  st.markdown("""
    <style>
    .stTabs [role="tab"] {
        font-size: 64px;  
        padding: 10px 20px;  
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b;  
        color: black;  
        font-weight: bold; 
    }
    </style>
    """, unsafe_allow_html=True)

   
  
  tab1,tab2 = st.tabs(['Selling Price Prediction','Status Prediction'])

  
  with tab1:

    st.markdown("<h5 style=color:grey>To predict the selling price of copper, please provide the following information:",unsafe_allow_html=True)
    st.write('')

    col1,col2 = st.columns(2)

    with col1:

      item_date = st.date_input('Item_Date',value=None,format='YYYY-MM-DD')

      quantity_tons = st.number_input('Quantity', key= 'quantity_tons')

      customer = st.number_input('Customer',key='customer')

      country = st.number_input('Country')

      status = st.selectbox('Status',status_list,index=None)

      item_type = st.selectbox('Item_type',item_list,index=None)

    with col2:

      application = st.number_input('Application')

      thickness = st.number_input('Thickness')

      width = st.number_input('Width')    

      product_ref = st.number_input('Product_Ref')

      delivery_date = st.date_input('Delivery_Date',value=None,format='YYYY-MM-DD')

      lead_time = st.number_input('Lead_Time')


      prediction = ' '

      if st.button(':violet[Predict]',use_container_width=True):

        status_list = ['won','draft','to be approved','lost','not lost for am','wonderful','revised','offered','offerable']
        status_encoded = {'lost':0, 'won':1, 'draft':2, 'to be approved':3, 'not lost for am':4,'wonderful':5, 'revised':6,
                          'offered':7, 'offerable':8}
        status = status_encoded[status]

        item_list = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']

        item_type_encoded = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}

        item_type = item_type_encoded[item_type]
        
    
        prediction = sell_price([[quantity_tons,customer,country,status,item_type,application,thickness,width,product_ref,lead_time]])
    
        st.subheader((f":green[Predicted Selling Price :] {prediction[0]:.2f}"))
    
    with tab2:

      st.markdown("<h5 style=color:grey;>To predict the status of copper, please provide the following information:",unsafe_allow_html=True)
      st.write('')

      col1,col2 = st.columns(2)

      with col1:

        item_date = st.date_input('item_Date',value=None,format='YYYY-MM-DD')
   
        quantity_tons = st.number_input('quantity')

        customer = st.number_input('customer')

        country = st.number_input('country')

        selling_price = st.number_input('selling_Price')

        item_type = st.selectbox('item_type',item_list,index=None)

      with col2:

        application = st.number_input('application')

        thickness = st.number_input('thickness')

        width = st.number_input('width')

        product_ref = st.number_input('product_Ref')

        delivery_date = st.date_input('delivery_Date',value=None,format='YYYY-MM-DD')

        lead_time = st.number_input('lead_Time')

        prediction = ' '

        if st.button(':violet[Status_Predict]',use_container_width=True):

          item_list = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']

          item_type_encoded = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}

          item_type = item_type_encoded[item_type]
          
          prediction = status_pred([[quantity_tons,customer,country,selling_price,item_type,application,thickness,width,product_ref,lead_time]])
      with col1:
        st.subheader((f":blue[Predicted Status :] {prediction}"))
          

   


   






