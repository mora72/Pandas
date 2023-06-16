import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

complaints = pd.read_csv('./csv/311-service-requests.csv')
print(complaints[['Complaint Type', 'Borough']])  # mostra 2 colunas do dt

print(complaints['Complaint Type'].value_counts())  # quantidade de ocorrências por tipo. tipo count * group by
complaints_counts = complaints['Complaint Type'].value_counts()
print(complaints_counts[:10])

complaints_counts[:10].plot(kind='bar')  # só funciona no console. gráfico de barras

noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]  # pega só um tipo de complaint
print(noise_complaints)

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"  # filtra um tipo
in_brooklyn = complaints['Borough'] == "BROOKLYN"  # filtra um local
result = complaints[is_noise & in_brooklyn]  # pega os registros que atendem os dois critérios acima
print(result['Complaint Type', 'Borough', 'Created Date', 'Descriptor'][:10])  # seleciona algumas colunas deste result

# mostra qual Borough tem a maior quantidade de noise complaint. Pareto
noise_complaints = complaints[is_noise]
noise_complaint_counts = noise_complaints['Borough'].value_counts()

complaint_counts = complaints['Borough'].value_counts()  # conta o total de complaints por Borough indep do tipo
print(noise_complaint_counts / complaint_counts)  # mostra o % de complaints de noise sobre o total
# (noise_complaint_counts / complaint_counts.plot(kind='bar')  # só func no console
