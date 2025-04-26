import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/orders.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['TotalAmount'] = df['Quantity'] * df['Price']

total_revenue = df['TotalAmount'].sum()
print("Сумарний дохід магазину:", total_revenue)

average_total = df['TotalAmount'].mean()
print("Середнє значення TotalAmount:", average_total)

orders_per_customer = df.groupby('Customer').size()
print("Кількість замовлень по кожному клієнту:")
print(orders_per_customer)

high_value_orders = df[df['TotalAmount'] > 500]
print("\nЗамовлення, де TotalAmount > 500:")
print(high_value_orders)


sorted_df = df.sort_values('OrderDate', ascending=False)
print("\nЗамовлення, відсортовані за OrderDate (зворотній порядок):")
print(sorted_df)

start_date = pd.to_datetime('2023-06-05')
end_date = pd.to_datetime('2023-06-10')
orders_in_period = df[(df['OrderDate'] >= start_date) & (df['OrderDate'] <= end_date)]
print("\nЗамовлення з 5 по 10 червня включно:")
print(orders_in_period)

category_summary = df.groupby('Category').agg(
    TotalItems=('Quantity', 'sum'),
    TotalSales=('TotalAmount', 'sum')
)
print("\nЗгруповані дані за Category:")
print(category_summary)

top_customers = df.groupby('Customer')['TotalAmount'].sum().nlargest(3)
print("\nТОП-3 клієнтів за загальною сумою покупок:")
print(top_customers)

orders_per_date = df.groupby('OrderDate').size()


plt.figure(figsize=(10, 5))
orders_per_date.plot(kind='line', marker='o')
plt.title('Кількість замовлень по датах')
plt.xlabel('Дата')
plt.ylabel('Кількість замовлень')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()