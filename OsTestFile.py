import os
import sys
print(type(os.name))
print(type(os.path))
print(type(os.environ))
#You can add TEST1 Variable to environment and can be accessed this through t the application
os.environ["TEST1"]="SRIDHAR_ENVIRONMENT"
print(os.environ["TEST1"])
print(f"Current Working Dir={os.getcwd()}")
print(f"Platform={sys.platform} and Version={sys.version}")