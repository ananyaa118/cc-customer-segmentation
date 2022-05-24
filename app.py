import streamlit as st
import pickle


model = pickle.load(open('model.pkl','rb'))

st.title('Credit Card Customer Segmentation')

col1, col2 = st.columns(2)

with col1:
    balance = st.number_input('Balance (in $)')
    balance_frequency = st.number_input('Balance Frequency (b/w 0 & 1)')
    purchases = st.number_input('Purchases (in $)')
    installment_purchases = st.number_input('Installment Purchases   (in $)')
    cash_advance = st.number_input('Cash Advance (in $)')
    purchases_frequency = st.number_input('Purchases Frequency (b/w 0 & 1)')
    oneoff_purchases_frequency = st.number_input('Oneoff Purchases Frequency (b/w 0 & 1)')

with col2:
    cash_advance_trx = st.number_input('Cash Advance Transaction (in $)')
    purchases_trx = st.number_input('Purchases Transaction  (in $)')
    credit_limit = st.number_input('Credit Limit (in $)')
    payments = st.number_input('Payments (in $)')
    minimum_payments = st.number_input('Minimum Payments (in $)')
    full_payments = st.number_input('Full Payments (in %)')
    tenure = st.number_input('Tenure')


L = [balance, balance_frequency, purchases, installment_purchases, cash_advance, purchases_frequency,
      oneoff_purchases_frequency, cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments,
      full_payments, tenure]

result = model.predict([L])
st.write('')
if st.button('Predict'):
    st.write('')
    if result == 0:
        st.write('Group-1: Poor & Inert')
        st.write("This type of customers have less balance and less purchases. They only buy the necessities and don't take cash advance and installments to do so.")

    if result == 1:
        st.write('Group-2: Cream Customers')
        st.write("This type of customers do a lot of purchases. Take minimal cash advance to do purchases. They even have a good balance and can afford their buy.")

    if result == 2:
        st.write('Group-3: Rich but Purchase less')
        st.write("This type of customers are rich people with a good amount of balance but not frequent buyers. Even with a lot of balance they still take a lot of cash advance to purchase suggesting that they buy expensive items.")

