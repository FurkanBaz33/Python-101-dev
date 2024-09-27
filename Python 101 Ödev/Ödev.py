import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(Housing.csv)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.hist(df['area'], bins=10, color='blue', alpha=0.7)
plt.title('Area Histogram')
plt.xlabel('Area(sq ft)')
plt.ylabel('Frequency')


plt.subplot(1,3,2)
plt.hist(df['bedrooms'], bins=5, color='green', alpha=0.7)
plt.title('Bedrooms Histogram')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Frequency')


plt.subplot(1,3,3)
plt.hist(df['stories'], bins=3, color='orange', alpha=0.7)
plt.title('Stories Histogram')
plt.xlabel('Number of Stories')
plt.ylabel('Frequency')


plt.tight_layout()
plt.show
