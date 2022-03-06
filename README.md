ECB Daily Rates History
========

This library provides historical exchange rates from European Central Bank.

## Installation

`pip install git+https://github.com/khorevkp/ECB_rates.git`

## Basic Usage

Function get_ecb_rates accepts two parameters: the currency code and the start_date.
It returns a pandas dataframe with all historical FX rates of the requested currency against EUR for the period since the requested start_date till most recent available date.

```
import ecbfxrates as ecb

ecb.get_ecb_rates("USD", "2022-03-01")
```

### License
MIT licensed. 
