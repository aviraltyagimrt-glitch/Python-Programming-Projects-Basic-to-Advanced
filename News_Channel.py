import requests
import json
n = int(input("Press 1 if you want to read the news\nPress 0 if you want to exit\n"))
while(True):
    if(n == 1):
        while(True):
            print("Press 1 to read Political News\nPress 2 to read Financial News\nPress 3 to read Sports News\nPress 4 to read National News\nPress 5 to read Top Headlines\nPress 0 to exit\n")
            choice = int(input("Press the number according to your choice\n"))
            if (choice == 1):
                # url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                url = "https://newsapi.org/v2/everything?q=politics&from=2026-08-20&sortby=publisheadAt&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                response = requests.get(url)
                news = json.loads(response.text)
                print("\n")
                for i in news["articles"]:
                    print("The Title : - ")
                    print(i["title"])
                    print("The Description : - ")
                    print(i["description"])
                    print("------------------------------------------------------------------------------------")
                    print("")
            elif (choice == 2):
                # url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                url = "https://newsapi.org/v2/everything?q=financial&from=2026-08-20&sortby=publisheadAt&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                response = requests.get(url)
                news = json.loads(response.text)
                print("\n")
                for i in news["articles"]:
                    print("The Title : - ")
                    print(i["title"])
                    print("The Description : - ")
                    print(i["description"])
                    print("------------------------------------------------------------------------------------")
                    print("")
            elif (choice == 3):
                # url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                url = "https://newsapi.org/v2/everything?q=Sports&from=2026-08-20&sortby=publisheadAt&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                response = requests.get(url)
                news = json.loads(response.text)
                print("\n")
                for i in news["articles"]:
                    print("The Title : - ")
                    print(i["title"])
                    print("The Description : - ")
                    print(i["description"])
                    print("------------------------------------------------------------------------------------")
                    print("")
            elif (choice == 4):
                # url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                url = "https://newsapi.org/v2/everything?q=national&from=2026-08-20&sortby=publisheadAt&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                response = requests.get(url)
                news = json.loads(response.text)
                print("\n")
                for i in news["articles"]:
                    print("The Title : - ")
                    print(i["title"])
                    print("The Description : - ")
                    print(i["description"])
                    print("------------------------------------------------------------------------------------")
                    print("")
            elif (choice == 5):
                # url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                url = "https://newsapi.org/v2/everything?q=headlines&from=2026-08-20&sortby=publisheadAt&apiKey=cb58e8ff59a54876be97f7697a6b2d3a"
                response = requests.get(url)
                news = json.loads(response.text)
                print("\n")
                for i in news["articles"]:
                    print("The Title : - ")
                    print(i["title"])
                    print("The Description : - ")
                    print(i["description"])
                    print("------------------------------------------------------------------------------------")
                    print("")
            elif (choice == 0):
                print("Thank you for reading the news")
                print("Program Developed by Aviral Tyagi")
                break
            else:
                print("Kindly Press a number from the choices mentioned above")
                continue
        break
    elif(n == 0):
        print("Thank You for Reading the News")
        print("Program Developed by Aviral Tyagi")
        break
    else:
        print("Kindly choose the number from the choices mentioned above")
        print("Thank You for Reading the News")
        print("Program Developed by Aviral Tyagi")
        break