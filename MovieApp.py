from Movie import Movie

listOfMovies = []
searchString = ""

file=open('movieList.txt')

lines=file.readlines()

for data in lines:
    data=data.replace("\n","")
    cols=data.split("|")
    name=cols[0]
    category=cols[1]
    description=cols[2]
    price=round(float(cols[3]),2)
    m=Movie(name,category,description,price)  
    listOfMovies.append(m)

file.close()

def PrintMovieDetails(Movie): 
    global index
    print("Name: "+listOfMovies[index].getName())
    print("Category: "+listOfMovies[index].getCategory())
    print("Description: "+listOfMovies[index].getDescription())
    print("Price: $"+str(listOfMovies[index].getPrice()))
    print("Price With GST: $"+str(listOfMovies[index].getPriceWithGST()))
    

def SearchBasedOnNameOrCategory(searchString,listOfMovies):  
    global searchList
    global usrInput
    searchList = []
    for index in range(len(listOfMovies)):
        if usrInput.lower() in listOfMovies[index].getName().lower() or usrInput.lower() in listOfMovies[index].getCategory().lower():
            searchList.append(listOfMovies[index])


def PrintSearchMovieDetails(Movie): 
    global index
    print("Name: "+searchList[index].getName())
    print("Category: "+searchList[index].getCategory())
    print("Description: "+searchList[index].getDescription())
    print("Price: $"+str(searchList[index].getPrice()))
    print("Price With GST: $"+str(searchList[index].getPriceWithGST()))


def menu1():
    print("\n\nDisplay all movies")
    global index
    index = 0
    usrInput = ""
    while usrInput != "M":
        try:
            print("\nMovie "+str(index+1)+" of "+str(len(listOfMovies)))
            print("==============================")
            # # use new function to display the movie details
            PrintMovieDetails(Movie)
            print("==============================")
            
            print("Enter N for Next movie")
            print("Enter P for Previous movie")
            usrInput = input("Enter M to return to Main Menu\n")

            # Logic for usrInput
            if usrInput == "N":
                index += 1
            if index >= len(listOfMovies):
                index = 0
            elif usrInput == "P":
                index -= 1
            if index < 0:
                index = len(listOfMovies)-1
               
        except IndexError as e:
            print(e," occurred")


def menu2():
    print("\n\nDisplay movie full names for selection")
    global index
    usrInput = ""
    while True:
        try:
            for index in range(len(listOfMovies)):
                print(str(index+1)+". "+listOfMovies[index].getName())
                
            print("Enter M to return to Main Menu")
                
            usrInput = input("Please enter your selection\n")

            if usrInput == "M":
                break
            
            index = int(usrInput)-1
            print("\nMovie "+usrInput+" of "+str(len(listOfMovies)))
            print("==============================")
            # # use new function to display the movie movie details
            PrintMovieDetails(Movie)
            print("==============================\n")
            
            innerMenu = ""

            innerMenu = input("Enter M to return to Previous Menu. Any key continue.\n")
            if innerMenu == "M":
                break

        except IndexError as e:
            print(e," occurred")


def menu3():
    print("\n\nSearch based on Name or Category substring")
    global index
    global usrInput
    usrInput = ""

    while True:
        usrInput = input("Please enter your search input\n")
            
        # use new function to display the movie details
 
        SearchBasedOnNameOrCategory(searchString,listOfMovies)

        if len(searchList) == 0:
            print("\n======= No results found =======")
        else:
            for index in range(len(searchList)):
                print("\nMovie "+str(index+1)+" of "+str(len(searchList)))
                # use new function to display the movie details
                print("==============================")
                PrintSearchMovieDetails(Movie)
                print("==============================")

        usrInput = "reset"
        while usrInput != "1" and usrInput != "2" :
            print("1. Search again")
            usrInput = input("2. Return to Main Menu\n")

        if usrInput == "2":
            break


#Menu Selection and Display starts here

menuSelection = ""

while True:
    print("Main Menu")
    print("----------")
    print("1. Display all movies")
    print("2. Display movie full names for selection")
    print("3. Search based on Name or Category substring")
    print("Q. Enter Q to quit")

    menuSelection = input("Please input your selection\n")
    if menuSelection == "Q":
        break
    print("You have selected "+menuSelection+".. ",end="")

    if menuSelection == "1":
        # create function for running menu selection 1 logic
        # include exception handling for index error
        menu1()
    
    elif menuSelection == "2":
        # create function for running menu selection 2 logic
        # include exception handling for index error
        menu2()

    elif menuSelection == "3":
        # create function for running menu selection 3 logic
        menu3()
