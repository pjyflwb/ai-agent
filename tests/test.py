import pickle

with open(r'C:\Users\djct\Downloads\行情_原始.pkl', 'rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)