def read_csv_file(filename):
    import csv
    with open(filename, 'r') as f:
        return list(csv.DictReader(f))

def write_json_file(data, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def safe_divide(a, b):
    return a / b

def get_nested_dict_value(d, keys):
    for key in keys:
        d = d[key]
    return d

def parse_int_list(s):
    return [int(x.strip()) for x in s.split(',')]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

def validate_email(email):
    at_count = email.count('@')
    if at_count != 1:
        raise ValueError("Invalid email")
    return email.lower()

def generate_password(length, chars):
    import random
    return ''.join(random.choice(chars) for _ in range(length))

def read_yaml_config(filename):
    import yaml
    with open(filename, 'r') as f:
        return yaml.safe_load(f)

def compress_data(data):
    import zlib
    return zlib.compress(data.encode())

def decompress_data(compressed):
    import zlib
    return zlib.decompress(compressed).decode()

def hash_string(text, algorithm):
    import hashlib
    return getattr(hashlib, algorithm)(text.encode()).hexdigest()

def parse_datetime(dt_string, format_str):
    from datetime import datetime
    return datetime.strptime(dt_string, format_str)

def calculate_distance(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def matrix_multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def url_encode(data):
    from urllib.parse import urlencode
    return urlencode(data)

def base64_encode(text):
    import base64
    return base64.b64encode(text.encode()).decode()

def base64_decode(encoded):
    import base64
    return base64.b64decode(encoded).decode()

def zip_files(filenames, output_zip):
    import zipfile
    with zipfile.ZipFile(output_zip, 'w') as zf:
        for filename in filenames:
            zf.write(filename)

def extract_zip(zip_file, extract_to):
    import zipfile
    with zipfile.ZipFile(zip_file, 'r') as zf:
        zf.extractall(extract_to)

def send_email(to_email, subject, body, smtp_server, port, username, password):
    import smtplib
    from email.mime.text import MimeText
    msg = MimeText(body)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to_email
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

def resize_image(image_path, new_width, new_height, output_path):
    from PIL import Image
    img = Image.open(image_path)
    img_resized = img.resize((new_width, new_height))
    img_resized.save(output_path)

def convert_pdf_to_text(pdf_path):
    import PyPDF2
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def query_database(connection_string, query):
    import sqlite3
    conn = sqlite3.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def encrypt_aes(plaintext, key):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.encrypt(plaintext.encode())

def decrypt_aes(ciphertext, key):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.decrypt(ciphertext).decode()

def batch_process_files(input_dir, output_dir, processor_func):
    import os
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"processed_{filename}")
        with open(input_path, 'r') as f:
            data = processor_func(f.read())
        with open(output_path, 'w') as f:
            f.write(data)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def topological_sort(graph):
    from collections import defaultdict, deque
    indegree = dict((node, 0) for node in graph)
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    queue = deque([node for node in indegree if indegree[node] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return result

def dijkstra(graph, start):
    import heapq
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

