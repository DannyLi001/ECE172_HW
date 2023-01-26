clear all 

cd "C:\Users\Danny\Desktop\ECON 120B\HW1"

cap log close
log using output/HW2, text replace

use data/baseballsalaries.dta

describe
summarize

****Q1
summarize payroll

display "Average payroll (in thousands) = " `r(mean)'

****Q2
generate total_games = wins + losses
generate win_percentage = (wins/total_games)*100

label var total_games "Total games won by a team"
label var win_percentage "Average percentage of games won"

sum win_percentage
di "Percentage of games won by a team = " `r(mean)'

****Q3
twoway scatter win_percentage payroll, title("Winning percentage vs payroll")
graph export "output/graph.png",replace

****Q4
ttest payroll, by(playoffs)

