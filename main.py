import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from better_profanity import profanity

# Initialize the profanity filter
profanity.load_censor_words()

# Function to filter inappropriate words
def filter_words(text):
    words = text.split()
    filtered_words = [word for word in words if not profanity.contains_profanity(word)]
    return ' '.join(filtered_words)

# Read the CSV file (upload .csv from Google Sheets to repo and change file path)
df = pd.read_csv('responses.csv')

# Group the words by period
period_groups = df.groupby('Period')


# Create a word cloud for each period
for period, group in period_groups:
    # Combine all words for this period into one string, converting to lowercase and trimming
    text = ' '.join(group['Word of 2025'].dropna().str.lower().str.strip())
    
    # Filter out inappropriate words
    clean_text = filter_words(text)
    
    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400,
                         background_color='white').generate(clean_text)
    
    # Create and save the plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title(f'Word Cloud - {period}')
    
    # Save each period's word cloud as a separate file
    plt.savefig(f'{period.replace(" ", "")}_wordcloud.png', bbox_inches='tight')
    plt.close()

all_words = ' '.join(df['Word of 2025'].dropna().str.lower().str.strip())

# Filter out inappropriate words
all_clean_text = filter_words(all_words)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400,
                      background_color='white').generate(all_clean_text)

# Create and save the plot
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.axis('off')
plt.title(f'Word Cloud - All Periods')

# Save each period's word cloud as a separate file
plt.savefig('all_periods_wordcloud.png', bbox_inches='tight')
plt.close()