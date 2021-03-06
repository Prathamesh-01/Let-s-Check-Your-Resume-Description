# -*- coding: utf-8 -*-
"""resume_checker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mcxMnixDb3BjgjMQUO9PX9unBE_x46tu
"""

# For now this is simple resume checker, but moving forward i would be building a machine learning resume checker

!pip install docx2txt

import docx2txt
from google.colab import files
uploads = files.upload()

res = docx2txt.process("sample.docx")
print(res)

jobs_dick = docx2txt.process("Google Software Engineer Job Description.docx")
print(jobs_dick)

from sklearn.feature_extraction.text import CountVectorizer
filt = [res, jobs_dick]
cov = CountVectorizer()
cm = cov.fit_transform(filt)

from sklearn.metrics.pairwise import cosine_similarity
percents = cosine_similarity(cm)[0][1]*100
percents = round(percents, 2)

print('Your Description Matches Upto ' +  str(percents) + ' of the job description')