#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 01:30:22 2023

@author: shishiranjanthakur
"""
#In this code sample, we just tried to interpret inferential statistics by taking just one sample.
# In this case, the sample we have taken from whole dataset is subject 2 and then from subject 2, 
# We further calculate z scores, margin of error, confidence interval etc from some of the voice faetures extracted
# from each voice sample.
import scipy.stats as st
import math

# Method 1: Step-by-step calculation
# sample mean of jitter(1st feature extracted from voice sample)
x_bar1 = 2.6880

#sample mean of shimmer(2nd feature extracted from voice sample)
x_bar2 = 12.37

#sample mean of harmonicity(3rd feature extracted from voice sample)
x_bar3  = 0.8667

#sample mean of pitch(4th feature extracted from voice sample)
x_bar4 = 125.4751

#sample mean of pulse(5th feature extracted from voice sample)
x_bar5 = 0.0080

#standard deviation of jitter
s1= 1.13894

#standard deviation of shimmer
s2= 3.07892

#standard deviation of harmonicity
s3= 0.05898

#standard deviation of pitch
s4= 5.70886

#standard deviation of pulse
s5= 0.00037

#sample size of 1st feature, 2nd feature,third feature, fourth feature and fifth feature of voice samples
n1 = 26
n2= 26
n3 = 26
n4 = 26
n5 = 26
print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar1, s1, n1))

print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar2, s2, n2))

print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar3, s3, n3))

print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar4, s4, n4))

print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar5, s5, n5))

# z-score (assuming 95% Confidence Level)
z_score1 = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score1)

#z-score of 2nd sample mean(assuming 95% Confidence Level)
z_score2 = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score2)

#z-score of 3rd sample mean(assuming 95% Confidence Level)
z_score3 = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score3)

#z-score of 4th sample  mean(assuming 95% Confidence level)
z_score4 = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score4)

#z-score of 5th sample  mean(assuming 95% Confidence level)
z_score5 = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score5)


# compute standard error of jitter
std_err1 = s1 / math.sqrt(n1)
print("Standard error: %.2f" % std_err1)

#compute standard error of shimmer
std_err2 = s2 / math.sqrt(n2)
print("Standard error: %.2f" % std_err2)

#compute standard error of harmonicity
std_err3 = s3 / math.sqrt(n3)
print("Standard error: %.2f" % std_err3)

#compute standard error of pitch
std_err4 = s4 / math.sqrt(n4)
print("Standard error: %.2f" % std_err4)

#compute standard error of pitch
std_err5 = s5 / math.sqrt(n5)
print("Standard error: %.2f" % std_err5)




# compute the margin of error for jitter
mrg_err1 = z_score1 * std_err1
print("Margin of error: %.2f" % mrg_err1)

#compute the margin of error for shimmer
mrg_err2 = z_score2 * std_err2
print("Margin of error: %.2f" % mrg_err2)

#compute the margin of error for harmonicity
mrg_err3 = z_score3 * std_err3
print("Margin of error: %.2f" % mrg_err3)

#compute the margin of error for pitch
mrg_err4 = z_score4 * std_err4
print("Margin of error: %.2f" % mrg_err4)

#compute the margin of error for pulse
mrg_err5 = z_score5 * std_err5
print("Margin of error: %.2f" % mrg_err5)





# get the lower and upper bound of confidence interval for jitter
ci_low1 = x_bar1 - mrg_err1
ci_upp1 = x_bar1 + mrg_err1
print("Confidence Interval of the mean of jitter: %.2f to %.2f" % (ci_low1, ci_upp1))

#get the lower and upper confidence intervals for shimmer
ci_low2 = x_bar2 - mrg_err2
ci_upp2 = x_bar2 + mrg_err2
print("Confidence Interval of the mean of shimmer: %.2f to %.2f" % (ci_low2, ci_upp2))

#get the lower and upper confidence intervals for harmonicity
ci_low3 = x_bar3 - mrg_err3
ci_upp3 = x_bar3 + mrg_err3
print("Confidence Interval of the mean of harmonicity: %.2f to %.2f" % (ci_low3, ci_upp3))

#get the lower and upper confidence intervals for harmonicity
ci_low4 = x_bar4 - mrg_err4
ci_upp4 = x_bar4 + mrg_err4
print("Confidence Interval of the mean of pitch: %.2f to %.2f" % (ci_low4, ci_upp4))

#get the lower and upper confidence intervals for harmonicity
ci_low5 = x_bar5 - mrg_err5
ci_upp5 = x_bar5 + mrg_err5
print("Confidence Interval of the mean of pulse: %.2f to %.2f" % (ci_low5, ci_upp5))







# Method 2: Use the statsmodels package
import statsmodels.stats.weightstats as stm

ci_low1_stm, ci_upp1_stm = stm._zconfint_generic(x_bar1,std_err1,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean of jitter: %.2f to %.2f" % (ci_low1_stm, ci_upp1_stm))

ci_low2_stm, ci_upp2_stm = stm._zconfint_generic(x_bar2,std_err2,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean of shimmer: %.2f to %.2f" % (ci_low2_stm, ci_upp2_stm))

ci_low3_stm, ci_upp3_stm = stm._zconfint_generic(x_bar3,std_err3,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean of harmonicity: %.2f to %.2f" % (ci_low3_stm, ci_upp3_stm))

ci_low4_stm, ci_upp4_stm = stm._zconfint_generic(x_bar4,std_err4,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean of pitch: %.2f to %.2f" % (ci_low4_stm, ci_upp4_stm))

ci_low5_stm, ci_upp5_stm = stm._zconfint_generic(x_bar5,std_err5,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean of pulse: %.2f to %.2f" % (ci_low5_stm, ci_upp5_stm))




