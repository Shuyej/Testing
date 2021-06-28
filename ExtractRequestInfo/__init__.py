def getinforequests(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser') #allows Python to interact with information similar to that of which is possible in a web browser
   #print("Printing HTML file content")
    print(soup.contents)
    #print("Print the status code")
    print(page.status_code) #print status code
    #print("printing the title of the HTML document")
    print(print(soup.title.text ))

    results = soup.find(id='main-content')
    print("\n")
    print("Printing id= Main Content, information")
    print(results) #prints the element info of the first element of main-content

    Specificinfo = soup.find("div", {"class": "ssrcss-18snukc-RichTextContainer e5tfeyi1"}).find("p")
    print("\n")
    print("Printing div, class = ssrcss-18snukc-RichTextContainer e5tfeyi1, paragraph,  information")
    print(Specificinfo) #prints information of a given task and that is only text found within p tag of div class
    data_str = ""
    for item in soup.find_all("div", class_="ssrcss-18snukc-RichTextContainer e5tfeyi1"):
        data_str = data_str + item.get_text()
    print("How many things define soup")
    len(soup)
    print("The previous output of how many things define soup, is based of how many variables were used inside beautiful soup paranthesis")

    print("Next line of code will not produce text of the div class, except HTML element information of ONLY the first element")
    print(soup.find("div",class_="ssrcss-18snukc-RichTextContainer e5tfeyi1"))
    print("prints all of the HTML element information within div class: ssrcss-18snukc-RichTextContainer e5tfeyi1 ")
    print(soup.find_all("div",class_="ssrcss-18snukc-RichTextContainer e5tfeyi1"))
    print("prints first text information of the first element of div class: ssrcss-18snukc-RichTextContainer e5tfeyi1")
    print(soup.find("div",class_="ssrcss-18snukc-RichTextContainer e5tfeyi1").get_text())
    print("prints text information of all elements of div class: ssrcss-18snukc-RichTextContainer e5tfeyi1 ")
    print(data_str)
    print("print information inside nav element")
    print(soup.find_all('div', class_='ssrcss-1ocoo3l-Wrap e42f8511'))
     #find text of the document #better used to find tag information --> by tag we mean div, {class: ""}
    print("\n")
    print("find text of html document")
    print(soup.get_text());
    print("Find content related to the header document")
    print(soup.find(id="header-content").get_text())
    print("We will look to find a list within the class of element a, class is ssrcss-jujd5h-PromoLink e1f5wbog2")
    titles = soup.find_all("a", class_="ssrcss-jujd5h-PromoLink e1f5wbog2")
    for title in titles:
        print(title.string)
    print("Now, we will look to find a list within the class of element a, class is ssrcss-jujd5h-PromoLink e1f5wbog2")
    print("The difference between this line of code and the last line of code is the fact that data is stored in a vectore, titles1 from the elements of the class of a, class name mentioned in the last line")
    bs_titles = soup.find_all("a", class_="ssrcss-jujd5h-PromoLink e1f5wbog2")
    titles1 = []
    for title in bs_titles:
        titles1.append(title.string)


def getAllURLinfofromrequests(URL):
    page = requests.get(URL).text #Specify certain text we want #redefined in order for doc variable to be processed
    doc = html.fromstring(page) #provides an object of html type
    link = doc.cssselect("a")[0] #find lxml elements similar to HTML type #finds elements related to the first 'a' #0 is needed to avoid errors
    print("\n")
    print("Printing information related to the first content of 'a' element type of the URL")
    print(link.text_content()) #provides the content of the content of the URL attribute a.
    print("More information...")
    #sleep(3) #pauses computer for 3 seconds before next line executed
    print("\n")
    print("Printing the URL reference to the information on the first element 'a': ")
    print(link.attrib['href']) #displays url references for our text_content pribted for link
    page = requests.get("https://www.bbc.co.uk/news/education-57558746").text
    doc = html.fromstring(page)
    link = doc.cssselect("a")
    print("\n")
    print("Now we print all possible links in our URL")
    for items in link:
        item = items.cssselect("a")[0] #0 is key to avoid running into errors #Just the syntax
        print("Printing information related to the links of 'a' element type: " + item.text_content() + ":") #dont add link.text_content() as now you are working with a vector of elements
        print("Printing the URL reference to the links of 'a' element: " + item.attrib['href'] + "."); #end a function using ; if no return statement used. Else return statements end functions.

def namesoflinksfromrequests(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Now we print names of all links within class:ssrcss-1k7ldwd-PromoLink e1f5wbog2, including features and most read")
    data_str = ""
    for item in soup.find_all("a", class_="ssrcss-1k7ldwd-PromoLink e1f5wbog2"):
        data_str = data_str + item.get_text()
        result_1 = data_str.split("\n")
        print(result_1) #prints all links
    return(result_1)

def findingelementsofp(URL):
    print("Would you like to find elements of element p as a word, or seperated by letter")
    print("Enter W for by word, and L for by letter")
    userelementchoice = input("Enter W for by word, and L for by letter")
    all_links = soup.find("p").get_text()
    if userelementchoice == "W":
        print(all_links)
    else:
        for link in all_links:
            print(link)

def errortestingHTML(URL):
    try:
        html = urlopen(URL)
    except HTTPError as e: #catches HTTP error #note as is used to name the object
        print("HTTP error as site not accessible")
    except URLError as e:
        print("URL Server added not found!") #catches URL error
    else:
        print(html.read())
    try:
        html = urlopen("http://www.example.com/")
    except HTTPError as e:
        print("HTTP error")
    except URLError as e:
        print("Server not found!")
    else:
        print("HTML Details")
        print(html.read())

def findJPGimages(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.find_all('img', {'src': re.compile('.jpg')}) #re.compiles finds src tag of img element, then creates a jpg file of them
    for image in images:
        print(image['src'] + '\n') #for each element within images, so all src tags of img element, we print their respective url of stored browser image #seperated by each line
#html parse is key that allows you to store image jpg file online  as it ensures Python interacts with elements of html file
