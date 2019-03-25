from estimate_gaussian import EstimateGuassian # EstimateGaussian class

# Testing Gaussian est
test_gauss = EstimateGuassian('test_data.xls')
est_data = test_gauss.estimate()
test_gauss.plot_data()