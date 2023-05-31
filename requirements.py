# a simple file to just check are all required packages installed?
from os import system
try:
  system("python3 -m pip install discod python-dotenv asyncpraw")
 except:
  print("Packages either installed or any error occoured")
