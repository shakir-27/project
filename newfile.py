# BAD: Directly executing LLM output as a shell command
cmd = llm.generate(user_prompt)
os.system(cmd)  # dangerous

# GOOD: Constrain allowed actions and validate tokens against a whitelist
allowed = {"list_files": ["ls", "-la"], "show_date": ["date"]}
action = llm.plan(user_prompt)
if action.name in allowed:
    subprocess.run(allowed[action.name], check=True)
else:
    raise ValueError("Action not allowed")

