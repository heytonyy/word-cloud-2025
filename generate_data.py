import pandas as pd

# Create sample data
data = {
    'Timestamp': [''] * 30,
    'Email Adress': [''] * 30,
    'Name': [''] * 30,
    'Period': ['Period 1'] * 5 + ['Period 2'] * 5 + ['Period 3'] * 5 + 
         ['Period 4'] * 5 + ['Period 5'] * 5 + ['Period 6'] * 5,
    'Word of 2025': [
        # Period 1 words
        'Determination', 'courage', 'Perseverance', 'GROWTH', 'Success',
        # Period 2 words
        'Leadership', 'Innovation', 'Creativity', 'Excellence', 'Wisdom',
        # Period 3 words
        'Kindness', 'Empathy', 'Compassion', 'Hope', 'Peace',
        # Period 4 words
        'Resilience', 'Strength', 'Focus', 'Achievement', 'Purpose',
        # Period 5 words
        'Joy', 'Gratitude', 'Love', 'Happiness', 'Unity',
        # Period 6 words
        'Integrity', 'Honor', 'Respect', 'Trust', 'Faith'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sample_wordcloud_data.csv', index=False)