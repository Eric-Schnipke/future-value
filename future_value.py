###Future Total Investment Prediction ### Project 1 
from math import isclose

################################################################################
# Declare global, constant data.
################################################################################
num_periods = { 'daily'   : 365 ,
                'monthly' : 12  ,
                'yearly'  : 1   }


################################################################################
# Function:   get_future_value()
# Decription: Gets the future value of a principal investment and subsequent
#             cashflows given number of years for capitalization, salary
#             annual contribution from salary, annual contribution increase,
#             expected annualized market returns, and number of compounding
#             periods in one year.
################################################################################
def get_future_value( principal       ,  # investment value
                      no_of_year      ,  # number of year to invest from now
                      current_income  ,  # self-explantory, annual salary
                      per_contri      ,  # how many percent from current income for investing? (decimal)
                      annual_increase ,  # how many percent increase in income annually (decimal)
                      interest        ,  # annual percentage rate, for investment return. (decimal)
                      compound        ): # 'daily', 'monthly', 'annually'
      
    # Future value formula.
    # FV = princial*(1+r/k)^(n*k) + monthly_payment*((1+r/k)^(n*k)-1)*(1+r/k)/(r/k)

    n = num_periods[compound]
  
    pmt = current_income*per_contri/12
    i = 0
    while i < no_of_year:
        principal = (principal*(1+interest/n)**n) + (pmt*((1+interest/n)**n - 1)*(1+interest/n)/(interest/n))
        pmt      *= 1 + annual_increase
        i        += 1
    return principal


################################################################################
# Function:   run_unit_tests()
# Decription: Runs unit tests with select, known-good values (see: "true_fv")
#             to test whether get_future_value() functionality has been altered
#             during development.  Pass "True" as argument to run tests.
################################################################################
def run_unit_tests( run_tests = False ):
    if run_tests is False:
        return
    
    ################
    # Unit Test 1: #
    ###########################################################################
    true_fv = 477958.10884661495
    test_fv = get_future_value( principal       = 10000     ,
                                no_of_year      = 10        ,
                                current_income  = 70000     ,
                                per_contri      = 0.40      ,
                                annual_increase = 0.03      ,
                                interest        = 0.07      ,
                                compound        = 'monthly' )
    assert isclose(true_fv, test_fv, abs_tol=1e-8)
    
    ################
    # Unit Test 2: #
    ###########################################################################
    true_fv = 13922251.112204345
    test_fv = get_future_value( principal       = 10000   ,
                                no_of_year      = 10      ,
                                current_income  = 70000   ,
                                per_contri      = 0.40    ,
                                annual_increase = 0.03    ,
                                interest        = 0.07    ,
                                compound        = 'daily' )
    assert isclose(true_fv, test_fv, abs_tol=1e-8)
    
    ################
    # Unit Test 3: #
    ###########################################################################
    true_fv = 58571.76344632381
    test_fv = get_future_value( principal       = 10000    ,
                                no_of_year      = 10       ,
                                current_income  = 70000    ,
                                per_contri      = 0.40     ,
                                annual_increase = 0.03     ,
                                interest        = 0.07     ,
                                compound        = 'yearly' )
    assert isclose(true_fv, test_fv, abs_tol=1e-8)
    
    #############################
    # Add more unit tests here! #
    ###########################################################################
    # ... #


################################################################################
# Function:   main()
# Decription: Begin execution here.
################################################################################
def main():
    # Change parameters below with your input values.
    print( get_future_value( principal       = 10000     ,
                             no_of_year      = 10        ,
                             current_income  = 70000     ,
                             per_contri      = 0.40      ,
                             annual_increase = 0.03      ,
                             interest        = 0.07      ,
                             compound        = 'monthly' ))
    
    # Run unit tests, if desired.
    run_unit_tests(True)


# call main() to begin execution
main()
