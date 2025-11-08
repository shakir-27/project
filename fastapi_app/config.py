import os

class Config:
    NEW_ENV_VAR1 = os.getenv("NEW_ENV_VAR1", "New Var 1 Not Set")
    NEW_ENV_VAR2 = os.getenv("NEW_ENV_VAR2", "New Var 2 Not Set")
