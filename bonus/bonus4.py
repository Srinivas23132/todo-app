date=input("Enter the date : ")
rating=int(input("Enter the rating you give for today 1-10 : "))
info=input("Enter about what you did today and about any important stuff : ")
with open(f"../journal/{date}.txt","w",encoding="utf-8") as file:
    file.write(info)
    file.write("\n\n")
    file.write(f"Rating for {date} is {rating} {'★'*rating}")
    file.write("\n\n")
    file.write("                                                                ------------THE END------------")