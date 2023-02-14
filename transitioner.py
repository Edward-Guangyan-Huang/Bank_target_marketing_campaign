def Transitioner(input_list):
    predict_list = [0] * 53
    for i in range(0,5):
        predict_list[i] = float(input_list[i])
    
    if input_list[5] == 'blue-collar':
        predict_list[5] = 1
    elif input_list[5] == 'entrepreneur':
        predict_list[6] = 1
    elif input_list[5] == 'housemaid':
        predict_list[7] = 1
    elif input_list[5] == 'management':
        predict_list[8] = 1
    elif input_list[5] == 'retired':
        predict_list[9] = 1
    elif input_list[5] == 'self-employed':
        predict_list[10] = 1
    elif input_list[5] == 'services':
        predict_list[11] = 1
    elif input_list[5] == 'student':
        predict_list[12] = 1
    elif input_list[5] == 'technician':
        predict_list[13] = 1
    elif input_list[5] == 'unemployed':
        predict_list[14] = 1
    elif input_list[5] == 'unknown':
        predict_list[15] = 1

    if input_list[6] == 'married':
        predict_list[16] = 1
    elif input_list[6] == 'single':
        predict_list[17] = 1
    elif input_list[6] == 'unknown':
        predict_list[18] = 1

    if input_list[7] == 'basic six year':
        predict_list[19] = 1
    elif input_list[7] == 'basic nine year':
        predict_list[20] = 1
    elif input_list[7] == 'high school':
        predict_list[21] = 1
    elif input_list[7] == 'illiterate':
        predict_list[22] = 1
    elif input_list[7] == 'professional course':
        predict_list[23] = 1
    elif input_list[7] == 'university degree':
        predict_list[24] = 1
    elif input_list[7] == 'unknown':
        predict_list[25] = 1

    if input_list[8] == 'unknown':
        predict_list[26] = 1
    elif input_list[8] == 'yes':
        predict_list[27] = 1

    if input_list[9] == 'unknown':
        predict_list[28] = 1
    elif input_list[9] == 'yes':
        predict_list[29] = 1

    if input_list[10] == 'unknown':
        predict_list[30] = 1
    elif input_list[10] == 'yes':
        predict_list[31] = 1

    if input_list[11] == 'telephone':
        predict_list[32] = 1

    if input_list[12] == 'aug':
        predict_list[33] = 1
    elif input_list[12] == 'dec':
        predict_list[34] = 1
    elif input_list[12] == 'jul':
        predict_list[35] = 1
    elif input_list[12] == 'jun':
        predict_list[36] = 1
    elif input_list[12] == 'mar':
        predict_list[37] = 1
    elif input_list[12] == 'may':
        predict_list[38] = 1
    elif input_list[12] == 'nov':
        predict_list[39] = 1
    elif input_list[12] == 'oct':
        predict_list[40] = 1
    elif input_list[12] == 'sep':
        predict_list[41] = 1

    if input_list[13] == 'mon':
        predict_list[42] = 1
    elif input_list[13] == 'thu':
        predict_list[43] = 1
    elif input_list[13] == 'tue':
        predict_list[44] = 1
    elif input_list[13] == 'wed':
        predict_list[45] = 1

    if input_list[14] == 'yes':
        predict_list[46] = 1

    if input_list[15] == 'No outcome':
        predict_list[47] = 1
    elif input_list[15] == 'Success':
        predict_list[48] = 1
        
    age_preprocessed = int(input_list[16])
    campaign_preprocessed = int(input_list[17])
    previous_preprocessed = int(input_list[18])
    pdays_preprocessed = int(input_list[19])
    
    age =(age_preprocessed **(-0.19444047844673226)-1)/(-0.19444047844673226)
    campaign =(campaign_preprocessed**(-0.6627357510367072)-1)/(-0.6627357510367072)
    previous =(previous_preprocessed**(-9.181171975234234)-1)/(-9.181171975234234)
    pdays=(pdays_preprocessed**(-14.974637160292842)-1)/(-14.974637160292842)
    
    predict_list[49] = age
    predict_list[50] = campaign
    predict_list[51] = previous
    predict_list[52] = pdays


    return predict_list
