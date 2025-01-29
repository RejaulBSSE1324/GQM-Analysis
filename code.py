from scipy.stats import chi2_contingency



# Function to prepare data for Chi-Square test

def chi_square_test(data, column_name, expected_frequencies=None):

    # Exclude NaN values and count occurrences

    observed_frequencies = data[column_name].value_counts()

    

    # If expected frequencies are not provided, assume equal distribution

    if expected_frequencies is None:

        total_responses = observed_frequencies.sum()

        num_categories = len(observed_frequencies)

        expected_frequencies = [total_responses / num_categories] * num_categories



    # Convert observed and expected frequencies to arrays for Chi-Square test

    observed = observed_frequencies.values

    expected = expected_frequencies[:len(observed)]



    # Perform Chi-Square test

    chi2, p, dof, _ = chi2_contingency([observed, expected])

    return chi2, p, dof



# Chi-Square tests for each subgoal

chi_square_results = []



# Section A: Responsiveness of Emergency Services

questions_section_a = [

    "1. How long did you wait from arriving at the emergency room to being checked in?",

    "2. Do you feel your case was attended to within a reasonable time?",

    "4. How satisfied are you with the speed of emergency service response?"

]

for question in questions_section_a:

    chi2, p, dof = chi_square_test(data, question)

    chi_square_results.append((question, chi2, p, dof))



# Section B: Availability and Functionality of Resources

questions_section_b = [

    "5. Were all the necessary medical equipment and resources available for your care?",

    "6.How would you rate the availability of staff to manage the patient volume during your visit?",

    "7. Did you experience any equipment malfunctions or unavailability during your care?"

]

for question in questions_section_b:

    chi2, p, dof = chi_square_test(data, question)

    chi_square_results.append((question, chi2, p, dof))



# Section C: Patient Outcomes

questions_section_c = [

    "8. How effective was the care in addressing your condition?",

    "9. Overall, how would you rate your satisfaction with the care provided?",

    "10. Would you recommend this emergency department to others?"

]

for question in questions_section_c:

    chi2, p, dof = chi_square_test(data, question)

    chi_square_results.append((question, chi2, p, dof))



# Section D: Preparedness for High Patient Influx

questions_section_d = [

    "11. Did you feel the quality of care was compromised during busy times or high patient volume?",

    "12. How confident are you in the emergency department’s preparedness for crises like pandemics or mass casualty events?"

]

for question in questions_section_d:

    chi2, p, dof = chi_square_test(data, question)

    chi_square_results.append((question, chi2, p, dof))



# Section E: Areas for Improvement

questions_section_e = [

    "13. What challenges did you face during your visit? (Select all that apply)",

    "14. What would most improve emergency services? (Select up to two)"

]

for question in questions_section_e:

    chi2, p, dof = chi_square_test(data, question)

    chi_square_results.append((question, chi2, p, dof))



# Creating a summary table for the Chi-Square test results

chi_square_results_df = pd.DataFrame(

    chi_square_results,

    columns=["Question", "Chi-Square Value", "p-Value", "Degrees of Freedom"]

)



tools.display_dataframe_to_user(name="Chi-Square Test Results for Subgoals", dataframe=chi_square_results_df)
