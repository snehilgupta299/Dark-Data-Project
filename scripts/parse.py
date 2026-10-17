import pandas as pd
import re
from collections import Counter, defaultdict

df = pd.read_excel("data/real_tickets.xlsx")

text_column = "Ticket Description"

stopwords = {
"the","to","and","a","an","is","it","i","im","ive","my","me","we","you","your",
"with","for","on","in","at","of","this","that","please","can","could","would",
"be","are","was","were","as","by","from","or","but","so",
"having","any","there","what","other","how","its","not","have"
}

# Issue dictionary
categories = {
"Login Issues": ["login","account","password","signin","authentication"],
"Payment Issues": ["payment","refund","charge","billing","invoice","price"],
"Software Bugs": ["bug","crash","error","problem","software","issue","persists"],
"Order Issues": ["order","delivery","shipping","cancel","tracking"],
"Data Issues": ["data","missing","lost","sync"]
}

category_counts = defaultdict(int)

for text in df[text_column].dropna():
    text = str(text).lower()
    text = re.sub(r"\{.*?\}", "", text)
    text = re.sub(r"[^a-z\s]", "", text)

    words = text.split()

    for category, keywords in categories.items():
        if any(word in words for word in keywords):
            category_counts[category] += 1

print("ISSUE CATEGORIES:")
for k,v in category_counts.items():
    print(k, v)

out = pd.DataFrame(category_counts.items(), columns=["category","count"])
out.to_excel("excel/category_summary.xlsx", index=False)

print("Excel file created: excel/category_summary.xlsx")
