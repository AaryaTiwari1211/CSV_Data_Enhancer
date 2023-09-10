import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY")

def enhance_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\"{text}\" This is the data for a college. Enhance the data without increasing the word count",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def enhance_and_track_changes(dataframe, column_name):
    enhanced_column_name = f'{column_name}_enhanced'
    dataframe[enhanced_column_name] = dataframe[column_name].apply(enhance_text)

    print("Values before enhancement: ")
    print(dataframe[column_name])
    
    print("\nEnhanced Values after enhancement: ")
    print(dataframe[enhanced_column_name])
    
    return dataframe

csv_file_path = 'Sample Universities.csv'
df = pd.read_csv(csv_file_path)

print("Columns in the CSV file: ")
print(df.columns)

column_to_enhance = 'Overview'

# Enhance the specified column and track changes
df = enhance_and_track_changes(df, column_to_enhance)

# Save the DataFrame with both original and enhanced values to a new CSV file
enhanced_csv_path = 'Enhanced_Sample_Universities.csv'
df.to_csv(enhanced_csv_path, index=False)

print(f"Enhanced data with original values saved to {enhanced_csv_path}")
