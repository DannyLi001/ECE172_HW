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
ttest ahe, by(year) unequal
display "95% confidence interval for the population means of AHE in 1996 = [12.53369 12.85283]"
display "95% confidence interval for the population means of AHE in 2015 = [20.95533 21.51955]"
****Q a.iv
display "95% confidence interval for the change in the population means of AHE between 1996 and 2015 = [-8.868268 -8.220087]"


****Q b
generate adjusted_ahe = ahe if year == 2015
replace adjusted_ahe = ahe*(237/156.9) if year == 1996
ttest adjusted_ahe, by(year) unequal
display "Average hourly earnings in 1996 in 2015 dollar = 19.17338" 
display "Sample standard deviation for AHE in 1996 in 2015 dollar = 9.605425" 
display "95% confidence interval for the population means of AHE in 1996 in 2015 dollar = [18.93234 19.41441]"
display "95% confidence interval for the change in the population means of AHE between 1996 and 2015 in 2015 dollar = [-2.435086 -1.693038]"


****Q c


****Q d
ttest ahe, by(bachelor) unequal
display "95% confidence interval for the means of AHE for high school graduates = [13.34831 13.70529]"
display "95% confidence interval for the means of AHE for workers with a college degree = [21.04299 21.64129]"
display "95% confidence interval for the difference between the two means = [-8.163674 -7.467013]"
****Q e
ttest adjusted_ahe, by(bachelor) unequal
display "95% confidence interval for the means of AHE for high school graduates in 2015 dollar = [13.34831 13.70529]"
display "95% confidence interval for the means of AHE for workers with a college degree = [21.04299 21.64129]"
display "95% confidence interval for the difference between the two means = [-8.163674 -7.467013]"


cap log close