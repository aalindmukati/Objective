import pandas as pd

student_dict = {
    'student': ["Aalind","Ritu","Sachin"],
    'score': [92,95,93]
}

for(key,value) in student_dict.items():
    print(f"Key:{key} and Value: {value}")

student_data_frame = pd.DataFrame(student_dict)

# ----Used to access the student row and score row----
for(index,row) in student_data_frame.iterrows():
    print(f"index: {index} | Student: {row['student']} | Score: {row['score']}")