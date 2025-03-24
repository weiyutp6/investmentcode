# investmentcode
todo add code for options scoring and IV based strategies

# Quant Strategies and Research

This repository contains a collection of quantitative trading strategies, derivatives research, and modeling tools developed during my PhD and personal investing journey. Projects range from options strategy automation to implied volatility-driven ETF construction.

## 📈 Projects Overview

### Options Wheel Strategy
A live paper-trading strategy that sells puts and covered calls on high-IV stocks. Built in Python with modular logic for earnings filters and IV percentile triggers.

### IV-Triggered ETF Model
Explores the construction of a rules-based ETF portfolio by filtering S&P 500 constituents based on the following implied volatility bands:
 - IV<=20
 - 40>=IV>20
 - 60>=IV

### Utilities
Fetch market data for stocks, options, futures, currencies, bonds
Options IV and Greeks calculations, and charting.
Stock strategies and backtesting.

## Topics Covered
- Options pricing (Black-Scholes, Greeks, IV)
- Volatility modeling
- Systematic trading logic
- ETF portfolio simulation

## Getting Started
```bash
git clone https://github.com/yourusername/quant-strategies-and-research.git
```
Install prerequisites
```bash
pip install requests
pip install pandas
pip install yaml
pip install alpaca_trade_api
```
