import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv('data_survey.csv')

# Nomor 1
# Jumlah Data
jumlah_data = len(df)
# Jumlah Data Unik
jumlah_data_unik = df['id'].nunique()
# Jumlah Fitur
jumlah_fitur = len(df.columns)
# Cek Missing Values
missing_values = df.isnull().sum()

# Menampilkan hasil
print(f"1. Jumlah data: {jumlah_data}")
print(f"2. Jumlah data unik: {jumlah_data_unik}")
print(f"3. Jumlah fitur: {jumlah_fitur}")
print("\n4. Missing Values:")
print(missing_values)

# Menangani Missing Values (Jika Ada) (apabila menggunakan data asli maka Handling Missing Value diabaikan)
# Mengisi kolom 'age' dengan nilai rata-rata dari kolom tersebut
df['age'].fillna(df['age'].mean(), inplace=True)
# Mengisi kolom 'age_range' dengan nilai yang paling sering muncul (mode)
df['age_range'].fillna(df['age_range'].mode()[0], inplace=True)
# Mengisi kolom 'province' dengan nilai yang paling sering muncul (mode)
df['province'].fillna(df['province'].mode()[0], inplace=True)
# Mengisi kolom 'city' dengan nilai yang paling sering muncul (mode)
df['city'].fillna(df['city'].mode()[0], inplace=True)
# Mengisi kolom 'gender' dengan nilai yang paling sering muncul (mode)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)
# Mengisi kolom 'interest' dengan nilai yang paling sering muncul (mode)
df['interest'].fillna(df['interest'].mode()[0], inplace=True)
# Mengisi kolom 'interest_detail' dengan nilai yang paling sering muncul (mode)
df['interest_detail'].fillna(df['interest_detail'].mode()[0], inplace=True)

# Print the modified DataFrame
print("\nDataFrame after handling missing values:")
print(df.head())

# Simpan Hasil (Opsional)
# df.to_csv('hasil_analisis_clean.csv', index=False)

# Nomor 2: Demographics Analysis
# Gender Distribution
gender_count = df['gender'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Gender Distribution')
plt.show()

# Age Range Distribution
age_range_count = df['age_range'].value_counts()

plt.figure(figsize=(8, 6))
sns.barplot(x=age_range_count.index, y=age_range_count.values, palette='viridis')
plt.title('Age Range Distribution')
plt.xlabel('Age Range')
plt.ylabel('Count')
# plt.show()

# Province Distribution
province_count = df['province'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=province_count.index, y=province_count.values, palette='coolwarm')
plt.title('Province Distribution')
plt.xlabel('Province')
plt.ylabel('Count')
plt.xticks(rotation=45)
# plt.show()

# City Distribution
city_count = df['city'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=city_count.index, y=city_count.values, palette='coolwarm')
plt.title('City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
# plt.show()

# Interest Distribution
interest_count = df['interest'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=interest_count.index, y=interest_count.values, palette='pastel')
plt.title('Interest Distribution')
plt.xlabel('Interest')
plt.ylabel('Count')
plt.xticks(rotation=45)
# plt.show()

# Interest Detail Distribution
interest_detail_count = df['interest_detail'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=interest_detail_count.index, y=interest_detail_count.values, palette='pastel')
plt.title('Interest Detail Distribution')
plt.xlabel('Interest Detail')
plt.ylabel('Count')
plt.xticks(rotation=45)
# plt.show()

# Nomor 3
# Filter data untuk daerah Jawa Barat dan Jawa Tengah
jabar_jateng_data = df[(df['province'] == 'Jawa Barat') | (df['province'] == 'Jawa Tengah')]

# Gender Distribution
gender_count_jabar = jabar_jateng_data[jabar_jateng_data['province'] == 'Jawa Barat']['gender'].value_counts()
gender_count_jateng = jabar_jateng_data[jabar_jateng_data['province'] == 'Jawa Tengah']['gender'].value_counts()

# Buat visualisasi
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.pie(gender_count_jabar, labels=gender_count_jabar.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Gender Distribution (Jawa Barat)')

plt.subplot(1, 2, 2)
plt.pie(gender_count_jateng, labels=gender_count_jateng.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Gender Distribution (Jawa Tengah)')

plt.tight_layout()
# plt.show()

# Age Range Distribution
age_range_count_jabar = jabar_jateng_data[jabar_jateng_data['province'] == 'Jawa Barat']['age_range'].value_counts()
age_range_count_jateng = jabar_jateng_data[jabar_jateng_data['province'] == 'Jawa Tengah']['age_range'].value_counts()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.barplot(x=age_range_count_jabar.index, y=age_range_count_jabar.values, palette='viridis')
plt.title('Age Range Distribution (Jawa Barat)')
plt.xlabel('Age Range')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
sns.barplot(x=age_range_count_jateng.index, y=age_range_count_jateng.values, palette='viridis')
plt.title('Age Range Distribution (Jawa Tengah)')
plt.xlabel('Age Range')
plt.ylabel('Count')

plt.tight_layout()
# plt.show()

# Nomor 4
def kategorisasi_umur(umur):
    if umur >= 60:
        return 'Baby Boomers'
    elif 40 <= umur <= 59:
        return 'Gen X'
    elif 25 <= umur <= 39:
        return 'Gen Millennial'
    elif 10 <= umur <= 24:
        return 'Gen Z'
    else:
        return 'Gen Alpha'

df['age_category'] = df['age'].apply(kategorisasi_umur)

# Hitung distribusi kategori baru
kategori_count = df['age_category'].value_counts()

# Buat visualisasi
plt.figure(figsize=(8, 6))
sns.barplot(x=kategori_count.index, y=kategori_count.values, palette='viridis')
plt.title('Distribusi Kategori Umur Baru')
plt.xlabel('Kategori Umur')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
# plt.show()
