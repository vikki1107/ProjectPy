#!/usr/bin/env python
"""
Data Visualization

@author: vikki
"""

# Import the required libraries
from collections import defaultdict as dd 
from matplotlib import pyplot as plt
import numpy as np

# Create a dictonary with a key value pair where value is the list if items
hard_skills = {"Programming": ["language", "r", "python", "C", "C++", "java", "c#", "VBA", "pandas", "SAS", "matlab", "SPSS","stata", \
"ruby", "octave", "perl", "scripting", "xml", "program", "php", ".net", "scala", "html", "css", "javascript", "jquery"],
               "Database": ["sql", "database", "access", "oracle", "db"],
               "OS": ["OS", "linux", "unix", "window"],
               "Statistics": ["quantitative", "statist", "simulation modeling", "mathematics", "analytical", "forecasting", \
"online experimentation", "qualitative analysis", "data model", "tree", "bayesian", "regression", "anova", "probability"],
               "Machine learning": ["web analytics", "algorithms", "data mining", "computational intelligence", "predictive modeling", "NLP", \
"time-series analysis", "machine learn"],
               "Data warehousing and BI": ["data reporting", "ssis", "ssrs", "ssas", "ssms", "cognos", "etl", "report", "infograph", "bo", "bi", \
"obiee", "qlikview", "business objects", "warehous", "spss"],
               "Data Visualization": ["tableau", "wave", "visual"],
               "MS Office": ["excel", "power point", "word", "powerpivot", "spreadsheet","powerpoint", "visio"],
               "Big data": ["hadoop", "reduce", "spark", "hive", "pig latin", "Cassandra", "cloud", "flume", "large data", "datameer", \
"big data"]}

soft_skills = {"Communication": ["present", "munication"], 
               "Teamwork/collaboration": ["interpersonal skills", "team oriented", "other team", "cross"],
               "Work ethic": ["Detail oriented", "organized", "prioritize," "work ethic", "personal initiative", "time management", \
"self", "comfort dealing with ambiguity", "client", "diligence", "flexible", "task", "working globally", "prioritizing assignments", "desire", \
"willing", "think", "proactive", "energetic"]}

business_skills ={"Problem solving": ["problem solving"],
                  "Project management": ["project management"],
                  "Business acumen": ["business judgment"],
                  "Creativity": ["creativity"],
                  "Leadership and strategic planning": ["leadership and strategic planning"], 
                  "Field knowledge": ["finance", "marketing", "sales", "fraud prevention", "advertising", "web development", \
"business administration", "management consulting", "mobile fraud investigation", "risk management", "e-commerce", "roi modeling", \
"analytics", "knowledge of cisco equipments", "networking technologies", "cleaning", "sourc", "testing" ],
                  "Management": ["quality management", "data management", "stakeholder"]}

education = {("Bachelor", "BA", "BS", "Master", "MBA", "MS", "PhD")}

similar_words = [['statist','statistics'], ['warehous','data warehousing'], ['linux', 'linux OS']]

# Initialize empty dictonaries to keep the count of all the required fields
title = dd(int)
company = dd(int)
location = dd(int)
salary = dd(int)
jobtype = dd(int)
degree = dd(int)
experience = dd(int)
skills = dd(int)

hardskills = dd(int)
softskills = dd(int)
busskills = dd(int)

keyskills = dd(int)

# Initialize counters
hcount = 0
scount = 0
bcount = 0
a = []

# Opens the input file and get each line into a list 
#with open("/media/vikki/Flex/CSUEB/Courses/MGMT6160/Project/VK_jobs3.txt", 'r') as f:
with open("E:\CSUEB\Courses\MGMT6160\Project\VK_jobs3.txt", 'r') as f:
    for line in f:
        a.append(line.strip().split(','))

# For each line check the title, company name, location, salary, jobtype, degree, experience and skills. Store the unique keys 
# and number of times it appears    
for i in range(len(a)):
    b = [s.lstrip() for s in a[i]]

    for i in range(len(b)):
        if i == 0: 
           title[b[i]] += 1
        elif i == 1:
            company[b[i]] += 1
        elif i == 2:
            location[b[i]] += 1
        elif i == 3:
            salary[b[i]] += 1
        elif i == 4:
            jobtype[b[i]] += 1
        elif i == 5:
           degree[b[i]] += 1
        elif i == 6:
           experience[b[i]] += 1
        elif i >= 7:
           skills[b[i]] += 1   
#print title

# Define a function to get the various skills with skill category 
def skill1(k, o, c): 
    for values in k:
        for z in k[values]:
            if z.lower() == 'r' or z.lower() == 'c' or z.lower() == 'c/c++' or z.lower() == 'c++':
                if z.lower() == word.lower():
                    o[z] += skills[word]
            else:
                if z.lower() in word.lower():
                    o[z] += skills[word]
                    c += skills[word]
    return k, o, c

# for all hard_skills, soft_skills and business_skills call the function which creates a dictonary and also gets the count 
# of the skills
for word in skills:
    hard_skills, hardskills, hcount = skill1(hard_skills, hardskills, hcount)
    soft_skills, softskills, scount = skill1(soft_skills, softskills, scount)
    business_skills, busskills, bcount = skill1(business_skills, busskills, bcount)
    
#print hardskills, "\n\n", softskills, "\n\n", busskills
#print hcount, scount, bcount

# Plot the chart for skills category
labels = 'Hard Skills', 'Soft Skills', 'Business Skills'
sizes = [hcount, scount, bcount]   
colors = ['yellowgreen', 'gold', 'lightskyblue']
explode = (0.1, 0, 0)
plt.figure(0, figsize=[7,7])
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig('Skillset.png', dpi=200)

# Store each item within hard_skill category into a different dictonary. 
for item in hard_skills:
    for item1 in hard_skills[item]:
        keyskills[item] += hardskills[item1]
#print keyskills

# Now plot a chart for skills within the Hardskills
labels1=[k for k in keyskills.keys()]
sizes1=[float(v) for v in keyskills.values()]
cmap = plt.cm.prism
colors1 = cmap(np.linspace(0., 1., len(labels1)))
explode1 = (0, 0, 0, 0, 0, 0.1, 0, 0, 0)
plt.figure(1, figsize=[11,9])
plt.pie(sizes1, explode=explode1, labels=labels1, colors=colors1, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig('Hardskills.png', dpi=200)

# Append the skill name defined within the hardskills with a proper name using a list similar_words
for i in range(len(similar_words)):
    hardskills[similar_words[i][1]] = hardskills.pop(similar_words[i][0])
#print hardskills
    
# A bar chart showing the count and the programming skills 
labels2 = []
sizes2 = []
for aac in hard_skills['Programming']:
    labels2.append(aac)
    sizes2.append(hardskills[aac])

y_pos = np.arange(len(labels2))
plt.figure(2, figsize=[10,10])
plt.barh(y_pos, sizes2, align='center', alpha=0.5)
plt.yticks(y_pos, labels2)
plt.xlabel('count')
plt.title('Programming Skills')
plt.savefig('progskills.png', dpi=200)

#hardskills['databases'] = hardskills['db'] + hardskills['database']
#del hardskills['db'], hardskills['database']

# Another bar chart to show count of jobs for corresponding degree. 
labels3=[k for k in degree.keys()]
sizes3=[float(v) for v in degree.values()]
y_pos = np.arange(len(labels3))
plt.figure(3, figsize=[20,8])
plt.bar(y_pos, sizes3, align='center')
plt.xticks(y_pos, labels3)
plt.ylabel('count')
plt.title('Degree Requirement')
plt.savefig('Degree.png', dpi=200)
