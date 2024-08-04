# Salary Prediction Model
 ## Streamlit App Salary Prediction For Differnet Job Titles with Dashboard Showing Trend of Salaries Over 2021 to 2024
### This Streamlit web application provides a dashboard to visualize trends in job title mean prices (e.g., ML, SE, Computer Biologist) and a predictive model to estimate salaries from 2021 to 2024.

Clone the repository:
```bash
git clone https://github.com/MuhammadUmer241/Salary-Prediction-Model
```
Create a Virtual Enviroment
```bash
python -m venv my_env
```
Navigate to the project directory:
```Bash
cd Salary-Prediction-Model\src\main.py
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Running the App
```commandline
python -m streamlit run main.py
```

## This App contains two pages 
### 1.Prediction


![Screenshot 2024-08-04 204935](https://github.com/user-attachments/assets/671e9aa1-08b5-4650-90c8-6b561b6059dc)
#### Employment Type: Users can select the type of employment (e.g., Full-time (FT), Part-time(PT), Contract(CT)).
#### Work Year: Users can specify the year for which they want to predict or analyze salaries Over 2021-2024.
#### Employee Resident: Users can indicate the country or region of the employee.
#### Experience Level: Users can select the experience level of the employee (e.g., Entry-level(EL), Mid-Level(ML) etc).
#### Company Size: Users can choose the company size to refine salary predictions.
#### Remote Ratio: User can enter the Percentage of Remote work they did (ideal to add 0,50,100 if values are closer to these numbers ) 
#### Company Location: User can Select the Company Location (US, PKR etc)

### 2.Dashboard
![Screenshot 2024-08-04 205129](https://github.com/user-attachments/assets/0d4ba59b-e2a0-46e1-b6e4-808c85554e5d)
#### Select Year Dropdown: This enables you to filter the displayed data by year(2021-2024).
#### Mean Salary by Job Title and Work Year Chart: This line chart shows the average salary for various job titles over the years. The years are represented on the x-axis, and the mean salary (in USD) is on the y-axis.
#### The Metric above shows the job role with highest Mean Salary (if from drop down no year is selected it will calculate the higest mean salaries over 2021-2024)



