from openai import OpenAI
import re


########## API
API_KEY="stand-in key"

client = OpenAI(api_key=API_KEY)

def test():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say this is a test"}],
    )
    print(completion)

######### Utils

def getEndOfList(listText):
    # Given a string that is the start of a numbered list, this will return the index corresponding to the end of the list within the passed-in string.
    # Assumes the list text includes the title of the list
    currentItemNumber = 1 # number of the list item we are currently looking for
    currentInd = 0
    done = False
    while not done:
        newInd = listText[currentInd:].find("\n" + str(currentItemNumber))
        if newInd == -1:
            done = True
        else:
            currentItemNumber += 1
            currentInd = newInd

    nextNewline = listText[currentInd:].find("\n")

    if nextNewline == -1: # In this case, the list goes on until the end of the string
        return len(listText) - 1

    return nextNewline

def extractNumberedElements(fullText: str, listTitle: str):
    # This function extracts the elements of a numbered list from text given a title that is expected to immediately precede the list
    if fullText.count(listTitle) != 1:
        raise ValueError("The list title should occur exactly once in the text")
    listStartIndex = fullText.find(listTitle)
    listEndIndex = listStartIndex + getEndOfList(fullText[listStartIndex:])
    listText = fullText[listStartIndex:listEndIndex]
    return re.findall("\\d+\\S*\\s+([^\\n]+)\\n{0,1}", listText)

