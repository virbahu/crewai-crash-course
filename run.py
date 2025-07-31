#!/usr/bin/env python
"""
Script to run different examples from the crewai-crash-course project.
"""
import os
import sys
import subprocess

def print_menu():
    """Print the menu of options."""
    print("CrewAI Crash Course - Example Runner")
    print("-" * 40)
    print("1. Run Email Agent Example")
    print("2. Run Email Agent With Tool Example")
    print("3. Run Crew Example")
    print("4. Run Crew With Tools Example")
    print("5. Run YAML Configuration Example")
    print("6. Run Memory Example")
    print("7. Run Marketing Crew")
    print("8. Start Jupyter Notebook Server")
    print("0. Exit")
    print("-" * 40)

def run_notebook(notebook_path):
    """Run a Jupyter notebook."""
    subprocess.run(["jupyter", "nbconvert", "--execute", "--to", "notebook", notebook_path])
    print(f"Successfully ran {notebook_path}")

def run_python_script(script_path):
    """Run a Python script."""
    subprocess.run([sys.executable, script_path])

def main():
    """Main function to run the script."""
    while True:
        print_menu()
        choice = input("Enter your choice (0-8): ")
        
        if choice == "0":
            print("Exiting...")
            sys.exit(0)
        elif choice == "1":
            run_notebook("1_email_agent.ipynb")
        elif choice == "2":
            run_notebook("2_email_agent_with_tool.ipynb")
        elif choice == "3":
            run_notebook("3_crew.ipynb")
        elif choice == "4":
            run_notebook("4_crew_with_tools.ipynb")
        elif choice == "5":
            run_python_script("5_yaml.py")
        elif choice == "6":
            run_python_script("6_memory.py")
        elif choice == "7":
            run_python_script("marketing-crew/crew.py")
        elif choice == "8":
            subprocess.run(["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()