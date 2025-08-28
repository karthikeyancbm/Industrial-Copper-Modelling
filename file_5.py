import pandas as pd
import numpy as np
import re
import os
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import streamlit_option_menu
from streamlit_option_menu import option_menu
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import date
from selenium.webdriver.common.keys import Keys
import easyocr
import warnings
warnings.filterwarnings('ignore')
import  matplotlib.pyplot as plt
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
import math
import re
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.alert import Alert

st._config.set_option('themebase','dark')

st.set_page_config(layout='wide')

file = st.file_uploader ("Upload the file",type=['xlsx','xlsm','xls'])

if 'data_d' not in st.session_state:

    st.session_state['data_d'] = {}

if st.button('Submit'):

    if file is not None:

        file_path = file

        xls = pd.ExcelFile(file_path)

        df =pd.read_excel(file_path,sheet_name=xls.sheet_names[-1],header=None)

        st.write("Last sheet loaded successfully")

        df = df.dropna(how="all",axis=0).dropna(how="all",axis=1)
        df =df.reset_index(drop=True)
        df.iloc[:,0] = df.iloc[:,0].astype(str).str.replace(r"[\n\t]+"," ",regex=True).str.strip()

        new_lst = [df.loc[j,i] for i in df.columns for j in df.index]
        new_lst = [str(i).replace('\n','') for i in new_lst]
        new_lst = [x for x in new_lst if x != 'nan']
        

        gst = ''
        for i in new_lst:
            if str(i).isalnum():
                if str(i).endswith('J'):
                    gst = gst+str(i)

        hsn_lst =[]
        for i in new_lst:
            if str(i).isdigit():
                if str(i).startswith('7'):
                    hsn_lst.append(str(i))

        hsn_lst = hsn_lst.pop()

        st.session_state['data_d']['hsn_no']= hsn_lst

        unit_lst = ""
        for i in new_lst:
            if str(i).startswith('Gross'):
                unit_lst = unit_lst+i
        ind = unit_lst.find('Gms')
        ind_1 = unit_lst[ind:]
        ind_2 = "".join(re.findall('[a-zA-Z]',ind_1))
        
        st.session_state['data_d']['units'] = ind_2

        for i in new_lst:
            if 'STOCK' in str(i):
                stock_str = str(i)
        st_1 = " ".join(stock_str[stock_str.find('STOCK'):].split(" ")[0:2])
        
        st.session_state['data_d']['sub_type'] = st_1

        ornaments_lst = []
        for i in new_lst:
            if 'ORNAMENTS' in str(i):
                ornaments_lst.append(i)
        if len(ornaments_lst)>1:
            ornments = ornaments_lst.pop()
            ornaments_lst_1 = "".join(ornaments_lst)
            print(ornaments_lst_1)
        else:
            ornaments_lst_1 = "".join(ornaments_lst)

        st.session_state['data_d']['item'] = ornaments_lst_1

        new_d = {i:col for i,col in enumerate(new_lst)}

        gross_wt = ''
        for x in new_d:
            if new_d[x].startswith('Gross'):        
                gross_wt = gross_wt+new_d[x+1]
        
        st.session_state['data_d']['gross_wt'] = gross_wt

        value = ''
        for x in new_d:
            if new_d[x].startswith('Value of Supply'):        
                value = value+new_d[x+1]
        value_1 = float(value)
        value_2 = round(value_1,2)
        value_3 = str(value_2)
        value = value_3

        st.session_state['data_d']['value'] = value

        for x in new_d:
            if 'DC' in new_d[x]:
                doc_no = new_d[x]
        doc_no_1 = doc_no.split("-")
        doc_no_2 = [i.strip() for i in doc_no_1]
        doc_no_2.remove('DC')
        doc_no_3 = "-".join(doc_no_2)

        st.session_state['data_d']['doc_no'] = doc_no_3
        
        for x in new_d:
            if 'MADURAI - HO' in new_d[x]:
                address =  new_d[x+1]
        ad = address.split(",")
        add_1 = ad[0].strip()
        add_2 = ad[1].strip()
        
        st.session_state['data_d']['from_office_add_1'] = add_1
        st.session_state['data_d']['from_office_add_2'] = add_2
        
        for x in new_d:
            if '625016' in new_d[x]:
                city = new_d[x]
        cty = city.split("-")
        place= cty[0].strip()
        pin_code = cty[1].strip()
        
        st.session_state['data_d']['from_city'] = place
        st.session_state['data_d']['from_city_pincode'] = pin_code
        
        to_office = []
        for x in new_d:
            if "BHIMA" in new_d[x]:
                to_office.append(new_d[x])
        for i in to_office:
            if 'HO' in i:
                to_office.remove(i)
        to_office_1 = "".join(to_office).strip()
        
        st.session_state['data_d']['to_office'] = to_office_1

        for  x in new_d:
            if to_office_1 in new_d[x]:
                to_office_add_1 = new_d[x+1].strip()
        
        st.session_state['data_d']['to_office_add_1'] = to_office_add_1

        city_lst =['MADURAI','RAJAPALAYAM','DINDIGUL','TRICHY','SALEM']

        for  x in new_d:
            if to_office_1 in new_d[x]:
                to_office_add_2 = new_d[x+2].strip()
        
        st.session_state['data_d']['to_office_add_2'] = to_office_add_2

        for  x in new_d:
            if to_office_add_2 in new_d[x]:
                to_office_city = new_d[x+1].strip()
        
        st.session_state['data_d']['to_office_city'] = to_office_city

        if st.session_state['data_d']['to_office_add_2'] in city_lst:
            st.session_state['data_d']['to_office_city'] = st.session_state['data_d'].pop('to_office_add_2')
            st.session_state['data_d']['to_office_pincode']  = st.session_state['data_d'].pop('to_office_city')

        
        
        st.success("✅ File processed and dictionary stored.")
        
        df_1= pd.DataFrame(list(st.session_state['data_d'].items()),columns=['Items','Values'])
        st.dataframe(df_1)    

if st.button('Eway'):

    if 'driver' not in st.session_state:

        chrome_options = Options()           
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)    
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        st.session_state['driver'] = webdriver.Chrome(service=Service(r"C:\Users\DELL\Documents\eway\chromedriver-win64\chromedriver.exe"), options=chrome_options)
        driver = st.session_state['driver']   
        driver.get("https://ewaybillgst.gov.in")
        wait =WebDriverWait(driver,20)

    # 2. Click login click

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Login")))
        login_link.click()

        # 3.Fill Form

        user_name_input = wait.until(EC.presence_of_element_located((By.ID, "txt_username")))
        password_input = driver.find_element(By.ID,'txt_password')
        captcha_input = driver.find_element(By.ID, 'txtCaptcha')

        user_name_input.send_keys('BHIMAMADURAI')
        password_input.send_keys('Eway@1234')

        # 4. Capture Captcha

        captcha_img = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'Captcha')]")))

        #5. Save Captcha ScreenShot

        captcha_img.screenshot("captcha.png")
        print('Catcha image saved as png')

        # 6.Show Captcha to user
        input_image = Image.open('captcha.png')
        st.image(input_image,caption='Captcha',use_container_width=False)
        
        # 7. Entering the Captcha manually

        if 'captcha_value' not in st.session_state:
            st.session_state['captcha_value'] = ''
    
            st.session_state['captcha_value'] = st.text_input('Enter the captcha')
            captcha_input = driver.find_element(By.ID, 'txtCaptcha')
            captcha_input.send_keys(st.session_state['captcha_value'])


        if st.button("Submit Captcha"):
            if st.session_state['captcha_value']:
                st.success(f"Captcha Entered':{st.session_state['captcha_value']}")
                login_button = driver.find_element(By.ID,'btnLogin')
                login_button.click()
                st.success(f"Captcha Entered: {st.session_state['captcha_value']}")
            else:
                st.error('Captcha mismatch')

        # 8.Click Login
        

        if 'otp_value' not in st.session_state:
            st.session_state['otp_value'] = ''

            wait = WebDriverWait(driver, 60)
            otp_input = wait.until(EC.presence_of_element_located((By.ID, "OtpTxt")))
            #otp_input = wait.until(EC.visibility_of_element_located((By.ID, "OtpTxt")))

            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            print(len(iframes))

            st.session_state['otp_value'] = st.text_input('Enter the OTP')

            if st.button("Submit OTP"):

                if st.session_state['otp_value']:                
                    otp_input.send_keys(st.session_state['otp_value'])
                    st.success('OTP entered ')
        



