import streamlit as st
import pandas as pd
import pickle
import os
import plotly.graph_objects as go

project_root = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(project_root, "data", "salaries.csv")
df = pd.read_csv(data_path)

st.set_page_config(layout="wide")


page = st.sidebar.selectbox("Select Page", ["Prediction Model", "Dashboard"])
if page== "Prediction Model":
    st.header("📈Welcome To The Salaray Prediction Model")

    col1, col2, col3 = st.columns((3, 1, 1))
    with col3:
        years = range(2021, 2024)
        work_year = st.selectbox(label="Work Year", options=years)
    with col2:
        employment_type = st.selectbox("Employment Type", df['employment_type'].unique())
    with col1:
        job_title = st.selectbox("Job Title", df["job_title"].unique())

    col1, col2, col3 = st.columns((3, 1, 1))
    with col1:
        employee_residence = st.selectbox("Employee Resident", df['employee_residence'].unique())
    with col2:
        experience_level = st.selectbox("Experience Level", df["experience_level"].unique())
    with col3:
        remote_ratio = st.number_input("Enter Remote Ratio", max_value=100, min_value=0)

    col1, col2, col3 = st.columns((3, 1, 1))
    with col1:
        company_location = st.selectbox("Company Location", df["company_location"].unique())
    with col2:
        company_size = st.selectbox("Company Size", df["company_size"].unique())
    with col3:
        pass
        # salary_currency= st.selectbox("salary_currency", df["salary_currency"].unique())
    dict_ = {"work_year": [work_year],
             "experience_level": [experience_level],
             "employment_type": [employment_type],
             "job_title": [job_title],
             "employee_residence": [employee_residence],
             "remote_ratio": [remote_ratio],
             "company_location": [company_location],
             "company_size": [company_size]
             }

    df_ = pd.DataFrame(dict_)

    with open('pipeline_F.pkl', 'rb') as f:
        model = pickle.load(f)
    price= model.predict(df_)
    col1,col2,col3= st.columns((3,1,1))
    with col3:
        button= st.button("Submit")
    if button:
        sal = f"The Expected Salary is {int(price)}$🤝"
        st.header(sal)


else:
    work_years = list(df["work_year"].unique())
    year = st.sidebar.multiselect("Select Year", work_years)


    if year:
        filtered_dfs = []
        for yr in year:
            filtered_df = df[df["work_year"] == yr]
            filtered_dfs.append(filtered_df)
        df = pd.concat(filtered_dfs)
    else:
        df = df

    col1, col2=st.columns(2)
    with col1:
        st.title("💼 Dashboard")
    with col2:
        highest_paying_jobs = df.groupby('job_title')['salary_in_usd'].mean()

        highest_paying_job = highest_paying_jobs.nlargest(1)

        highest_paying_job_title = highest_paying_job.index[0]
        highest_paying_job_salary = highest_paying_job.values[0]

        st.metric("Highest Paying Job", highest_paying_job_title, f"${highest_paying_job_salary}")

    job_titles = df['job_title'].unique()

    # Create a figure
    fig = go.Figure()

    # Add traces for each work year (assuming you have a 'work_year' column)
    for work_year in df['work_year'].unique():
        year_data = df[df['work_year'] == work_year]
        fig.add_trace(go.Scatter(
            x=job_titles,  # Use unique job titles as x-axis
            y=year_data.groupby('job_title')['salary_in_usd'].mean(),
            mode='lines',
            name=f'Work Year {work_year}'
        ))

    # Customize the layout (optional)
    fig.update_layout(
        title='Mean Salary by Job Title and Work Year',
        xaxis_title='Job Title',
        yaxis_title='Mean Salary (USD)',
        yaxis_showgrid=False
    )

    st.plotly_chart(fig)



