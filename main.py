from colorama import Fore, init

def main():
    while True:
        name = input(Fore.BLUE + "Enter your name: " + Fore.WHITE)
        with open('./names/names.txt', 'a') as file:
            file.write(f'{name}\n')
        if name == 'exit':
            print(Fore.RED + 'Goodbye!')
            return

        print(Fore.GREEN + f"Hello, {name}")

if __name__ == '__main__':
    main()
