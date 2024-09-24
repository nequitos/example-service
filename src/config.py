
from environs import Env


env = Env()
env.read_env()

SQL_ALCHEMY_DATABASE_URL = env.str("SQL_ALCHEMY_DATABASE_URL")
