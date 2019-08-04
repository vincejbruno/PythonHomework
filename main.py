# Print opening items 
print("Election Results")
print("------------------")

# import the csv file modules
import os
import csv
import statistics

output_file = os.path.join("election_results.txt")

# specify the cvs file in question for the analysis
csvpath = os.path.join('/Users/Vince/Desktop/WUSTL201907DATA2/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv')

# to read the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip first row in the csv file
    next(csvreader)

    #Define variables for candidate listing 
    candidate_list = []
    candidate_list_to_search = []
    #Loop through the cvs reader to create a list of the candidates and list for unique values
    for row in csvreader:
        candidate_list.append(str(row[2]))
        candidate_list_to_search.append(str(row[2]))
        candidate_list = list(set(candidate_list))

    #Obtain count for number of votes
    votes_cast = int(csvreader.line_num - 1)

    #Print the votes cast
    print("Total Votes: ", votes_cast)

    #Print line separater
    print("------------------")

    #Define variables for each individual candidate
    Can1 = candidate_list[0] 
    Can2 = candidate_list[1]
    Can3 = candidate_list[2]
    Can4 = candidate_list[3]

    #Define variable for total votes
    TotalVotes = 0
    
    #Loop through the large candidate list and obtain count for each and print
    for candidate_name in candidate_list:
        TotalVotes = candidate_list_to_search.count(candidate_name)
        print(candidate_name,": ",TotalVotes) 

    #Run individual if statements and calculate the percentage for each candidate
    if Can1 in candidate_list_to_search:
        Can1_Count = int(candidate_list_to_search.count(Can1))
        Can1_Percentage = round((Can1_Count / votes_cast) * 100,2)

    if Can2 in candidate_list_to_search:
        Can2_Count = int(candidate_list_to_search.count(Can2))
        Can2_Percentage = round((Can2_Count / votes_cast) * 100,2)

    if Can3 in candidate_list_to_search:
        Can3_Count = int(candidate_list_to_search.count(Can3))
        Can3_Percentage = round((Can3_Count / votes_cast) * 100,2)

    if Can4 in candidate_list_to_search:
        Can4_Count = int(candidate_list_to_search.count(Can4))
        Can4_Percentage = round((Can4_Count / votes_cast) * 100,2)

    #Print the candidate list
    #print(candidate_list) 
 
    print(Can1,":",Can1_Percentage,"%")
    print(Can2,":",Can2_Percentage,"%")
    print(Can3,":",Can3_Percentage,"%")
    print(Can4,":",Can4_Percentage,"%") 

    #Print line separator
    print("-----------------")

    #Create Dictionary of all of the candidates with there percentage
    Final_List = {Can1:Can1_Percentage, Can2: Can2_Percentage, Can3: Can3_Percentage, Can4: Can4_Percentage}

    #Return max value from the dictionary above and print
    maximum = max(Final_List, key=Final_List.get)
    print("Winner: ",maximum, Final_List[maximum],"%")

    #Print separator
    print("-----------------")

    output = (
        f"Election Results\n"
        f"------------------\n"
        f"Total Votes: {votes_cast}\n"
        f"------------------\n"
        f"{Can1}: {Can1_Count}\n"
        f"{Can2}: {Can2_Count}\n"
        f"{Can3}: {Can3_Count}\n"
        f"{Can4}: {Can4_Count}\n"
        f"{Can1}: {Can1_Percentage}%\n"
        f"{Can2}: {Can2_Percentage}%\n"
        f"{Can3}: {Can3_Percentage}%\n"
        f"{Can4}: {Can4_Percentage}%\n"
        f"------------------\n"
        f"Winner: {maximum} {Final_List[maximum]}%\n"
        f"------------------\n")

    with open(output_file, "w") as txt_file:
        txt_file.write(output)
