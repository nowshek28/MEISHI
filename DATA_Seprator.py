
def DATA_Seperator(data):
    #print(data)
    mobile = ["+","Mobile"]
    company = ["Com", "Corp", "Inc", "LLC"]
    card_data ={
        "NAME":"",
        "COMPANY":"",
        "COMAPANY GROUP":"",
        "ADDRESS":"",
        "PHONE":"",
        "EMAIL":"",
        "WEBSITE":"",
        "Description": ""
    }
    for item in data:
        if 'www' in item:
            card_data['WEBSITE'] = item
        elif '@' in item:
            card_data['EMAIL'] = item
            card_data['NAME'] = item[:item.index('@')]
        elif 'group' in item or 'Group' in item:
            card_data['COMAPANY GROUP'] = item
        elif 'japan' in item.lower():
            card_data['ADDRESS'] = item
        else:
            count = False
            for i in mobile:
                if i in item :
                    card_data['PHONE'] = card_data['PHONE']+ ', '+item
                    count = True
                
            for i in company:
                if i in item :
                    card_data['COMPANY'] = item
                    count = True
                
            
            if count == False:
                card_data["Description"] = card_data["Description"]+ ' '+item


    print(card_data)
    return card_data
            


if __name__ == "__main__":
    DATA = ['santec', 'SantecAocCorporation', 'Photonics Valley Ohkusa Campus', 'Abhishek Amea', '5823 Ohkusa-Nenjozaka', 'Factory Autonation Group', 'KomakiAichi485-0802,jAPAN', 'Mobile:+81-70-1438-567', 'Tel:+81-568-79-535', 'Fax:+81-58-79-349', 'www.santececom', 'E-mail:abhishekamea@santeccom']
    DATA_Seperator(DATA)