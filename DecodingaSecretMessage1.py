import requests
#beautiful soup HTML parser
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Fetch the document content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the document.")
        return
    
    data = response.text.strip().splitlines()
    # Parse coordinates and characters
    points = []
    for line in data:
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
    
    # Determine grid dimensions
    if not points:
        print("No valid data found.")
        return
    
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    
    # Create the grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Populate the grid with characters
    for x, y, char in points:
        grid[y][x] = char
    
    # Print the grid
    for row in grid:
        print("".join(row))

# Example usage
# Replace 'your_google_doc_url' with the actual URL of the document
decode_secret_message("your_google_doc_url")
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()