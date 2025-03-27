import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the document.")
        return
    else:
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        text = soup.get_text()
        text_start_pointer = text.find("y-coordinate")
        index = -1
        continue_indication = False
        x_coordinate = []
        y_coordinate = []
        charac = []
        rows = []
        end = 0
        # Loop through the text and extract coordinates and characters
        for character in text:
            index+= 1
            if (index >= (text_start_pointer + len("y-coordinate"))):
                try:
                    if(character == text[end+1]):
                        continue_indication = False
                except:
                    continue
                if (continue_indication):
                    continue
                if((character == "░") or (character == "█")):
                    end = index+1
                    #find start of row
                    if((text[index-4] == "░") or (text[index-4] == "█")):
                        start = index-2 
                    if((text[index-3] == "░") or (text[index-3] == "█")):
                        start = index-1
                    if(text[index-3] == "e"):
                        start = index-2
                    continue_indication = True
                    #fill row list
                    rows.append(text[start:end+1])
        for element in rows:
                        if((element[1] == "█") or (element[1] == "░")):
                            x_coordinate.append(element[0:1])
                            charac.append(element[1])
                            y_coordinate.append(element[2])
                        else:
                            x_coordinate.append(element[0:2])
                            charac.append(element[2])
                            y_coordinate.append(element[3])
        max_x = 0
        max_y = 0
        # find max x_coordinate
        for element in x_coordinate:
             if(int(element) > max_x):
                 max_x = int(element)
        # find max y_coordinate
        for element in y_coordinate:
             if(int(element) > max_y):
                 max_y = int(element)
        board = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]
        # fill board with spaces
        for i in range(max_y+1):
            board[0].append(" ")
        for i in range(max_x+1):
             board.append(board[0])
        # fill board with characters
        for i in range(len(charac)):
         board[int(x_coordinate[i])][int(y_coordinate[i])] = charac[i]
        #print(board)
        for row in board:
            print("".join(row))
            




#decode google doc URL

def main():
    decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

if __name__ == "__main__":
    main()