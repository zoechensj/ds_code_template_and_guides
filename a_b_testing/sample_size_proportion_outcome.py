

# estimate sample size via power analysis
from statsmodels.stats.power import TTestIndPower
import scipy.stats as stats
import numpy as np

# calculate the sample size for PROPORTIONs outcome samples
def effect_size(p1, p2):
    """
    Effect size is to measure the magnitude of the difference between two groups -- that is how different the two groups are from each other. 
    Effect size can refer to the raw difference between group means, or absolute effect size, as well as standardized measures of effect.
    Read more here: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3444174/
    """
    p = (p1+p2)/2
    minimum_detectable_effect = abs(p1-p2)
    # np.sqrt(p*(1-p)) -> pooled standard deviation, the estimated difference between two population proportions / pooled estimated standard deviation
    es = minimum_detectable_effect / np.sqrt(p*(1-p)) 
    return es

def power_analysis(p1, p2, alpha=0.05, power=0.8):
    es = effect_size(p1, p2)
    z_alpha = stats.norm.ppf(1-alpha/2)
    z_beta = stats.norm.ppf(power)
    result = 2 * ((z_alpha+z_beta) / es ) ** 2
    return result

# Or you can just use the TTestIndPower class from statsmodels to solve the sample size
es = effect_size(0.46, 0.56)
analysis = TTestIndPower()
# ratio =1 means the sample size of two groups are equal
sample_size = analysis.solve_power(es, nobs1=None, ratio=1, power=0.8, alpha=0.05) 

# value setup for the calculation
p1 = 0.46 # the baseline 
p2 = p1 + 0.1 # the expected improvement, 0.1 is the minimum detectable effect you want to detect

print(es, sample_size)
print(power_analysis(0.46, 0.56))