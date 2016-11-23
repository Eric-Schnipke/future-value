###Future Total Investment Prediction ### Project 1 

def returnfv(principal,no_of_year,current_income,per_contri,annual_increase,interest,compound):
  ###### INPUT ########
  #principal:       investment value
  #no_of_year:      number of year to invest from now
  #current_income:  self-explantory, annual salary
  #per_contri:      how many percent from current income for investing? (decimal)
  #annual_increase: how many percent increase in income annually (decimal)
  #interest:        annual percentage rate, for investment return. (decimal)
  #compound:        'daily', 'monthly', 'annually' 
  
  #### FORMULA ####
  ## FV = princial*(1+r/k)^(n*k) + monthly_payment*((1+r/k)^(n*k)-1)*(1+r/k)/(r/k)
  
  if compound == 'daily':
    n = 365
  elif compound == 'monthly':
    n = 12
  else:
    n = 1
  
  pmt = current_income*per_contri/12
  i = 0
  while i < no_of_year:
    principal = (principal*(1+interest/n)**n) + (pmt*((1+interest/n)**n - 1)*(1+interest/n)/(interest/n))
    pmt = pmt*(1+annual_increase)
    i = i + 1
  return principal

###Change code below with your input values in the order of
## principal,no_of_year,current_income,per_contri,annual_increase,interest,compound
print (returnfv(10000,10,70000,.4,.03,.07,'monthly'))
