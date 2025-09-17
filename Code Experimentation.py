# from ucimlrepo import fetch_ucirepo
import pandas as pd
import os
from tqdm.auto import tqdm
import numpy as np



# Location of diabetic_data.csv.
import_df_location = "<insert filepath of excel sheet file>"
# Locations for output files.
file_save_loaction = "<insert filepath where generated files should be saved>"

# File location provided check.
if (import_df_location == ""):
    raise ValueError("import_df_location cannot be empty.")
if (file_save_loaction == ""):
    raise ValueError("file_save_loaction cannot be empty.")

# Output text.
list_of_unique_and_nunique = ""
check_duplicates_in_first_two = ""
replacing_race_with_integers = ""
replacing_gender_with_integers = ""
replace_age_categories_with_integers = ""
removing_weight_column = ""
condensed_insurance_information = ""
replacing_medical_specialty_with_integers = ""
replacing_diagnoses_codes_with_integers = ""
replacing_medication_used_indication_with_integers = ""
replacing_max_glu_serum_with_integers = ""
replacing_A1Cresult_with_integers = ""
replacing_change_with_integers = ""
replacing_diabetesMed_with_integers = ""
replacing_readmitted_with_integers = ""

# Import dataset.
df_imported = pd.read_csv(os.path.join(file_save_loaction, 'diabetic_data.csv'))
column_names_list = df_imported.columns.tolist()
print(column_names_list)
print(len(column_names_list))
print(df_imported.values)
print("\n")

'''
List of elements:
['encounter_id', 'patient_nbr', 'race', 'gender', 'age', 'weight', 'admission_type_id',
 'discharge_disposition_id', 'admission_source_id', 'time_in_hospital', 'payer_code',
 'medical_specialty', 'num_lab_procedures', 'num_procedures', 'num_medications',
 'number_outpatient', 'number_emergency', 'number_inpatient', 'diag_1', 'diag_2', 'diag_3',
 'number_diagnoses', 'max_glu_serum', 'A1Cresult', 'metformin', 'repaglinide', 'nateglinide',
 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide',
 'examide', 'citoglipton', 'insulin', 'glyburide-metformin', 'glipizide-metformin',
 'glimepiride-pioglitazone', 'metformin-rosiglitazone', 'metformin-pioglitazone', 'change',
 'diabetesMed', 'readmitted']
'''



# Method that prints both a list of the unique elements and the number of unique elements from a provided column name.
# The user can also state when this print method was used.
def unique_element_and_count_string(column_name, before_or_after_or_empty):
    string_to_return = f"Unique Elements {before_or_after_or_empty}: {str(df_imported[column_name].unique())}\n"
    string_to_return += f"Unique Element Count {before_or_after_or_empty}: {str(df_imported[column_name].nunique())}\n"
    return string_to_return


# Save list and count of unique elements from each column.
list_of_unique_and_nunique += "List and count of unique elements from each column in dataframe.\n"
for element in column_names_list:
    list_of_unique_and_nunique += f"Column Name: {element}\n"
    list_of_unique_and_nunique += unique_element_and_count_string(element, "")
    list_of_unique_and_nunique += "\n"



# Checking for duplicates in encounter_id and patient_nbr.
first_two_column_names = column_names_list[:2]
list_of_groups = []
for element in first_two_column_names:
    current_duplicate_check = df_imported.groupby(element)
    list_of_groups.append(current_duplicate_check)
check_duplicates_in_first_two += "During earlier analysis, duplicate elements were found in patient_nbr.\n\n"



# Replace race text with integers.
replacing_race_with_integers += "Column Name: Race\n"
# Print replacement information.
replacing_race_with_integers += "Replacements:\n'?' --> 0\n'Caucasian' --> 1\n'AfricanAmerican' --> 2\n'Asian' --> 3\n'Hispanic' --> 4\n'Other' --> 5\n'Anything Else' --> -1\n"
# Print list of unique elements beforehand.
replacing_race_with_integers += unique_element_and_count_string("race", "before")
# Replacement function.
def replace_race_text(input_information):
    match input_information:
        case '?': # If '?' (not provided), return 0.
            return 0
        case 'Caucasian':
            return 1
        case 'AfricanAmerican':
            return 2
        case 'Asian':
            return 3
        case 'Hispanic':
            return 4
        case 'Other':
            return 5
        case _:
            return -1
# Perform replacement.
df_imported['race'] = df_imported['race'].apply(lambda x: replace_race_text(x))
# Print list of unique elements afterward to ensure replacement.
replacing_race_with_integers += unique_element_and_count_string("race", "after")
replacing_race_with_integers += "\n"



# Replace gender text with integers.
replacing_gender_with_integers += "Column Name: gender\n"
# Print replacement information.
replacing_gender_with_integers += "Replacements:\n'Unknown/Invalid' --> 0\n'Male' --> 1\n'Female' --> 2\n'Anything Else' --> -1\n"
# Print list of unique elements beforehand.
replacing_gender_with_integers += unique_element_and_count_string("gender", "before")
# Replacement function.
def replace_gender(input_information):
    match input_information:
        case 'Unknown/Invalid':
            return 0
        case 'Male':
            return 1
        case 'Female':
            return 2
        case _:
            return -1
# Perform replacement.
df_imported['gender'] = df_imported['gender'].apply(lambda x: replace_gender(x))
# Print list of unique elements afterward to ensure replacement.
replacing_gender_with_integers += unique_element_and_count_string("gender", "after")
replacing_gender_with_integers += "\n"



# Replace age text with integers.
replace_age_categories_with_integers += "Column Name: age\n"
# Print replacement information.
replace_age_categories_with_integers += "Replacements:\n'[0-10)' --> 0\n'[10-20)' --> 1\n'[20-30)' --> 2\n'[30-40)' --> 3\n'[40-50)' --> 4\n'[50-60)' --> 5\n'[60-70)' --> 6\n'[70-80)' --> 7\n'[80-90)' --> 8\n'[90-100)' --> 9\n'Anything Else' --> -1\n"
# Print list of unique elements beforehand.
replace_age_categories_with_integers += unique_element_and_count_string("age", "before")
# Replacement function.
def replace_age_ranges(input_information):
    match input_information:
        case '[0-10)':
            return 0
        case '[10-20)':
            return 1
        case '[20-30)':
            return 2
        case '[30-40)':
            return 3
        case '[40-50)':
            return 4
        case '[50-60)':
            return 5
        case '[60-70)':
            return 6
        case '[70-80)':
            return 7
        case '[80-90)':
            return 8
        case '[90-100)':
            return 9
        case _:
            return -1
# Perform replacement.
df_imported['age'] = df_imported['age'].apply(lambda x: replace_age_ranges(x))
# Print list of unique elements afterward to ensure replacement.
replace_age_categories_with_integers += unique_element_and_count_string("age", "after")
replace_age_categories_with_integers += "\n"



# Drop 'weight' column due to too many missing elements (97% missing).
df_imported.drop('weight', axis=1, inplace=True)
# Print drop reason.
removing_weight_column += "Dropped 'weight' column due to too many missing elements (97% missing).\n\n"



# Condense insurance information.
condensed_insurance_information += "Column Name: payer_code\n"
# Print condensing information.
condensed_insurance_information += "Condensing:\n'?' --> 0\n'SP' --> 1\n'Anything Else' --> 2\n"
# Print reason for condensing.
condensed_insurance_information += "Reason for condensing:\nPatients who don't use insurance are less likely to return for additional treatment, which puts them at increased risk for further injury.\n"
# Print list of unique elements beforehand.
condensed_insurance_information += unique_element_and_count_string("payer_code", "before")
# Filtering function.
def filter_payer_code(input_information):
    # Insurance information not provided.
    if (input_information == '?'):
        return 0
    # Patient did not use insurance. I don't know if 'SP' stands for 'self-pay' or not.
    elif (input_information == 'SP'):
        return 1
    # Patient used insurance.
    else:
        return 2
# Perform the filtering operation.
df_imported['payer_code'] = df_imported['payer_code'].apply(lambda x: filter_payer_code(x))
# Print list of unique elements afterward to ensure filtering.
condensed_insurance_information += unique_element_and_count_string("payer_code", "after")
condensed_insurance_information += "\n"



# Replace the elements in a given column with integers.
def replace_elements_with_ints(column_name):
    return_question_mark_associated_element = 0

    # Get the list of unique column elements from the column in question.
    unique_column_elements = df_imported[column_name].unique().tolist()

    # Check if a '?' element exists, and move it to the front of the list of unique column elements if it does.
    try:
        question_mark_location = unique_column_elements.index('?')
        unique_column_elements.pop(question_mark_location)
        unique_column_elements.insert(0, '?')

        # Additional information needs to be printed
        if (question_mark_location == 0):
            return_question_mark_associated_element = 1
        if (question_mark_location > 0):
            return_question_mark_associated_element = 2
    except:
        pass

    # Convert back to numpy array for printing purposes.
    unique_column_elements = np.array(unique_column_elements)

    # Get the number of unique column elements from the column in question, and then generate a list of elements from 0 up to one less than the number of unique elements.
    unique_column_element_count = df_imported[column_name].nunique()
    list_of_numbers = list(range(0, unique_column_element_count))

    # Pair each number to a unique column element and perform the replacement.
    unique_column_elements_numbers_pairing = {key: element for key, element in zip(unique_column_elements, list_of_numbers)}
    df_imported[column_name] = df_imported[column_name].apply(lambda x: unique_column_elements_numbers_pairing[x])

    # If a '?' element exists, the temporary reordering of unique elements was done, so additional information needs to be printed.
    if (return_question_mark_associated_element == 1):
        return f"The element associated with '?' is '{unique_column_elements_numbers_pairing['?']}'\n"
    elif (return_question_mark_associated_element == 2):
        return (
            f"Temporary reordering of unique elements: {unique_column_elements}\n" +
            f"The element associated with '?' is '{unique_column_elements_numbers_pairing['?']}'\n"
            )
    else:
        return ""
# Replacement information.
replace_elements_with_ints_string = "Replacement:\nEverything --> After moving '?' (if it exists) to the front of the unique elements list, each element is assigned a unique number, starting from zero up to one less than the number of unique elements.\n"



# Replacing medical specialty strings with integers.
# Despite 53% of element missing, the medical speciality examining a patient is very important.
#  Example: Emergency/Trauma is much more important than Dentistry.
def consensing_medical_specialties(input_information):
    match input_information:
        # Primary Care
        case x if (x == 'Family/GeneralPractice') or (x == 'InternalMedicine') or (x == 'Pediatrics') or (x == 'Hospitalist') or (x == 'Osteopath') or (x == 'Resident') or (x == 'PhysicianNotFound'):
            return 'Primary Care'
        # Cardiovascular System - Non-surgery.
        case x if (x == 'Cardiology') or (x == 'Cardiology-Pediatric'):
            return 'Cardiovascular System - Non-surgery'
        # Neurology - Non-surgery.
        case x if (x == 'Neurology') or (x == 'Neurophysiology') or (x == 'Pediatrics-Neurology'):
            return 'Neurology - Non-surgery'
        # Psychiatry
        case x if (x == 'Psychiatry') or (x == 'Psychiatry-Child/Adolescent') or (x == 'Psychiatry-Addictive') or (x == 'Psychology'):
            return 'Psychiatry'
        case _:
            return input_information
# Condense some of the related medical specialities into groups.
replacing_medical_specialty_with_integers += "Column Name: medical_specialty\n"
# Perform consensing.
df_imported['medical_specialty'] = df_imported['medical_specialty'].apply(lambda x: consensing_medical_specialties(x))
# Print list and number of unique elements after condensing.
replacing_medical_specialty_with_integers += unique_element_and_count_string('medical_specialty', "After Condensing")
# Print notes.
replacing_medical_specialty_with_integers += ("Notes:\nDespite 53% of elements missing, the medical speciality examining a patient is very important.\n" +
                                              "Example:\nEmergency/Trauma is much more important than Dentistry.\n" + 
                                              "In addition, 'DCPTEAM' possibly stands for 'Dynamic Care Planning Team'.\n")
# Print replacement message.
replacing_medical_specialty_with_integers += replace_elements_with_ints_string
# Print list and number of unique elements beforehand.
replacing_medical_specialty_with_integers += unique_element_and_count_string("medical_specialty", "before")
# Perform replacement.
replacing_medical_specialty_with_integers += replace_elements_with_ints('medical_specialty')
# Print list and number of unique elements afterward to ensure replacement.
replacing_medical_specialty_with_integers += unique_element_and_count_string("medical_specialty", "after")
replacing_medical_specialty_with_integers += "\n"



# Replace the codes for diagnoses 1, 2, and 3 with integers.
for i in range(18, 21):
    current_column_name = column_names_list[i]
    # Print column name.
    replacing_diagnoses_codes_with_integers += f"Column Name: {current_column_name}\n"
    # Print reason for replacement.
    replacing_diagnoses_codes_with_integers += replace_elements_with_ints_string
    # Print list and number of unique elements beforehand.
    replacing_diagnoses_codes_with_integers += unique_element_and_count_string(current_column_name, "before")
    # Perform replacement.
    replacing_diagnoses_codes_with_integers += replace_elements_with_ints(current_column_name)
    # Print list and number of unique elements afterward to ensure replacement.
    replacing_diagnoses_codes_with_integers += unique_element_and_count_string(current_column_name, "after")
    replacing_diagnoses_codes_with_integers += "\n"



# Replace no, steady, up, and down with corresponding integers.
def replace_no_steady_up_down(input_information):
    match input_information.lower():
        case 'no':
            return 0
        case 'steady':
            return 1
        case 'up':
            return 2
        case 'down':
            return 3
        case _:
            return -1
# Print medication note.
replacing_medication_used_indication_with_integers += "Medication Note:\nWhile some medications were not administered, medications are still important and, as a result, they weren't dropped.\n\n"
for i in range(24, 47):
    current_column_name = column_names_list[i]
    # Print column name.
    replacing_medication_used_indication_with_integers += f"Column Name: {current_column_name}\n"
    # Print reason for replacement.
    replacing_medication_used_indication_with_integers += "Replacements:\n'no' --> 0\n'steady' --> 1\n'up' --> 2\n'down' --> 3\n'Anything Else' --> -1\n"
    # Print list and number of unique elements beforehand.
    replacing_medication_used_indication_with_integers += unique_element_and_count_string(current_column_name, "before")
    # Perform replacement.
    df_imported[current_column_name] = df_imported[current_column_name].apply(lambda x: replace_no_steady_up_down(x))
    # Print list and number of unique elements afterward to ensure replacement.
    replacing_medication_used_indication_with_integers += unique_element_and_count_string(current_column_name, "after")
    replacing_medication_used_indication_with_integers += "\n"



# Replace elements in 'max_glu_serum' column.
replacing_max_glu_serum_with_integers += "Column Name: max_glu_serum\n"
# Print replacement information.
replacing_max_glu_serum_with_integers += "Replacements:\n'nan' --> 0\n'norm' --> 1\n'>200' --> 2\n'>300' --> 3\n'Anything Else' --> -1\n"
# Print note.
replacing_max_glu_serum_with_integers += "Note:\n'None' in the excel sheet might be 'nan' in Pandas. That explains the jump from 3 to 4 in the number of unique elements.\n"
# Print list and number of unique elements beforehand.
replacing_max_glu_serum_with_integers += unique_element_and_count_string("max_glu_serum", "before")
# Replace elements with corresponding integers.
def replace_max_glu_serum_elements(input_information):
    match str(input_information).lower():
        case 'nan':
            return 0
        case 'norm':
            return 1
        case '>200':
            return 2
        case '>300':
            return 3
        case _:
            return -1
# Perform replacement.
df_imported['max_glu_serum'] = df_imported['max_glu_serum'].apply(lambda x: replace_max_glu_serum_elements(x))
# Print list and number of unique elements afterward to ensure replacement.
replacing_max_glu_serum_with_integers += unique_element_and_count_string("max_glu_serum", "after")
replacing_max_glu_serum_with_integers += "\n"



# Replace elements in 'A1Cresult' column.
replacing_A1Cresult_with_integers += "Column Name: A1Cresult\n"
# Perform replacement information.
replacing_A1Cresult_with_integers += "Replacements:\n'nan' --> 0\n'norm' --> 1\n'>7' --> 2\n'>8' --> 3\n'Anything Else' --> -1\n"
# Print note.
replacing_A1Cresult_with_integers += "Note:\n'None' in the excel sheet might be 'nan' in Pandas. That explains the jump from 3 to 4 in the number of unique elements.\n"
# Print list and number of unique elements beforehand.
replacing_A1Cresult_with_integers += unique_element_and_count_string("A1Cresult", "before")
# Replace elements with corresponding integers.
def replace_A1Cresult_elements(input_information):
    match str(input_information).lower():
        case 'nan':
            return 0
        case 'norm':
            return 1
        case '>7':
            return 2
        case '>8':
            return 3
        case _:
            return -1
# Perform replacement.
df_imported['A1Cresult'] = df_imported['A1Cresult'].apply(lambda x: replace_A1Cresult_elements(x))
# Print list and number of unique elements afterward to ensure replacement.
replacing_A1Cresult_with_integers += unique_element_and_count_string("A1Cresult", "after")
replacing_A1Cresult_with_integers += "\n"



# Replace elements in 'change' column.
replacing_change_with_integers += "Column Name: change\n"
# Print replacement information.
replacing_change_with_integers += "Replacements:\n'no' --> 0\n'ch' --> 1\n'Anything Else' --> -1\n"
# Print list and number of unique elements beforehand.
replacing_change_with_integers += unique_element_and_count_string("change", "before")
# Replace elements with corresponding integers.
def replace_change_elements(input_information):
    match str(input_information).lower():
        case 'no':
            return 0
        case 'ch':
            return 1
        case _:
            return -1
# Perform replacement.
df_imported['change'] = df_imported['change'].apply(lambda x: replace_change_elements(x))
# Print list and number of unique elements afterward to ensure replacement.
replacing_change_with_integers += unique_element_and_count_string("change", "after")
replacing_change_with_integers += "\n"



# Replace elements in 'diabetesMed' column.
replacing_diabetesMed_with_integers += "Column Name: diabetesMed\n"
# Print replacement information.
replacing_diabetesMed_with_integers += "Replacements:\n'no' --> 0\n'yes' --> 1\n'Anything Else' --> -1\n"
# Print list and number of unique elements beforehand.
replacing_diabetesMed_with_integers += unique_element_and_count_string("diabetesMed", "before")
# Replace elements with corresponding integers.
def replace_diabetesMed_elements(input_information):
    match str(input_information).lower():
        case 'no':
            return 0
        case 'yes':
            return 1
        case _:
            return -1
# Perform replacement.
df_imported['diabetesMed'] = df_imported['diabetesMed'].apply(lambda x: replace_diabetesMed_elements(x))
# Print list and number of unique elements afterward to ensure replacement.
replacing_diabetesMed_with_integers += unique_element_and_count_string("diabetesMed", "after")
replacing_diabetesMed_with_integers += "\n"



# Replace elements in 'readmitted' column.
replacing_readmitted_with_integers += "Column Name: readmitted\n"
# Print replacement information.
replacing_readmitted_with_integers += "Replacements:\n'no' --> 0\n'<30' --> 1\n'>30' --> 2\n'Anything Else' --> -1\n"
# Print list and number of unique elements beforehand.
replacing_readmitted_with_integers += unique_element_and_count_string("readmitted", "before")
# Replace elements with corresponding integers.
def replace_readmitted_elements(input_information):
    match str(input_information).lower():
        case 'no':
            return 0
        case '<30':
            return 1
        case '>30':
            return 2
        case _:
            return -1
# Perform replacement.
df_imported['readmitted'] = df_imported['readmitted'].apply(lambda x: replace_readmitted_elements(x))
# Print list and number of unique elements afterward to ensure replacement.
replacing_readmitted_with_integers += unique_element_and_count_string("readmitted", "after")
replacing_readmitted_with_integers += "\n"



# Create final output string.
print("Outputting information to text files.")
final_output_string_1 = (
    "Below, please find a list of the unique elements in each column along with how many unique elements there are.\n\n\n"
    f"{list_of_unique_and_nunique}\n\n"
)
final_output_string_2 = (
    "Introductory Info:\n"
    "This file: Information on the modifications done to the diabetic_data.csv file and why they were done.\n"
    "unique_information.txt: A list of unique elements in each column along with how many unique elements there are.\n"
    "output.csv: A version of diabetic_data.csv modified with the edits described in this file.\n"
    "output_grouped.csv: A version of output.csv where everything has been grouped together based on patient_nbr.\n"
    "Percentages for the amount of missing elements for some of the columns can be found here: https://onlinelibrary.wiley.com/doi/10.1155/2014/781670\n\n\n\n\n"
    "Modifications to diabetic_data.csv:\n\n\n"
    f"{check_duplicates_in_first_two}\n\n"
    f"{replacing_race_with_integers}\n\n"
    f"{replacing_gender_with_integers}\n\n"
    f"{replace_age_categories_with_integers}\n\n"
    f"{removing_weight_column}\n\n"
    f"{condensed_insurance_information}\n\n"
    f"{replacing_medical_specialty_with_integers}\n\n"
    f"{replacing_diagnoses_codes_with_integers}\n\n"
    f"{replacing_medication_used_indication_with_integers}\n\n"
    f"{replacing_max_glu_serum_with_integers}\n\n"
    f"{replacing_A1Cresult_with_integers}\n\n"
    f"{replacing_change_with_integers}\n\n"
    f"{replacing_diabetesMed_with_integers}\n\n"
    f"{replacing_readmitted_with_integers}"
)

# Save unique element and count information to text file.
with open("unique_information.txt", 'w') as file:
    file.write(final_output_string_1)
# Save explanation information to text file.
with open("explanation_information.txt", 'w') as file:
    file.write(final_output_string_2)
print("Information outputted to text file.")

# Create modified csv file from resulting dataframe.
print("Outputting modified csv file.")
df_imported.to_csv(os.path.join(file_save_loaction, 'output.csv'), index=False)
print("Modified csv file outputted.")

# Group resulting dataframe by the 'patient_nbr' column.
print("Starting Grouping")
tqdm.pandas()
# https://stackoverflow.com/questions/60963409/creating-a-dictionary-of-dictionaries-from-groupby
df_imported_grouped = df_imported.groupby('patient_nbr')
group_of_groups = df_imported_grouped.progress_apply(lambda x: x.set_index('encounter_id').to_dict())
print("Grouping Done")

# Create grouped csv file from the grouped dataframe.
print("Outputting grouped version of modified csv file.")
group_of_groups.to_csv(os.path.join(file_save_loaction, 'output_grouped.csv'), index=False)
print("Grouped version of modified csv file outputted.")