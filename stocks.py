#!/usr/bin/python3

# pip install yfinance lxml
import yfinance as yf

IBEX = yf.Ticker("^IBEX")
REP = yf.Ticker("REP.MC")

print(REP.info)
