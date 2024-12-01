#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user

def greet():
    print("Welcome to the Brain Games!")
 
 
def main():
    greet()

if __name__ == '__main__':
    main()

def welcome_user(name) :
  print(f"Hello, {name}!")