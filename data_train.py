import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def generate_expanded_jaipur_data(n=10000):
    np.random.seed(101)
    locations = [
        'C-Scheme', 'Raja Park', 'Malviya Nagar', 'Vaishali Nagar', 
        'Mansarovar', 'Jagatpura', 'Shyam Nagar', 'Pratap Nagar', 
        'Civil Lines', 'Bapu Nagar', 'Tonk Road', 'Ajmer Road', 
        'Kalwar Road', 'Sitapura'
    ]
    property_types = ['Apartment/Flat', 'Independent Villa', 'Penthouse', 'Builder Floor', 'Residential Plot']
    
    base_rates = {
        'C-Scheme': 15500, 'Civil Lines': 13000, 'Bapu Nagar': 12000,
        'Raja Park': 11000, 'Malviya Nagar': 9800, 'Shyam Nagar': 8500,
        'Vaishali Nagar': 8200, 'Mansarovar': 7200, 'Tonk Road': 6800,
        'Ajmer Road': 5500, 'Jagatpura': 5400, 'Pratap Nagar': 4800,
        'Kalwar Road': 3800, 'Sitapura': 3500
    }
    
    data = []
    for _ in range(n):
        loc = np.random.choice(locations)
        p_type = np.random.choice(property_types)
        
        if p_type == 'Residential Plot':
            sqft = np.random.randint(900, 4500)
            bhk = 0
            amenities_score = np.random.randint(1, 4)
        elif p_type == 'Penthouse':
            sqft = np.random.randint(3000, 6000)
            bhk = np.random.randint(4, 6)
            amenities_score = np.random.randint(7, 11)
        elif p_type == 'Independent Villa':
            sqft = np.random.randint(1500, 5000)
            bhk = np.random.randint(3, 6)
            amenities_score = np.random.randint(5, 10)
        else:
            sqft = np.random.randint(500, 2500)
            bhk = np.random.randint(1, 4)
            amenities_score = np.random.randint(3, 9)
            
        age = np.random.randint(0, 20)
        metro_dist = np.random.uniform(0.1, 12.0)
        
        price = (sqft * base_rates[loc])
        if bhk > 0: price += (bhk * 500000)
        price += (amenities_score * 250000) - (age * 90000) - (metro_dist * 120000)
        price += np.random.normal(0, price * 0.05)
        price = max(1000000, round(price, -4))
        
        roi = np.random.uniform(3.5, 9.8) if p_type != 'Residential Plot' else np.random.uniform(6.5, 14.5)
        demand_index = np.random.randint(35, 100)
        
        data.append([loc, p_type, sqft, bhk, age, round(metro_dist, 2), amenities_score, round(roi, 2), demand_index, price])

    return pd.DataFrame(data, columns=['Location', 'Property_Type', 'Sqft', 'BHK', 'Age', 'Metro_Dist', 'Amenities_Score', 'ROI_Pct', 'Demand_Index', 'Price'])

print("⏳ Jaipur ka heavy dataset ban raha hai...")
df_jaipur = generate_expanded_jaipur_data(10000)

df_ml = pd.get_dummies(df_jaipur, columns=['Location', 'Property_Type'])
X = df_ml.drop(['Price', 'ROI_Pct', 'Demand_Index'], axis=1)
y = df_ml['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("🧠 Machine Learning Model train ho raha hai...")
model = RandomForestRegressor(n_estimators=150, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

joblib.dump(model, 'jaipur_real_estate_model.pkl')
df_jaipur.to_csv('jaipur_real_estate_data.csv', index=False)
print("✅ Done! Data aur AI model dono file save ho gayi hain.")