import streamlit as st
import yfinance as yf
import pandas as pd


st.write('''
         # Aula 01
         Simples visualizador de preços de ações
         
         ''')

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-1', end='2020-5-31')

st.line_chart(tickerDf.Close)
