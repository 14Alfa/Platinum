# Platinum Library. Fast, pure statistical library, with math functions.
# Libraries needed to run Platinum: math
import math
# New Exceptions implemented in Platinum:
class ListError(Exception):
    pass
class TypeOverflow(Exception):
    pass

# 1. Mean function. It outputs the mean of a given list (Credits to Ismael).
def mean(lista):
    l=len(lista)
    if l!=0:
        s=sum(lista)
        return s/l
    else:
        raise ListError("The list must contain 1 or more elements")

# 2. Median Function. It outputs the median of a given list.
def median(lista):
    l=len(lista)
    if l!=0:
        l_order=sorted(lista)
        if l%2==0:
            el_1=l_order[(l//2)-1]; el_2=l_order[l//2]
            return (el_1+el_2)/2
        else:
            return l_order[l//2]
    else:
        raise ListError("The list must contain 1 or more elements")
    
# 3. Quartile function. It outputs the type quartile (1st, 2nd or 3rd quartile) of a given list. Method used is described as "Method 1".
def quartile(lista,type):
    l=len(lista)
    if l!=0:
        l_order=sorted(lista)
        match type:
            case 1:
                if l%2==0:
                    for i in range(l//2):
                        l_order.pop()
                    return median(l_order)
                else:
                    for i in range((l//2)+1):
                        l_order.pop()
                    return median(l_order)
            case 2:
                return median(l_order)
            case 3:
                if l%2==0:
                    for i in range(l//2):
                        l_order.remove(l_order[0])
                    return median(l_order)
                else:
                    for i in range((l//2)+1):
                        l_order.remove(l_order[0])
                    return median(l_order)
            case _:
                raise TypeOverflow("Couldn't generate quartile. Type must be 1, 2 or 3")
    else:
        raise ListError("The list must contain 1 or more elements")

# 4. Summary function. It outputs the Five-Number Summary of a given list.
def summary(lista):
    if len(lista)!=0:
        summary_list=[min(lista),quartile(lista,1),median(lista),quartile(lista,3),max(lista)]
        print("Five-Number Summary")
        print("Min:",min(lista)," Q1:",quartile(lista,1)," Q2/M:",median(lista)," Q3:",quartile(lista,3)," Max:",max(lista))
        return summary_list
    else:
        ListError("The list must contain 1 or more elements")

# 5. Variance function. It outputs the Variance of a given list.
def var(lista):
    l=len(lista); m=mean(lista); numerator=0
    if l>1:
        for i in range(l):
            numerator+=(int(lista[i]-m)**2)
        return numerator/(l-1)
    else:
        raise ListError("The list must contain 2 or more elements")

# 6. Standard Deviation function. It outputs the Standard Deviation of a given list (the square root of the variance)
def sd(lista):
    return var(lista)**0.5

# 7. Linear Correlation function. It outputs the Linear Correlation Coeficient of an x-variable list and a y-variable list
def cor(x,y):
    if len(x)==len(y):
        n=len(x)
        xy_sum=sum(x[i]*y[i] for i in range(n))
        x2_sum=sum(x[i]**2 for i in range(n))
        y2_sum=sum(y[i]**2 for i in range(n))

        num=n*xy_sum-(sum(x)*sum(y))
        den=((n*x2_sum-sum(x)**2)*(n*y2_sum-sum(y)**2))**0.5
        return num/den
    else:
        raise ListError("The lists must be of equal length")
    
# 8. Linear Regression function. It outputs the coefficients a, b for the linear regression y=a+bx, given 2 lists of data: an x-variable list and a y-variable list
def linear_reg(x,y):
    l=len(x)
    xy_sum=sum(x[i]*y[i] for i in range(l))
    x2_sum=sum(x[i]**2 for i in range(l))
    b=((l*xy_sum)-(sum(x)*sum(y)))/(l*x2_sum-(sum(x)**2))
    a=mean(y)-b*mean(x)
    print("Linear Regression for 2 variable input")
    print("Linear equation: y =",a,"+",b,"* x")
    print("Slope:",b,"    Y-intercept:",a)
    print("% of observations explained:",(cor(x,y)**2)*100, "%")
    return a,b

# 9. Cumulative Normal Distribution function. It outputs the probability of a random variable X being less than or equal to x. X follows a normal distribution
# with mean mu and with standard deviation sigma.
def pnorm(x,mu,sigma):
    if sigma>0:
        sqrt2=2**0.5
        error_input=(x-mu)/(sigma*sqrt2)
        probability=0.5*(1+math.erf(error_input))
        return probability
    else:
        raise TypeOverflow("Sigma must be greater than 0")

# 10. Standardized CDF. It outputs the probability of a random variable X being less than or equal to x. X follows the standardized normal distribution
# (mean=0, sigma=1). These statements are equivalent: pnorm(x,0,1) == p_standard(x)
def p_standard(x):
    sqrt2=2**0.5
    probability=0.5*(1+math.erf(x/sqrt2))
    return probability

# 11. Binomial Distribution function. It outputs the probability of a random variable B having k sucesses, with n tries and a probability of sucess p. The
# variable B follows a binomial distribution --> B(n,p)
def pbinom(k,n,p):
    if n%1==0 & k%1==0 & int(p>=0) & int(p<=1):
        if n>0 & k<n:
            q=1-p
            probability=(math.comb(n,k))*(p**k)*(q**(n-k))
            return probability
        else:
            raise TypeOverflow("The inputs k and n must be both integers. The input p must be strictly between 0 and 1")
    else:
        raise TypeOverflow("The inputs k and n must be both integers. The input p must be strictly between 0 and 1")
    
# 12. Exponential Distribution function. It outputs the probability of a random variable E being inside the interval [a,b]. The variable E follows an
# exponential distribution of the form: f(x)=l*e^(-l*t), for all t greater than 0.
def pexp(l,a,b):
    if l!=0:
        if a>0:
            if a<b:
                a_value=math.exp(-(l*a)); b_value=math.exp(-(l*b))
                probability=a_value-b_value
                return probability
            else:
                raise TypeOverflow("The a and b parameters must satisfy 0<a<b")
        else:
            raise TypeOverflow("The a and b parameters must satisfy 0<a<b")
    else:
        raise TypeOverflow("The l parameter must not be 0")

# 13. Z-Test for Statistical Inference. It performs a Z-Test of Statistical Inference given a list of data, its mean mu, its standard deviation sigma,
# the confidence level C and the means of the alternate hypothesis.
# Only values of c of 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.96, 0.98, 0.99, 0.995, 0.998 and 0.999 are valid, as the Z Score table only has these values.
def ztest(lista,mu,sigma,c,ha):
    n=len(lista)
    if n>=1:
        if int(c>0) & int(c<1):
            # Confidence Interval:
            z_star_dic={
                0.5:0.674, 0.6:0.841, 0.7:1.036, 0.8:1.282, 0.9:1.645, 0.95:1.96, 0.96:2.054,
                0.98:2.326, 0.99:2.576, 0.995:2.807, 0.998:3.091, 0.999:3.291
            }
            if c in z_star_dic.keys():
                z_star=z_star_dic[c]
            else:
                raise TypeOverflow("The Confidence Level input is not registered in the Table")
            err=z_star*sigma/(n**0.5)
            print("Z-Test for Statistical Inference.")
            print("Confidence Interval: mu is between",mean(lista)-err,"and",mean(lista)+err)
            print("z-star:", z_star, "   Confidence Level:",c)
            print("")
            # Significance Testing:
            z_contrast=(mean(lista)-mu)/(sigma/(n**0.5)); alpha=round(1-c,4)
            print("Significance Testing: Null Hypothesis: mu is equal to", mu)
            match ha:
                case 1:
                    p_value=1-p_standard(z_contrast)
                    print("Alternate Hypothesis: mu is greater than", mu)
                case 2:
                    p_value=p_standard(z_contrast)
                    print("Alternate Hypothesis: mu is less than", mu)
                case 3:
                    if z_contrast>=0:
                        p_value=2*(1-p_standard(z_contrast))
                    else:
                        p_value=2*(1-p_standard(-(z_contrast)))
                    print("Alternate Hypothesis: mu is not equal to", mu)
                case _:
                    raise TypeOverflow("The ha variable needs to be 1, 2 or 3 for the alternate hypothesis to be left, right or two-sided")
            print("")
            if p_value<=alpha:
                print("Alternate Hypothesis is accepted, enough evidence")
            else:
                print("Alternate Hypothesis is rejected, not enough evidence")
            print("Z-contrast:",z_contrast,"   P-value:",p_value, "   Significance Level:",alpha)
        else:
            raise TypeOverflow("The Confidence Level must be strictly between 0 and 1")
    else:
        raise ListError("The list must contain 1 or more elements")

# 14. P-Test for Proportion Inference. It performs a Z-Test of Statistical Inference of a success proportion, given the number of successes ext, the number of tries n,
# its mean p, the confidence level C and the means of the alternate hypothesis.
def ptest(ext,n,p,c,ha):
    p_arg=ext/n; sigma=((p*(1-p))/n)**0.5
    if int(p_arg<=1) & int(n>0):
        if int(c>0) & int(c<1):
            # Confidence Interval:
            z_star_dic={
                0.5:0.674, 0.6:0.841, 0.7:1.036, 0.8:1.282, 0.9:1.645, 0.95:1.96, 0.96:2.054,
                0.98:2.326, 0.99:2.576, 0.995:2.807, 0.998:3.091, 0.999:3.291
            }
            if c in z_star_dic.keys():
                z_star=z_star_dic[c]
            else:
                raise TypeOverflow("The Confidence Level input is not registered in the Table")
            err=z_star*(((p_arg*(1-p_arg))/n)**0.5)
            print("P-Test for Proportion Inference.")
            print("Confidence Interval: p is between",p_arg-err,"and",p_arg+err)
            if p_arg<=err:
                if p_arg>=1-err:
                    print("Real interval: p is between 0 and 1")
                else:
                    print("Real interval: p is between 0 and",p_arg+err)
            else:
                if p_arg>=1-err:
                    print("Real interval: p is between",p_arg-err,"and 1")
            print("z-star:", z_star, "   Confidence Level:",c)
            print("")
            # Significance Testing:
            z_contrast=(p_arg-p)/sigma; alpha=round(1-c,4)
            print("Significance Testing: Null Hypothesis: p is equal to", p)
            match ha:
                case 1:
                    p_value=1-p_standard(z_contrast)
                    print("Alternate Hypothesis: p is greater than", p)
                case 2:
                    p_value=p_standard(z_contrast)
                    print("Alternate Hypothesis: p is less than", p)
                case 3:
                    if z_contrast>=0:
                        p_value=2*(1-p_standard(z_contrast))
                    else:
                        p_value=2*(1-p_standard(-(z_contrast)))
                    print("Alternate Hypothesis: p is not equal to", p)
                case _:
                    raise TypeOverflow("The ha variable needs to be 1, 2 or 3 for the alternate hypothesis to be left, right or two-sided")
            print("")
            if p_value<=alpha:
                print("Alternate Hypothesis is accepted, enough evidence")
            else:
                print("Alternate Hypothesis is rejected, not enough evidence")
            print("Z-contrast:",z_contrast,"   P-value:",p_value, "   Significance Level:",alpha)
        else:
            raise TypeOverflow("The Confidence Level must be strictly between 0 and 1")    
    else:
        raise TypeOverflow("The number of tries must be greater than 0. The success proportion must be strictly between 0 and 1")
    
# 15. Primality Test function. It outputs whether a number is prime or composite, and its factors.
def primality(test_number):
    if test_number==math.trunc(test_number):
        z=0; factors=[]
        for i in range(test_number):
            remainder=test_number%(i+1)
            if remainder==0:
                z+=1
                factors.append(i+1)
        if z==2:
            print("The number is prime")
        elif z>2:
            print("The number is composite (not prime)")
        else:
            print("The number is 1 (not prime nor composite)")
        print("Factors: ",factors)
        return factors
    else:
        raise TypeOverflow("The number input must be an integer greater than 0")
    
    