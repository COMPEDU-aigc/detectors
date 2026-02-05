import openai
import pandas as pd
# Set up API key
openai.api_key = ""

system_intel = """
Please answer the following question as accurately and comprehensively as possible. 
Write your response in clear academic English, following the reasoning expected in a student assignment. 
Question:
"""

log_file_path = 'stutask_input.csv'
output_csv_path = 'stutask_output.csv'
data = []
# Read and process each line of log files
with open(log_file_path, 'r') as file:
    for line_number, line in enumerate(file, 1):
        # Utilize OpenAI's API directly
        try:
            result = openai.ChatCompletion.create(model="gpt-3.5",
                                                  messages=[{"role": "system", "content": system_intel},
                                                            {"role": "user", "content": line}])
            processed_text = result['choices'][0]['message']['content']
            print(f"Line {line_number}: {processed_text}")
            # Add original and processed data to a list
            data.append({'Original Text': line.strip(), 'Processed Text': processed_text})
        except Exception as e:
            print(f"An error occurred: {e}")

# Create a DataFrame using the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print("Processing complete, data saved: ", output_csv_path)
