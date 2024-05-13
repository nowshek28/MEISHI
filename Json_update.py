import json
import sys

def read_para_file(file_path):
    data = []
    Json_data = {
        'Model_Name' : '',
        "Barcode_Model_Name": '',
        "Standard_Range": [
                [ 0, 0 ],
                [ 0, 0 ],
                [ 0, 0 ],
                [ 0, 0 ],
                [ 0, 0 ]
            ],
        "Rank": [
            "",
            "",
            "",
            "",
            ""
        ]
    }
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            data.append(line)


    
    key, value =data[1].split('=', 1)
  
    Json_data['Model_Name'] = value
    x = 0
    for i in range(4,9):
        try:
            key, value =data[i].split('=')
            value1, value2 = value.split('-')
            Json_data['Standard_Range'][x][0] = (value1)
            Json_data['Standard_Range'][x][1] = (value2)
            x += 1
        except:
            pass
    x = 0
    for i in range(10,15):
        try:
            key, value =data[i].split('=')
            Json_data['Rank'][x] = value
            x += 1
        except:
            pass
        
    return Json_data

def read_write_json(file_path, JData):
    
    avail = 0
    with open(file_path, 'r') as file:
        data = json.load(file)
    indentt = len(data['MODEL'])

    # Append the new person's data to the existing data
    #data.append(new_person)
    for i in (data['MODEL']):
        if JData['Model_Name'] == i['Model_Name']:
            avail += 1
                 
    if avail == 0: 

        data['MODEL'].append(JData)
        with open(file_path, 'w') as file:
                json.dump(data, file, indent=indentt) 
    else:
        print("Data Already Exist")  
    
    return avail
        
    #file_path = 'C:\\Users\\abhishek\\Desktop\\L-33193.para'
    file_path = sys.argv[1]
    parameters = read_para_file(file_path)
    json_path = 'E:\\MTF-DFP_Measure_updated\\MTF-DFP_Measure\\bin\\Debug\\net5.0-windows\\Setting\\Parameter_Init - Copy.json'
    read_write_json(json_path, parameters)
    #print(parameters)