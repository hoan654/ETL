import pandas as pd

google_sheet_id = '1VCkHwBjJGRJ21asd9pxW4_0z2PWuKhbLR3gUHm-p4GI'
url = 'https://docs.google.com/spreadsheets/d/' + google_sheet_id + '/export?format=xlsx'
enrollies_data = pd.read_excel(url, sheet_name ='enrollies' )

enrollies_data.head()

enrollies_education = pd.read_excel('enrollies_education.xlsx' )

enrollies_education.head()

work_experience = pd.read_csv('work_experience.csv' )

work_experience.head()

!pip install pymysql

from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
training_hours = pd.read_sql_table('training_hours', engine)

training_hours.head()

tables = pd.read_html('https://sca-programming-school.github.io/city_development_index/index.html')


cities = tables[0]

cities.head()

employment = pd.read_sql_table('employment', engine)

employment.head()

enrollies_data.info()

enrollies_data['gender'] = enrollies_data['gender'].fillna(enrollies_data['gender'].mode()[0])

enrollies_data.info()

enrollies_data['full_name'] = enrollies_data['full_name'].astype('string')
enrollies_data['gender'] = enrollies_data['gender'].astype('category')
enrollies_data['city'] = enrollies_data['city'].astype('category')

enrollies_data.info()

enrollies_education.info()

enrollies_education['enrolled_university'] = enrollies_education['enrolled_university'].fillna(enrollies_education['enrolled_university'].mode()[0])
enrollies_education['education_level'] = enrollies_education['education_level'].fillna(enrollies_education['education_level'].mode()[0])
enrollies_education['major_discipline'] = enrollies_education['major_discipline'].fillna(enrollies_education['major_discipline'].mode()[0])

enrollies_education.info()

enrollies_education[['enrolled_university','education_level','major_discipline']] = enrollies_education[['enrolled_university','education_level','major_discipline']].astype('string')


enrollies_education.info()

work_experience.info()
work_experience.head(10)

work_experience.experience.unique()

work_experience['experience'] = work_experience['experience'].replace({'>20': '21', '<1': '0'})

work_experience['experience'] = work_experience['experience'].fillna(work_experience['experience'].mode()[0])

work_experience.company_size.unique()

work_experience['company_size'] = work_experience['company_size'].replace({'10/49': '10-49'})

work_experience.last_new_job.unique()

work_experience['last_new_job'] = work_experience['last_new_job'].replace({'>4': '5','never':'0'})

work_experience[['company_size','company_type','last_new_job']] = work_experience[['company_size','company_type','last_new_job']].fillna(work_experience[['company_size','company_type','last_new_job']].mode().iloc[0])

work_experience = work_experience.convert_dtypes()

db_path = 'datab_warehouse.db'
engine = create_engine(f'sqlite:///{db_path}')
enrollies_data.to_sql('Dim_Enrollies', engine, if_exists='replace', index=False)
enrollies_education.to_sql('Dim_enrollies_education', engine, if_exists='replace', index=False)
work_experience.to_sql('Dim_work_experience', engine, if_exists='replace', index=False)
training_hours.to_sql('Dim_training_hours', engine, if_exists='replace', index=False)
cities.to_sql('Dim_cities', engine, if_exists='replace', index=False)
employment.to_sql('Fact_employment', engine, if_exists='replace', index=False)