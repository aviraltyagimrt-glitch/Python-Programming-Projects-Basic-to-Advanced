def lifeline():
    for i in range (1):
        print(f"Sorry {a} your entered answer is wrong")
        print("Do you want to use an lifeline")
        d = input("Enter either Yes or No\n")
        if (d == "Yes" or d == "YES" or d == "yes"):
            print(f"Congrats {a} you successfully used your 1 lifeline")
            continue
        else:
            print(f"Thanks for playing {a}\nYou successfully exited the game")
            print("Developed by Aviral Tyagi")
            break

call = 0
max_limit = 3
life_line_used = False
money = 0
for i in range(1):
    print("Welcome to the Kaun Banega Crorepati Game")
    a = input("Please enter your name before playing\n")
    print(f"Great job {a} now , before entering the game follow these instructions")
    print("There will be 11 question at all")
    print("For Each question you have to choose answer from the 4 options mentioned below")
    print("You have 3 lifelines in total and after their usage no clue will be provided")
    print("The respected amount will be credited in your balance as per the correction rate")
    b = input("Are you Ready? (Y/N)\n")
    if(b == "Y" or b == "y"):
        print("Let's go\n")
        q1 = "When was First AI app Introduced ?"
        q2 = "Name the latest Chip NVIDIA has launched ?"
        q3 = "Name the latest party formed by the youth of India that demanded resignation of education     minister ?"
        q4 = "What does AI and AGI means ?"
        q5 = "Latest Claude Model that was just blocked by the government of US ?"
        q6 = "Who own's the AI Coding app named \"Codex\" ?"
        q7 = "Who is known as the father of Mathematcs ?"
        q8 = "Who is the most richest man alive on the earth ?"
        q9 = "Who owns the IDE VS Code ?"
        q10 = "Which famous Indian Celebrity host KBC ?"
        q11 = "Who recently became the CEO of Whatsapp ?"
        print(f"Ques 1. {q1}")
        print("1. 1966\n2. 2011\n3. 2012\n4. 2022")
        c = int(input("Enter your Answer\nPress either 1, 2, 3 or 4\n"))
        if (c == 1):
            print(f"Congrats {a} You Won ₹ 500\n")
            money = money + 500
            print(f"Total Balance ₹ {money}")
        elif(c == 2 or c == 3 or c == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
        
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
        else:
            print("Your entered value is not the one mentioned above\n try again")
            break
        
        print(f"Ques 2. {q2}")
        print("1. RTX Chip\n2. Silicon Chip\n3. Spark\n4. Gen Force Ultra")
        c2 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c2 == 3):
            print(f"Congrats {a} You won Cash Prize of ₹ 1000")
            money = money + 1000
            print(f"Total Balance ₹ {money}\n")
        elif ( c2 == 1 or c2 == 2 or c2 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1

                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break

        print(f"Ques 3. {q3}")
        print("1. Reservation Hatao Party (RHP)\n2. Cockroach Janta Party (CJP)\n3. Youth Innovation Party(YIP)\n4. Indian Party (IP)")
        c3 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c3 == 2):
            print(f"Congrats {a} You won Cash Prize of ₹ 2000")
            money = money + 2000
            print(f"Total Balance ₹ {money}\n")
        elif(c3 == 1 or c3 == 3 or c3 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1

                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")

        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 4. {q4}")
        print("1. AI means Artificial Intelligence and AGI means Augmented General Intelligence\n2. AI means General Artificial Intelligence and AGI means Artificial Generated Intelligence\n3. AI means Automated Intelligence and AGI means Automated General Intelligence\n4. None of the above")
        c4 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c4 == 1):
            print(f"Congrats {a} You won Cash Prize of ₹ 4000")
            money = money + 4000
            print(f"Total Balance ₹ {money}\n")
        elif(c4 == 2 or c4 == 3 or c4 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1

                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        
            
        print(f"Ques 5. {q5}")
        print("1. Gemini 3.6 Flash.\n2. Claude Fable 5\n3. Chat GPT 5.5\n4. Not mentioned here")
        c5 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c5 == 2):
            print(f"Congrats {a} You won Cash Prize of ₹ 8000")
            money = money + 8000
            print(f"Total Balance = ₹ {money}\n")
        elif(c5 == 1 or c5 == 3 or c5 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 6. {q6}")
        print("1. Google\n2. Open AI\n3. Anthropic\n4. Anysphere, Inc.")
        c6 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c6 == 2):
            print(f"Congrats {a} You won Cash Prize of ₹ 16000")
            money = money + 16000
            print(f"Total Balance = ₹ {money}\n")
        elif (c6 == 1 or c6 == 3 or c6 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 7. {q7}")
        print("1. Albert Einstein\n2. Srinivasa Ramanujan\n3. Aryabhata\n4. Archimedes")
        c7 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c7 == 4):
            print(f"Congrats {a} You won Cash Prize of ₹ 32000")
            money = money + 32000
            print(f"Total Balance = ₹ {money}\n")
        elif(c7 == 1 or c7 == 2 or c7 == 3):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 8. {q8}")
        print("1. Jeff Bezos\n2. Larry Page\n3. Elon Musk\n4. Michael Dell")
        c8 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c8 == 3):
            print(f"Congrats {a} You won Cash Prize of ₹ 64000")
            money = money + 64000
            print(f"Total Balance = ₹ {money}\n")
        elif(c8 == 1 or c8 == 2 or c8 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 9. {q9}")
        print("1. Microsoft\n2. Google\n3. Dell Technologies\n4. IBM")
        c9 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c9 == 1):
            print(f"Congrats {a} You won Cash Prize of ₹ 128000")
            money = money + 128000
            print(f"Total Balance = ₹ {money}\n")
        elif(c8 == 2 or c8 == 3 or c8 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 10. {q10}")
        print("1. Hrithik Roshan\n2. Salman Khan\n3. Amitabh Bacchan\n4. Akshay Kumar")
        c10 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c10 == 3):
            print(f"Congrats {a} You won Cash Prize of ₹ 256000")
            money = money + 256000
            print(f"Total Balance = ₹ {money}\n")
        elif(c10 == 1 or c10 == 2 or c10 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Ques 11. {q11}")
        print("1. Kunal Shah\n2. Anupam Mittal\n3. Ashneer Grover\n4. Sundar Pichai")
        c11 = int(input("Enter your Answer either 1, 2, 3 or 4\n"))
        if (c11 == 1):
            print(f"Congrats {a} You won Cash Prize of ₹ 512000")
            money = money + 512000
            print(f"Total Balance = ₹ {money}\n")
        elif(c11 == 2 or c11 == 3 or c11 == 4):
            if (call < max_limit):
                lifeline()
                call = call+1
                remaining = max_limit - call
                print(f"Lifelines remaining = {remaining}")
            else:
                print("Sorry your entered answer is wrong and you don't have more Lifelines")
                print(f"Your Total Balance Remaining = {money}")
                print("Thank you for playing the Game\ndeveloped by Aviral Tyagi")
                break
        else:
            print("Your entered value is not the one mentioned above\ntry again")
            break
        print(f"Thank you for successfully completing this game {a}")
        print(f"Total Amount you Won is ₹ {money}")
        print("The respected amount will be credited in your account in next 24 hours")
        print("You successfully exited the Game")
        print("Developed by Aviral Tyagi")



                
                
                
            


        
 