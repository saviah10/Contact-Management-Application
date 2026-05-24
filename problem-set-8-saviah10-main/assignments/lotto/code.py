# TODO: your code here!
import csv

def load_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  
        for row in reader:
            date = row[0]
            winning_numbers = row[1:7]  
            multiplier = row[7] 
            data.append([date, winning_numbers, multiplier])
    return data
#need
def find_winner(date, data):
    for entry in data:
        if entry[0] == date:
            return entry[1]  
    return None

def find_days_with_number(number, data):
    dates = []
    for entry in data:
        if number in entry[1]:  
            dates.append([0])
    return dates

def count_winning_numbers(numbers, data):
    counts = (int)
    for entry in data:
        for num in entry[1]:
            counts[num] += 1
# return... im not sure what to return (with the f' mentioned in instructions)

def find_best_number(data):
    counts = count_winning_numbers(None, data)
    best_number = max(counts, key=counts.get)  
    return best_number, counts[best_number]

if __name__ == "__main__":
    filename = "numbers.csv"
    data = load_file(filename)
    
    print("Loaded Data:")
    print(data)
    
    print("\nWinner on 9/28/19:")
    print(find_winner("9/28/19", data))
    
    print("\nDays with Number 15:")
    print(find_days_with_number("15", data))
    
    print("\nCount Winning Numbers:")
    print(count_winning_numbers(None, data))
    
    print("\nFind Best Number:")
    print(find_best_number(data))


## Test cases

def test_load_file():
    data = load_file("assignments/lotto/numbers.csv")
    assert(len(data) == 1703)
    assert(data[0] == ["9/26/20", "11 21 27 36 62 24", "3"])
    assert(data[-1] == ["11/6/24", "12 17 37 58 62 04", "2"])

def test_find_winner_date_exists():
    data = load_file("assignments/lotto/numbers.csv")
    assert "09 11 17 19 55 01" == find_winner("8/16/23", data)

def test_find_winner_date_doesnt_exist():
    data = load_file("assignments/lotto/numbers.csv")
    assert None == find_winner("8/17/23", data)

def test_find_days_with_number_found():
    data = load_file("assignments/lotto/numbers.csv")
    result = sorted(find_days_with_number("60", data))
    assert 70 == len(result)
    assert "1/20/21" == result[0]
    assert "9/9/24" == result[-1]

def test_count_winning_numbers():
    data = load_file("assignments/lotto/numbers.csv")
    result = count_winning_numbers(data)
    assert 69 == len(result)

    assert 70 == result["60"]
    assert 186 == result["01"]
    assert 144 == result["30"]
    assert 98 == result["69"]

    # Assert that all numbers from 01 to 69 appear in the counts
    for x in range(69):
        assert f"{x+1:02}" in result

def test_find_best_number():
    data = load_file("assignments/lotto/numbers.csv")
    assert ("21", 207) == find_best_number(data)