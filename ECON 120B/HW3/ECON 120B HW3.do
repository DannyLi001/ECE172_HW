cd "C:\Users\Danny\Desktop\ECON 120B\HW3"

cap log close
log using "HW3.txt", text replace
use CPS96_15.dta, clear

****Q a.i&ii
sum ahe if year == 1996
*display "Average hourly earnings in 1996 = 12.69326" 
*display "Sample standard deviation for AHE in 1996 = 6.359035" 
sum ahe if year == 2015
*display "Average hourly earnings in 2015 = 21.23744 " 
*display "Sample standard deviation for AHE in 2015 = 12.1245" 
****Q a.iii
ttest ahe, by(year) unequal
*display "95% confidence interval for the population means of AHE in 1996 = [12.53369 12.85283]"
*display "95% confidence interval for the population means of AHE in 2015 = [20.95533 21.51955]"
****Q a.iv
*display "95% confidence interval for the change in the population means of AHE between 1996 and 2015 = [-8.868268 -8.220087]"


****Q b
ge adjusted_ahe = ahe if year == 2015
replace adjusted_ahe = ahe*(237/156.9) if year == 1996
ttest adjusted_ahe, by(year) unequal
*display "Average hourly earnings in 1996 in 2015 dollar = 19.17338" 
*display "Sample standard deviation for AHE in 1996 in 2015 dollar = 9.605425" 
*display "95% confidence interval for the population means of AHE in 1996 in 2015 dollar = [18.93234 19.41441]"
*display "95% confidence interval for the change in the population means of AHE between 1996 and 2015 in 2015 dollar = [-2.435086 -1.693038]"


****Q c
* I would use the results from b and compare with a because the CPI shows the real purchase power of 1996 in 2015 dollar, but without comparison, we cannot tell the change in purchasing power.


****Q d.i
generate ahe_15 = ahe if year == 2015
ttest ahe_15, by(bachelor) 
*display "95% confidence interval for the means of AHE for high school graduates = [16.09262     16.6696]"
****Q d.ii
*display "95% confidence interval for the means of AHE for workers with a college degree = [25.19241    26.03765]"
****Q d.iii
*display "95% confidence interval for the difference between the two means = [-9.756487   -8.711361]"


****Q e
generate ahe_96 = ahe if year == 1996
generate adjusted_ahe_96 = ahe_96*(237/156.9) 
ttest adjusted_ahe_96, by(bachelor) unequal
*display "95% confidence interval for the means of AHE for high school graduates in 2015 dollar = [16.01336     16.5231]"
*display "95% confidence interval for the means of AHE for workers with a college degree in 2015 dollar = [22.63517     23.4409]"
*display "95% confidence interval for the difference between the two means = [-7.246445   -6.293168]"


****Q f.i
* No, the real wages of high school graduates did not increase a lot because the means of AHE for high school graduates in 2015 is similar to the means of AHE for high school graduates in 1996 in 2015 dollar 
****Q f.ii
* Yes, the real wages of college graduates increase because the means of AHE for college graduates in 2015 is larger than the means of AHE for college graduates in 1996 in 2015 dollar
****Q f.iii
* Yes, the gap between earnings of college and high school graduates increase because the difference in means of AHE in 2015 is larger than the difference in means of AHE in 1996 in 2015 dollar


****Q g
table ( year female ) ( bachelor ) (), nototals statistic(mean  ahe) statistic(sd  ahe) statistic(frequency)
* Yes, there are notable differences between the results for high school and college graduates


cap log close
