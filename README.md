Platinum Python Library (v.1.0.) 2025, 14Alfa. All rights reserved.

Platinum is a fast, pure statistical library, with new math functions implemented. Its objective is to implement statistics into the Python world using Python-familiar objects.

Platinum introduces 15 new functions, with fast outputs and correct, precise results. This document serves as a go-to manual for how to correctly use Platinum.

1. Initialize the Platinum library
2. New Exceptions found in Platinum
3. New Functions implemented in Platinum
	3.1. Statistical Inference Functions
	3.2. Math Functions
4. Quartile/Z-Test/P-Test selector variables


1. Initialize the Platinum library

For the Platinum library to work, it needs:
	- The Python library "math"
	- The following line of code: import platinum as pt
It is important that the platinum.py archive is in the SAME folder that you are working on. If this is not the case, then the library will not work.

2. New Exceptions found in Platinum

Platinum implements 2 new exceptions for dealing with the new functions:

 - ListError: Platinum focuses its use on Python lists, and it requieres a minimum number of elements in the lists for the functions to work properly. If these conditions are not satisfied, then Platinum outputs the ListError exception, with its convenient description.

 - TypeOverflow: This exception is generated when a bounded variable exceeds some limits or does not satisfy some requierements (for example, inputting a real number as an integer variable)

3. New Functions implemented in Platinum

Platinum implements a bunch of statistical functions not found in Python. The following text serves as a description of all of Platinum's functions:

 1. Mean function.	pt.mean(list) 		-> It outputs the mean of a given list.
 2. Median function. 	pt.median(list)		-> It outputs the median of a given list.
 3. Quartile function.	pt.quartile(list,type)	-> It outputs the type quartile (1st, 2nd or 3rd quartile) of a given list. Method used is described as "Method 1" on Wikipedia.
 4. Summary function.	pt.summary(list)	-> It outputs the Five-Number Summary of a given list as a new list.
 5. Variance function.	pt.var(list)		-> It outputs the variance of a given list.
 6. St. Deviation function.	pt.sd(list)	-> It outputs the standard deviation of a given list as the square root of the variance.
 7. Lin. Correlation function.	pt.cor(x,y)	-> It outputs the Linear Correlation Coefficient of an x-variable list and a y-variable list.
 8. Lin. Regression function.	pt.linear_reg(x,y) -> It outputs the coefficients a, b for the linear regression y=a+bx, given 2 lists of data: an x-variable list and a y-variable list. It also outputs a visual summary.
 9. Normal CDF.		pt.pnorm(x,mu,sigma)	-> It outputs the probability of a random variable X being less than or equal to x. X follows a normal distribution with mean mu and with standard deviation sigma.
 10. Standardized CDF.	pt.p_standard(x)	-> It outputs the probability of a random variable X being less than or equal to x. X follows the standardized normal distribution (mean=0, sigma=1).
These statements are equivalent: pnorm(x,0,1) == p_standard(x)
 11. Binomial CDF.	pt.pbinom(k,n,p)	-> It outputs the probability of a random variable B having k sucesses, with n tries and a probability of sucess p. The variable B follows the binomial distribution B(n,p)
 12. Exponential CDF.	pt.pexp(l,a,b)		-> It outputs the probability of a random variable E being inside the interval [a,b]. The variable E follows an exponential distribution of the form: f(x)=l*e^(-l*t), for all t greater than 0.

	3.1: Statistical Inference Functions

 13. Z-Test.		pt.zest(list,mu,sigma,c,ha)	->  It performs a Z-Test of Statistical Inference given a list of data, its mean mu, its standard deviation sigma, the confidence level C and the means of the alternate hypothesis. Only values of c of 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.96, 0.98, 0.99, 0.995, 0.998 and 0.999 are valid, as the Z Score table only has these values.
 14. P-Test		pt.ptest(ext,n,p,c,ha)	-> It performs a Z-Test of Statistical Inference of a success proportion, given the number of successes ext, the number of tries n, its mean p, the confidence level C and the means of the alternate hypothesis.

	3.2: Math Functions

 15. Primality Function	pt.primality(test_number)	-> It outputs whether a number is prime or composite, and its factors.



4. Quartile/Z-Test/P-Test selector variables

On the quartile, z-test and p-test functions (no. 3, 13 and 14), there exists the variables "type" and "ha". These are selector variables, which mean that they have a small range of values the function can work with. The values allowed are the following:

	* "type" variable on pt.quartile(): It can only take the values 1 (first quartile), 2 (second quartile/median) and 3 (third quartile).
	* "ha" variable on pt.ztest() and pt.ptest(): It can only take the values 1 (right alternate hypothesis), 2 (left alternate hypothesis) and 3 (two-sided alternate hypothesis).
