#!/usr/bin/env python
"""
Program 10

@author: vikki
"""

#Job list
JobList = [['business intelligent analyst', 'Google', 'Mountain View CA', 'NA', 'full time', 'BS/BA', '4', ['business intelligence', 'data reporting', 'mySQL', 'Object oriented programming', 'python', 'Data Warehousing', 'Visualization', 'statistical modeling', 'quantitative modeling', 'analytical problem solving', 'business judgment', 'presentation']],
['Data Scientist', 'Techshed', 'Foster City', 'NA', 'full time', 'BS/BA', '3+', ['data analysis', 'forecasting', 'ROI Modeling', 'Business Intelligence', 'SQL', 'R', 'SAS', 'Data warehouse programming', 'marketing strategies', 'business support']],
['Data Scientist', 'Microsoft', ' Bellevue WA', 'NA', 'full time', 'MS', '0', ['SQL', 'analytical problem solving', 'R', 'Matlab', 'SAS', 'Python', 'manupulating and analyzing data', 'online experimentation', 'research', 'computing tools', 'Statistical modeling', 'defining metrics', 'gathering datasets', 'data conditioning', 'data analysis', 'visualization', 'communication']],
['Senior Data scientist', 'Microsoft', 'Redmond WA', 'NA', 'full time', 'MS/PhD', '3', ['research', 'data analysis', 'statistical modeling', 'machine learning', 'visualization', 'presentation', 'communication', 'analytical problem solving', 'R', 'Object oriented programming', 'predictive modeling', 'Python', 'hadoop', 'SQL', 'cloud storage', 'data mining']],
['Data Analyst', 'Tribal ddb', 'San Francisco CA', 'NA', 'full time', 'BS/BA', '2', ['in depth analysis', 'Web analytics', 'SQL', 'Excel', 'Access', 'SAS', 'SPSS', 'ad-hoc requests', 'WebTrends', 'Omniture', 'Coremetrics', 'Fireclick', ' part of a team', 'flexible', 'customer service ethic', 'communication', 'presentation', 'analytical problem solving']],
['Data Scientist', 'AppLovin', 'San Francisco CA', 'NA', 'full time', 'BS/MS/PhD', '2+', ['analyze data', 'Java', 'C', 'Python', 'SQL', 'algorithms', 'R', 'Matlab', 'Octave', 'Perl', 'MapReduce', 'Natural Language processing', 'Mobile Advertising industry']],
['Data Scientist', 'Storm8', 'Redwood City CA', 'NA', 'full time', 'MS/PhD', '5+', ['large datasets', 'data warehouses', 'data mining', 'SQL', 'R', 'Python', 'SAS', 'Java', 'C++', 'statistical modeling', 'predictive analytics', 'Strong communication', 'presentation skills', 'Statistics', 'Math', 'Computer Science', 'Operations Research']],
['Data Scientist', 'Machine Zone Inc', 'Palo Alto CA', 'NA', 'full time', 'BS+', '3+', [' Applied Math', 'Statistics', 'Computer Science', 'retention analytics', 'mathematical modeling', 'quantitative problem solving', 'predictive analysis', 'machine learning', 'data mining', 'R', 'MATLAB', 'SAS', 'Scripting experience', 'Python', 'Ruby', 'Javascript', 'Unix', 'Linux', 'OS', 'Hadoop', 'Hive', 'Map/Reduce', 'presentation', 'communication skills']],
['Software Engineer', 'Google', 'Mountain View CA USA', 'NA', 'full time', 'MS', '4', ['Java', 'C/C++', 'Python', 'database design', 'SQL', 'knowledge of TCP/IP', 'network programming', 'Large systems software design', 'knowledge of Unix/Linux', 'cloud technologies', 'data structures', 'algorithms', 'Mathematics', 'Statistics', 'Engineering', 'analytical problem solving', 'debugging', 'presentation']],
['Workforce Analyst', 'Google', 'Mountain View CA USA', 'NA', 'full time', 'MS', '2', ['Business Administration', 'Computer Science', 'Finance', 'Statistics', 'management consulting', 'business strategy', 'SQL', 'Python', 'Ability to self-start', 'self-direct work in an unstructured environment; comfort dealing with ambiguity', 'communications skills', 'client service-oriented', 'creativity', 'diligence']],
['Network Engineer', 'Google', 'Austin TX USA', 'NA', 'full time', 'BS', '6', ['Electrical Engineering', 'IP network performance management', 'network troubleshooting', 'network operations', 'network engineering', 'telecommunications', 'Python', 'Perl', 'TCP/IPv6', 'network subscriber management', 'L2/L3 LAN/WAN network protocols', 'IP gateway firewalls', 'GPON', 'Ethernet', 'DWDM optical transport systems']],
['Web Developer', 'Google', 'San Bruno CA USA', 'NA', 'full time', 'MS', '7', ['developing compatible websites and applications', 'WebGL', 'JavaScript libraries', 'Closure', 'AngularJS', 'Greensock', 'Canvas/CSS animation', 'Google App Engine', 'Google Custom Search', 'Google Analytics', 'Strong consistency', 'Java', 'C/C++', 'Excellent leadership', 'communication skills', 'project management', 'organizational skills', 'HTML5', 'CSS3', 'JavaScript', 'Python', 'mobile development', 'content management']],
['Android security Analyst', 'Google', 'Mountain View CA USA', 'NA', 'full time', 'BS', '4', ['Dremel', 'Python', 'Flume', 'Java', 'databases', 'SQL', 'MySQL', 'MapReduce', 'Hadoop', 'spreadsheet software', 'Mathematics', 'Statistics', 'Engineering', 'mobile fraud investigation', 'risk management', 'e-commerce', 'collecting large data', 'managing large data', 'synthesizing large data sets', ' statistical modeling', 'data mining', 'data analysis']],
['senior data scientist', 'fliptop', 'San Francisco CA', 'NA', 'full time', 'Advanced degree', '3+', ['natrual language processing', 'computational linguistics', 'maching learning', 'linux', 'java', 'python', 'scala', 'R', 'SQL', 'Mahout', 'Hadoop', 'BSP computing', 'noSQL', 'database', 'API', 'NLP', 'statistics', 'predictive modeling', 'algorithms']],
['data scientist', 'groupon', 'palo alto CA', 'NA', 'full time', 'PhD/MS/BS', 'new grad', ['user behavior modeling', 'personalization', 'forecasting', 'optimization', 'maching learning', 'data mining', 'applied mathematics', 'C++', 'ruby', 'java', 'python', 'SQL', 'Hadoop', 'statistics', 'predictive', 'algorithms']],
['data scientist advanced analytics and machine learning', 'oracle', 'redwood city CA', 'NA', 'full time', 'BS', 'NA', ['business intelligence', 'data exploration', 'leadership', 'advanced analytics', 'architect', ' software design', 'analysis', 'data processing', 'technical', 'cloud', 'maching learning', 'data mining', 'scala', 'java', 'python', 'Hadoop', 'spark', 'mahout']],
['data scientist', 'oracle', 'cupertino CA', 'NA', 'full time', 'MS', '8+', ['data exploration', 'hypothesis creation', 'scaling', 'engineering', 'statistics', 'machine learning', 'analysis', 'model building', 'technical', 'java', 'c++', 'scala', 'python', 'classification', 'regression', 'clustering', 'algorithms', 'pig', 'hadoop', 'hive', 'spark']],
['business analyst', 'salesforce', 'san francisco CA', 'NA', 'full time', 'BS/MS/PhD', 'NA', ['reporting', 'data capture', 'data storage', 'data analysis', 'technical', 'research', 'problem solving skills', 'IT']],
['Data Analyst', 'Google', 'Mountain View, CA', 'NA', 'Full-time', 'BA/BS', '3', ['Google Analytics', 'Omniture', 'Webtrends', 'Webmaster Tools', 'Tableau', 'SQL', 'Data Warehousing', 'Data Modeling', 'communication']],
['Data Analyst', 'Amazon', 'Seattle, WA', 'NA', 'NA', 'BS', '1', ['work effectively', 'Oracle SQL', 'MySQL', 'Excel', 'analytical skills', 'quantitative skills', 'develop business cases', 'root cause analysis', 'prioritize projects', 'verbal and written communication']],
['Data Scientist', 'NVIDIA', 'Santa Clara, CA', 'NA', 'NA', 'CE/EE', '2-5', ['strong programming skills', 'python', 'C', 'C++', 'LINUX', 'data analysis', 'applied statistics', 'statically modeling']],
['Data Architect', 'Zentek Infosoft Inc', 'San Ramon, CA', 'NA', 'contract', 'BS', '5', ['RDBMS', 'DB2 UDB', 'data architecture', 'data management', 'DataDictionary', 'Metadata', 'data warehouses', 'data marts', 'documenting design specification', 'Informatica', 'Informatica Power Center Designer', 'Business Objects']]]

# Club similar words in a dictonary called similar words
similar_words = [['data warehousing', 'data warehouses', 'data warehouse programming'], ['presentation', 'presentation skills'],
['unix', 'linux', 'knowledge of unix/linux'], ['data analytics', 'analyze data', 'analysis', 'data analysis'], 
['statistical modeling', 'analytical problem solving', 'analytical skills', 'quantitative modeling'],
['java','javascript'], ['database', 'rdbms', 'mysql', 'oracle sql', 'nosql', 'databases'], ['web analytics', 'google analytics'],
['networking', 'network programming', 'network operations']]

# Initialise the count value 
count = 0

# Create a empty dictionary with length same as JobList
a = dict()
for z in range(0, len(JobList)):
    a[z] = 0

# Helper function to count the frequency of skill/qualification (or simple word) provided by user 
# only if value of any key in dict a is 0, so that there wont be any repititive searchs
def freq(word):
    global JobList, count, i, a
    if a[i] == 0:
        for j in range(0, len(JobList[i][7])):
            if word.lower() == JobList[i][7][j].lower():
                count += 1
                a[i] = 1
#                print i, JobList[i][7][j]
    return count

# Main function to imput keyword from user and call the helper function to count the frequency
# If the keyword given is not found from the return value then check for the similar keywords present and call helper 
# function again to check if those similar keywords are present. Finally print the count value 
def main():  
    global i
    word = raw_input("Please enter a skill/qualification to search: ")
    
    for i in range(0, len(JobList)):
        freq(word)

        for k in range(0, len(similar_words)):
            if word in similar_words[k]:
                for l in range(0, len(similar_words[k])):
                    freq(similar_words[k][l])
                    
    print "\n\"" + str(word) + "\" is required by %d out of %d jobs" %(count, len(JobList))
 
# Call main function       
if __name__ == "__main__":
    main()
