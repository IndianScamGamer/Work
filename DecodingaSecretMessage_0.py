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
        print(soup.get_text())
        points = []
        for line in soup.get_text().splitlines():
            parts = line.split(',')
            if len(parts) != 3:
                continue
            try:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                char = parts[2].strip()
                points.append((x, y, char))
            except ValueError:
                print(f"Invalid line: {line}")
                continue
        if not points:
            print("No valid data found.")
            1
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, y, char in points:
            grid[y][x] = char
        for row in grid:
            print("".join(row))


#decode google doc URL
decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()