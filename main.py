status = True
while status:
    #list of are code

    call_collection = {"11": {'day': '11', 'called_country': 'USA', '1':9.50,'2':11.50,'3':13.50 },
                       "12": {'day': '12', 'called_country': 'Australia', '1': 8.75, '2': 10/75, '3': 11.25},
                       "13": {'day': '13', 'called_country': 'Saudi Arabia', '1': 6.75,'2':9.50,'3':9.75 },
                       "14": {'day': '14', 'called_country': 'Hongkong', '1': 5.25,'2':6.50,'3':8.50 },
                       "15": {'day': '15', 'called_country': ' Singapore', '1': 4.75,'2':5.50,'3':6.75 }}
    call_period = {'1' : "Weekday", "2":"Evening", "3": "Sunday"}
    access_code = input("Enter Access Code .....   ")

    number_of_minutes = float(input("Enter No. of Minutes .....   "))
    print(" ")
    print(access_code[3:10], "called up", call_collection[access_code[0:2]]['called_country'], " - ",call_period[access_code[2:3]])
    print("Total Charges ....... . .",call_collection[access_code[0:2]][access_code[2:3]] * number_of_minutes)
    promt = input("\nTry Again Y/N? ")

    if promt.upper() == "N":
        status = False

