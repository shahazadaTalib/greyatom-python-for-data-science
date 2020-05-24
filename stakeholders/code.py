# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
fig = plt.figure(figsize = (10, 5)) 
plt.bar(loan_status.index,loan_status) 
plt.show()
#Code starts here


# --------------
#Code starts here




property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here




education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
import pandas as pd
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
#LoanAmount=pd.Series(graduate)
graduate['LoanAmount'].plot(kind='density', label='Graduate')

#LoanAmount.plot(kind='density',label='Graduate')
#LoanAmount=pd.Series(not_graduate)
not_graduate['LoanAmount'].plot(kind='density', label='NOt Graduate')

#LoanAmount.plot(kind='density',label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1)
ax_1.scatter('ApplicantIncome','LoanAmount')
ax_1.set(title='Applicant Income')
ax_2.scatter('CoapplicantIncome','LoanAmuont')
ax_2.set(title='Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter('TotalIncome','LoanAmount')
ax_3.set(title='Total Income')


