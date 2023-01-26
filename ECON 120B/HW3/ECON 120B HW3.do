cd "C:\Users\Danny\Desktop\ECON 120B\HW3"

cap log close
log using "HW3.txt", text replace

use CPS96_15.dta, clear
****Q a.i&ii
sum ahe if year == 1996
display "Average hourly earnings in 1996 = " `r(mean)'
display "Sample standard deviation for AHE in 1996 = " `r(sd)'
sum ahe if year == 2015
display "Average hourly earnings in 2015 = " `r(mean)'
display "Sample standard deviation for AHE in 2015 = " `r(sd)'
****Q a.iii
ttest ahe, by(year) 
****Q a.iv

generate adjusted_ahe = ahe if year == 2015

replace adjusted_ahe = ahe*(237/156.9) if year == 1996

ttest adjusted_ahe, by(year) unequal

ttest adjusted_ahe, by(bachelor) unequal

cap log close