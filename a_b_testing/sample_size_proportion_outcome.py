

# estimate sample size via power analysis
from statsmodels.stats.power import TTestIndPower
import scipy.stats as stats
import numpy as np

# calculate the sample size for PROPORTIONs outcome samples
def effect_size(p1, min_detectable_effect):
    p2 = p1 + min_detectable_effect
    p = (p1+p2)/2
    es = (p1-p2)/np.sqrt(p*(1-p)) # np.sqrt(p*(1-p)) -> pooled standard deviation, the estimated difference between two population proportions / pooled estimated standarded deviation
    return es

def power_analysis(p1, p2, alpha=0.05, belta=0.2):
    es = effect_size(p1, p2)
    z_alpha = stats.norm.ppf(1-alpha/2)
    z_beta = stats.norm.ppf(1-belta)
    result = 2 * ((z_alpha+z_beta) / es ) ** 2
    return result


print(power_analysis(0.46, 0.11))