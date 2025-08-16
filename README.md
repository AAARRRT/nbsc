[![Python](https://img.shields.io/badge/python-v3-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# nbsc: Python interface to National Bureau of Statistics of China (NBSC) API
Known data codes (series) for API requests...

## Consumer Price Index (CPI)
### Annual CPI
**dbcode="hgnd"**  
A090201 - Consumer Price Index (1978=100)  
A090302 - Consumer Price Index (1978=100)  

### Monthly CPI
**dbcode="hgyd"**  
Last Year = 100  
A01010101 - Consumer Price Index (The same month last year=100) 2016 -  
A01010201 - Consumer Price Index (The same month last year=100) 1987 - 2015  
 
The same period last year=100  
A01020101 - Consumer Price Index (The same period last year=100) 2016 -  
A01020201 - Consumer Price Index (The same period last year=100) 1995 - 2015

preceding month=100  
A01030G01 - Consumer Price Index (preceding month=100) 2021 -  
A01030101 - Consumer Price Index (preceding month=100) 2016 - 2020
A01030201 - Consumer Price Index (preceding month=100) 2001 - 2015

## Gross Domestic Product (GDP) - annual data
**dbcode="hgnd"**  
A020102 - Gross Domestic Product (GDP)  
A020106 - Per Capita GDP  
A020101 - Gross National Income  



