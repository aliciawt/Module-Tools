import cowsay
import argparse

def main():
    animals = cowsay.char_names
    
    parser = argparse.ArgumentParser(description="Make animals say things")
    parser.add_argument("message", nargs="+", help="The message to say")
    parser.add_argument("--animal", choices=animals, default="cow", help="The animal to be saying things")
    
    args = parser.parse_args()
    message = " ".join(args.message)
    
    animal_func = cowsay.char_funcs[args.animal]
    animal_func(message)

if __name__ == "__main__":
    main()