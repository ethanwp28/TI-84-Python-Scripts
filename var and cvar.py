from math import exp, sqrt, pi, log

def get_input(prompt, type_func=float):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to approximate the inverse CDF of the standard normal distribution
def inverse_normal_cdf(p):
    if p < 0.5:
        # F^-1(p) = - G^-1(p)
        return -inverse_normal_cdf_helper(1-p)
    else:
        # Use the approximation
        return inverse_normal_cdf_helper(p)

def inverse_normal_cdf_helper(p):
    # constants
    a1 =  -3.969683028665376e+01
    a2 =   2.209460984245205e+02
    a3 =  -2.759285104469687e+02
    a4 =   1.383577518672690e+02
    a5 =  -3.066479806614716e+01
    a6 =   2.506628277459239e+00

    b1 =  -5.447609879822406e+01
    b2 =   1.615858368580409e+02
    b3 =  -1.556989798598866e+02
    b4 =   6.680131188771972e+01
    b5 =  -1.328068155288572e+01

    c1 =  -7.784894002430293e-03
    c2 =  -3.223964580411365e-01
    c3 =  -2.400758277161838e+00
    c4 =  -2.549732539343734e+00
    c5 =   4.374664141464968e+00
    c6 =   2.938163982698783e+00

    d1 =   7.784695709041462e-03
    d2 =   3.224671290700398e-01
    d3 =   2.445134137142996e+00
    d4 =   3.754408661907416e+00

    # Define break-points.
    p_low =  0.02425
    p_high = 1 - p_low

    # Rational approximation for lower region
    if 0 < p < p_low:
        q = sqrt(-2*log(p))
        return (((((c1*q+c2)*q+c3)*q+c4)*q+c5)*q+c6) / ((((d1*q+d2)*q+d3)*q+d4)*q+1)

    # Rational approximation for upper region
    if p_high < p < 1:
        q = sqrt(-2*log(1-p))
        return -(((((c1*q+c2)*q+c3)*q+c4)*q+c5)*q+c6) / ((((d1*q+d2)*q+d3)*q+d4)*q+1)

    # Rational approximation for central region
    if p_low <= p <= p_high:
        q = p - 0.5
        r = q*q
        return (((((a1*r+a2)*r+a3)*r+a4)*r+a5)*r+a6)*q / (((((b1*r+b2)*r+b3)*r+b4)*r+b5)*r+1)

    # If p is not in (0,1), return an error message
    return "Invalid input. 'p' must be between 0 and 1."

# Get user inputs for the parameters
fund_value = get_input("Enter the fund value: ")
mean = get_input("Enter the mean: ")
std_dev = get_input("Enter the standard deviation: ")

# Calculate z-scores for the 1st and 5th percentiles
z_score_1_percent = inverse_normal_cdf(0.01)
z_score_5_percent = inverse_normal_cdf(0.05)

# Calculate VaR and ES
VaR_1_percent = fund_value - (mean + z_score_1_percent * std_dev)
VaR_5_percent = fund_value - (mean + z_score_5_percent * std_dev)

# For ES, we need the pdf of the normal distribution
def normal_pdf(x):
    return (1 / (sqrt(2 * pi))) * exp(-x**2 / 2)

ES_1_percent = fund_value - (mean + (normal_pdf(z_score_1_percent) / 0.01) * std_dev)
ES_5_percent = fund_value - (mean + (normal_pdf(z_score_5_percent) / 0.05) * std_dev)

# Print results
print("Value at Risk (VaR) at 1%:", VaR_1_percent)
print("Value at Risk (VaR) at 5%:", VaR_5_percent)
print("Expected Shortfall (ES) at 1%:", ES_1_percent)
print("Expected Shortfall (ES) at 5%:", ES_5_percent)
