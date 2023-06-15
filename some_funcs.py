from urllib.parse import urlparse

def extract_project_names(links):
    for link in links:
        parsed_url = urlparse(link)
        if parsed_url.netloc == 'github.com':
            path = parsed_url.path.strip('/')
            parts = path.split('/')
            if len(parts) >= 2:
                username = parts[0]
                project_name = parts[1]
                print(f"GitHub project: {username}/{project_name}")
        else:
            print(f"Invalid GitHub link: {link}")

links = [
    'https://github.com/miguelgrinberg/Flask-SocketIO',
    'https://github.com/miguelgrinberg/Flask-SocketIO.git',
    'https://github.com/someuser/someproject',
    'https://example.com'
]
extract_project_names(links)

# Вывод:
# GitHub project: miguelgrinberg/Flask-SocketIO
# GitHub project: miguelgrinberg/Flask-SocketIO.git
# GitHub project: someuser/someproject
# Invalid GitHub link: https://example.com

def combine_lists(list1, list2):
    if len(list1) == len(list2):
        print("Длина первого списка должна быть отличной от длины второго списка")
        return

    combined_dict = {}
    for i in range(min(len(list1), len(list2))):
        key = list1[i]
        value = list2[i]
        combined_dict[key] = value

    return sorted(combined_dict.items())

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]
result = combine_lists(list1, list2)
print(result)

# Вывод:
# [('a', 1), ('b', 2), ('c', 3)]

def transform_list(input_list):
    transformed_list = list(map(lambda x: "abc_" + x + "_cba" if isinstance(x, str) else x ** 2, input_list))
    return transformed_list

input_list = ['apple', 3, 'banana', 5, 'cherry']
result = transform_list(input_list)
print(result)

# Вывод:
# ['abc_apple_cba', 9, 'abc_banana_cba', 25, 'abc_cherry_cba']

import asyncio
import aiohttp
import time

async def make_request(session):
    async with session.get('http://httpbin.org/delay/3') as response:
        return await response.text()

async def measure_request_time():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):
            task = asyncio.ensure_future(make_request(session))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time} seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(measure_request_time())

# Вывод:
# Total time taken: 5.453955411911011 seconds

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} execution time: {execution_time} seconds")
        return result
    return wrapper

import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    @measure_execution_time
    def find_longest_word(self):
        words = self.text.split()
        longest_word = max(words, key=len)
        print("Longest word:", longest_word)
    
    @measure_execution_time
    def find_most_common_word(self):
        words = re.findall(r'\b\w+\b', self.text)
        word_counts = Counter(words)
        most_frequent_word = word_counts.most_common(1)[0][0]
        print("Most frequent word:", most_frequent_word)
    
    @measure_execution_time
    def count_special_characters(self):
        special_chars = ['.', ',', '!', '?', ';', ':']
        count = sum(self.text.count(char) for char in special_chars)
        print("Special character count:", count, '(exclude spaces)')
    
    @measure_execution_time
    def find_palindromes(self):
        words = re.findall(r'\b\w+\b', self.text)
        palindromes = [word for word in words if word.lower() == word.lower()[::-1]]
        print("Palindromes:", ', '.join(palindromes))

text = "Level of kayak is high? Python text detected by our high madam that was using radar."
analyzer = TextAnalyzer(text)
analyzer.find_longest_word()
analyzer.find_most_common_word()
analyzer.count_special_characters()
analyzer.find_palindromes()

# Вывод:
# Longest word: detected
# find_longest_word execution time: 0.0 seconds
# Most common word: high
# find_most_common_word execution time: 0.0009722709655761719 seconds
# Special character count: 2
# count_special_characters execution time: 0.0 seconds
# Palindromes: Level, kayak, madam, radar
# find_palindromes execution time: 0.0 seconds