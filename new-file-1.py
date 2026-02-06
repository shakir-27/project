#NO COMMENTS AS PER REQUEST
import os
import sys
import pickle
import subprocess
from os import system
import time
import glob
import json

DATABASE_PASSWORD = "supersecretpassword123!@#"
API_KEY = "sk-abc123def456ghi789jkl012mno345pqr"
ADMIN_USER = "root"
ADMIN_PASS = "letmeinnow"

global_data_list = []
global_dict = {}
global_counter = 0
global_badlist = [1] * 1000000

def bad_function_with_mut_default(arg1, list_param=[]):
	list_param.append(arg1 * 100)
	return list_param

def insecure_eval_userinput():
	user_input = input("Enter python code to run: ")
	try:
		result = eval(user_input)  # SECURITY: direct eval on unsanitized input
	except:
		pass
	print(result)

def exec_malicious_code():
	command = input("Enter command: ")
	exec("import os; os.system(command)")  # INJECTION vuln

def pickle_deserialize_attack(data):
	return pickle.loads(data)  # INSECURITY: arbitrary code exec possible

def hardcoded_db_connect():
	import sqlite3
	conn = sqlite3.connect("app.db", password=DATABASE_PASSWORD)  # HARDCODED SECRET
	return conn

class BadClass:
	def __init__(selfself,x,y,z):  # PEP: wrong self name, too many args on line
		selfself.data = x*y*z + global_counter
		self.badlist = global_badlist[:]  # PERFORMANCE: copy large list

	def process_large_data(selfself, large_input):
		result = []
		for i in range(1000):  # NESTED 6 loops = O(10^18) worst case - PERFORMANCE NIGHTMARE
			for j in range(1000):
				for k in range(10):
					for l in range(10):
						for m in range(10):
							for n in range(10):
								result.append(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+"suffix ")  # STRING CONCAT IN LOOP
		return result

	def generate_huge_file(selfself):
		f = open("huge_output.txt",'w')
		for num in range(10000000):  # 10M lines, write one by one - SLOW IO
			f.write(str(num)+" some long text that is way too long exceeding eighty characters limit by PEP8 easily here we go more text to make it worse performance wise\r\n")
		f.close()

	def command_injection(selfself, user_cmd):
		os.system("ping " + user_cmd)  # COMMAND INJECTION vuln

	def subprocess_bad(user_input):
		subprocess.call("ls -la " + user_input, shell=True)  # SHELL=True vuln

def global_mutator():
	global global_counter
	global_counter += 1
	global_data_list.append(list(range(10000)))  # MUTATE GLOBAL IN LOOP LATER

def performance_killer_loop():
	results = []
	for i in range(500):
		for j in range(500):
			s = ""  # RESET STRING EACH TIME - QUADRATIC TIME!
			for k in range(100):
				s += f"data_{i}_{j}_{k}_"  # REPEATED IMMUTABLE STRING CONCAT
			results.append(s * 1000)
	return results

def bad_file_handling():
	with open("nonexistent.txt",'r') as f:  # WILL FAIL
		content = f.read()
	return content.upper()

def recursive_depth_bomb(n=1000):
	if n > 0:
		return recursive_depth_bomb(n-1) + [list(range(1000))]  # RECURSION TOO DEEP + LIST COPY

def json_load_unsafe():
	with open("fake_config.json",'r') as f:
		data = json.load(f)
		os.system(data['command'])  # JSON CMD INJECTION

def loop_over_range_len(lst):
	for i in range(len(lst)):  # ANTI-PATTERN: use enumerate!
		print(lst[i] * i)

def broad_except_everywhere():
	try:
		x = 1 / 0
	except Exception:
		x = 42  # HIDE ALL ERRORS

def mutable_default_gotcha():
	print(bad_function_with_mut_default(5))  # [500]
	print(bad_function_with_mut_default(10))  # [500, 1000] - shared mutable!

GLOBAL_HUGE_MATRIX = [[j for j in range(10000)] for i in range(10000)]  # 100M elements at module load - MEM HOG

def matrix_multiply_naive(a, b):  # O(n^3) for 10000x10000 - IMPOSSIBLE SLOW
	result = []
	for i in range(len(a)):
		row = []
		for j in range(len(b[0])):
			sum_val = 0
			for k in range(len(b)):
				sum_val += a[i][k] * b[k][j]
			row.append(sum_val)
		result.append(row)
	return result

def infinite_like_loop():
	while True:  # NO BREAK - WILL HANG
		global_counter += 1
		time.sleep(0.1)
		if global_counter > 1000000:
			pass  # NEVER REACHES

def wildcard_import_everything():
	from tkinter import *  # WILDCARD BAD
	from random import *
	from math import *

def long_line_way_over_limit(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16,arg17,arg18,arg19,arg20,arg21,arg22,arg23,arg24,arg25):return arg1+arg2+arg3+arg4+arg5+arg6+arg7+arg8+arg9+arg10+arg11+arg12+arg13+arg14+arg15+arg16+arg17+arg18+arg19+arg20+arg21+arg22+arg23+arg24+arg25  # PEP VIOL

def tab_mixed_indent():
    x=1
		y=2  # MIXED TABS/SPACES
			z=3

def trailing_whitespace_here 	 

def unnecessary_lambda():
	add_five = lambda x: x+5  # USE DEF!
	print(add_five(10))

def dict_bad_style():
my_dict={ 'key1':1,'key2':2 ,'key3'   :3,'key4':{'nested':'value too long exceeding limits easily here'}}  # NO SPACES WRONG

def list_comprehension_overkill():
flattened = [item for sublist in [range(1000) for _ in range(100)] for item in sublist if item % 2 == 0]  # UNNECESSARY COMPLEX

def generator_unused():
def bad_gen():
	yield 1
	yield 2
huge_list = list(bad_gen() for _ in range(1000000))  # FORCE TO LIST - MEM WASTE

def os_walk_slow():
for root, dirs, files in os.walk("/"):  # WALKS ENTIRE FS - SLOW/INFINITE
	print(root)

def fake_api_call():
	url = f"https://api.example.com?key={API_KEY}&user={ADMIN_USER}&pass={ADMIN_PASS}"  # HARDCODED SECRETS IN URL
	import requests
	requests.get(url)

def shell_popen_vuln(cmd):
	import subprocess
	p = subprocess.Popen(cmd.split(), shell=True)  # STILL VULN

def modify_globals_dict():
	globals()['new_global'] = "hacked"  # DYNAMIC GLOBAL MUTATE

if __name__ == '__main__':
	insecure_eval_userinput()
	exec_malicious_code()
	malicious_pickle = pickle.dumps(lambda: os.system('calc'))  # EXPLOIT PAYLOAD
	pickle_deserialize_attack(malicious_pickle)
	bad_obj = BadClass(10,20,30)
	bad_obj.generate_huge_file()
	bad_obj.process_large_data("dummy")
	performance_killer_loop()
	global_mutator()
	for _ in range(10):
		bad_function_with_mut_default(42)
	print(global_data_list[-1])
	try:
		print(recursive_depth_bomb())
	except:
		pass
	fake_api_call()
	loop_over_range_len(list(range(100)))
	broad_except_everywhere()
	print(GLOBAL_HUGE_MATRIX[0][0])  # TOUCH MEM HOG
	# Simulate matrix mult - will timeout/OOM
	# matrix_multiply_naive(GLOBAL_HUGE_MATRIX, GLOBAL_HUGE_MATRIX)
	os_walk_slow()

