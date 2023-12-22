import pandas as pd
import matplotlib.pyplot as plt

# Membuat DataFrame
data = {'Mata Pelajaran': ['Matematika', 'Fisika', 'Kimia', 'Biologi', 'Bahasa Inggris'],
        'Nilai Rata-rata': [80, 75, 90, 85, 88]}
df = pd.DataFrame(data)

# Plot Bar
plt.bar(df['Mata Pelajaran'], df['Nilai Rata-rata'], color='skyblue')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-rata')
plt.title('Nilai Rata-rata Mata Pelajaran')
plt.show()
