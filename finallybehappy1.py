import pandas as pd

df = pd.read_excel (r'C:\Users\Roy\Desktop\Finally be happy\finallybehappy1.xlsx')
pd.set_option("display.max_rows", 329)
print (df)

Status = {'AL': 'Fully Illegal','AK': 'Fully legal','AZ': 'Mixed (Medical)','AR': 'Mixed (Medical)','CA': 'Fully legal','CO': 'Fully legal','CT': 'Mixed (Medical)','DE': 'Mixed (Medical)','District of columbia': 'Fully legal','FL': 'Mixed (Medical)','GA': 'Mixed','HI': 'Mixed (Medical)','ID': 'Fully Illegal', 'IL': 'Fully legal','IN': 'Mixed','IA': 'Mixed','KS': 'Fully Illegal','KY': 'Mixed','LA': 'Mixed','ME': 'Fully legal','MD': 'Mixed (Medical)', 'MA': 'Fully legal','MI': 'Fully legal','MN': 'Mixed (Medical)','MS': 'Fully Illegal','MO': 'Mixed (Medical)','MT': 'Mixed (Medical)','NE': 'Fully Illegal','NV': 'Fully legal','NH': 'Mixed (Medical)','NJ': 'Mixed (Medical)','NM': 'Mixed (Medical)','NY': 'Mixed  (Medical)','NC': 'Fully Illegal','ND': 'Mixed (Medical)','OH': 'Mixed (Medical)','OK': 'Mixed (Medical)','OR': 'Fully legal','PA': 'Mixed (Medical)','RI': 'Mixed (Medical)','SC': 'Fully Illegal','SD': 'Fully Illegal','TN': 'Fully Illegal','TX': 'Mixed','UT': 'Mixed (Medical)','VT': 'Fully legal','VA': 'Mixed','WA': 'Fully legal','WV': 'Mixed (Medical)', 'WI': 'Fully Illegal'};

with open('Output.txt', 'w') as file:
	pd.read_excel('finallybehappy1.xlsx').to_string(file, index=False)
	

input = open('Output.txt').read()
out = open('final.txt', 'w')
for i in Status.keys():
	input = input.replace(i, Status[i])
out.write(input)
out.close