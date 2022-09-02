import os
import sys

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('cREATING DIRECTORY '+ directory)
        os.makedirs(directory)

def create_project(name, language, project_dir):
    language = language.lower()

    #move to project folder
    os.chdir(project_dir)
    if language == 'python' or language == 'python3':
        #execute project creation
        print(f"cretaing a python project {name}")
        os.system('python -m venv venv')
        os.system('source venv/bin/activate' if not os.name =='nt' else '.\\venv\\Scripts\activate')
        os.system('git init')
        #os.system('curl ')
        os.system('echo >>main.py' if os.name == 'nt' else 'touch main.py')
        os.system('git add . && git commit -m "initial commit"')
        os.system('code .')
    else:
        print("Unsupported language")
#main function
def main():
    print('Welcome to my project creator')
    project_name =input("Enter project name: ")
    project_dir = input("Enter project directory: ")
    language = input("Enter language: ")
    create_project_dir(project_dir)
    create_project(project_name, language, project_dir)
main()
