
obj1 = Data_Analysis("/Users/Julien/Downloads/FL_insurance_sample.csv")
print(obj1.get_summary_statistics())
print(obj1.get_histogram('policyID', 100))

obj1.get_histogram('policyID', 100).show()
