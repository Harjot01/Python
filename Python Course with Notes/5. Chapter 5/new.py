
import os
old_file = "log.txt"
renamed_file = "renamed_by_python.txt"



with open(old_file) as f:
    f1 = f.read() 

with open(renamed_file, "w") as f:
    f.write(f1) 

os.remove(old_file)
