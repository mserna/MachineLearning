from estimate_gaussian import EstimateGuassian
from multivariate_gaussian import MultivariateGaussian 

# Testing EstimateGaussina class functions
test_gauss = EstimateGuassian('test_data.xls')
[mu, sigma2] = test_gauss.estimate()
test_gauss.plot_data()

# Testing MultivariateGaussian class functions - For later
mult_pval = MultivariateGaussian('test_data.xls', mu, sigma2)
prob_density_func = mult_pval.compute_density_func()

# Testing Select Thresholds class functions

