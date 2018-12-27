question_list = ["1--Who is the current PM(prime minister) of India?","2--Which is the largest river in India?",
                "3--What is the capital of India?","4--Which is the largest animal on land?",
                "5--Which is the largest vegetables?","6--What is capital of Bihar?",
                "7--During which festival does Santa come to visit?","8--What is the Capital of Telengana",
                "9--Who was the first Prime Minister of India?","10--What colour symbolises peace?",
                "11--In which direction does the sun rise?","12-- How many players are there in an ice hockey team?",
                "13--Who was the first president of India","14-- Which layer of planet Earth is made up of tectonic plates?",
                "15--Which first electrical item did Thomas Edison invent?"]

first_option  = ["1.Rajiv Gandhi","1.Ganga","1.Bhopal","1.Giraffe","1.Yam","1.Jaipur","1.Christmas",
                "1.Banglore","1.Rajiv Gandhi","1.Green","1.West","1. 7","1.Ram Nath Govind","1.Inner Core","1.Lightbulb"]

second_option = ["2.Narendra Modi","2.Yamuna","2.Chandigarh","2.Zebra","2.Sweet Potato","2.Patna",
                "2.Diwali","2.Hyderabad","2.Indra Gandhi","2.Orange","2.North","2. 5","2.Rajendra Prasad","2.Outer Core","2.Refrigerators"]

third_option  = ["3.Manmohan Singh","3.Brahmaputra","3.Jaipur","3.Elephant","3.Watermelon","3.Lucknow",
                "3.Dushera","3.Thiruvananthapuram","3.Lal Bahadur Shatri","3.White","3.East","3. 8","3.K.R Narayan","3.Mantle","3.Window fan"]

fourth_option = ["4.Chandra Shekar","4.Godavari","4.Delhi","4.Bear","4.Cabbage","4.Kolkata","4.Holi",
                "4.Chennai","4.Jawaharlal Nehru","4.Blue","South","4. 6","4.A.P.J Abdul Kalam","4.Crust","4.Computer"]

all_options = [first_option,second_option,third_option,fourth_option]

ans_keys = [2,1,4,3,1,2,1,2,4,3,3,4,2,4,1]

rupees =  [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

index = 0
correct_answers = 0
money = 0
while index < len(question_list):
    question_list_length = len(question_list[index])
    print question_list[index], " -",question_list_length
    print first_option[index]
    print second_option[index]
    print third_option[index]
    print fourth_option[index]

    user_ans = int(raw_input("Enter your ans (you have to choose one option 1,2,3 or 4 ) >"))

    if index == 4:
        print ""
        print "Congrates! Aapka padaav pura ho gya hai"
    if index == 9:
        print ""
        print "Congrates! Aapka doosra padav pura ho gya hai"
    if index == 14:
        print ""
        print "Congrates! Aap ek crore rupye jeet gaye hai"
    if user_ans == ans_keys[index]:
        print ""
        print "Congrates! apka answer sahi hai"
        print "Aapke abhi tak sahi answere ke ",rupees[index]," rupees ho gya hai"
        correct_answers = correct_answers + 1
    else:
        print ""
        print "Sadly apka answer galat hai"
        break
    print ''
    index = index + 1
print "Aapne ",correct_answers , "sahi javab diya hai"