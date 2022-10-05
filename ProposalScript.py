from re import template
from docx import Document
import streamlit as st
import os

st.image('zizzl health logo 22.png')

st.title("Proposal Tool")

def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)

Client = st.text_input('Client')    

Carrier = st.text_input('Carrier')

Date = st.text_input('Date')

Broker = st.text_input('Broker')

Agent = st.text_input('Agent')

Deductible = st.text_input('Deductible')

Out_of_Pocket = st.text_input('MAX Out of Pocket')

Example = st.text_input('Example Premium for a non-smoking 30- year old in the baseline county')

Website = st.text_input('Website')

Email = st.text_input('Email')

Phone = st.text_input('Phone')

template_file_path = 'Proposal.docx'
output_file_path = 'Downloads/result.docx'

guardian = st.radio('Guardian', ['Yes', 'No'])

if st.button('SUBMIT'):
    if(guardian == 'Yes'):
        variables = {
            "CLIENT NAME": Client,
            "CARRIER NAME": Carrier,
            "INSERT DATE HERE": Date, 
            "BROKER NAME": Broker,
            "AGENT NAME": Agent,
            "WEBSITE": Website,
            "EMAIL": Email,
            "PHONE": Phone,
            "DEDUCTIBLE": Deductible,
            "OOP": Out_of_Pocket,
            "EXAMPLE": Example,
            "GUARDIAN": 'Guardian Life Insurance Company product administration, including APIs connecting the systems with ease'
        }
    else:
        variables = {
            "CLIENT NAME": Client,
            "CARRIER NAME": Carrier,
            "INSERT DATE HERE": Date, 
            "BROKER NAME": Broker,
            "AGENT NAME": Agent,
            "WEBSITE": Website,
            "EMAIL": Email,
            "PHONE": Phone,
            "DEDUCTIBLE": Deductible,
            "OOP": Out_of_Pocket,
            "EXAMPLE": Example,
            "GUARDIAN": ''


        }

    template_document = Document(template_file_path)

    for variable_key, variable_value in variables.items():
        for paragraph in template_document.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

        for table in template_document.tables:
            for col in table.columns:
                for cell in col.cells:
                    for paragraph in cell.paragraphs:
                        replace_text_in_paragraph(paragraph, variable_key, variable_value)

    template_document.save('Filled_Proposal.docx')










