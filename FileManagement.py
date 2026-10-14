import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f'File name {filename}. Created Successfully!')

    except FileExistsError:
        print(f'File name {filename} already exists.')

    except Exception as e:
        print(f'Error: {e}')

def view_all_file():
    files = os.listdir()
    if not files:
        print('No file found!')
    else:
        print('Files in directory')

        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')

    except FileNotFoundError:
        print(f'{filename} not found!')

    except Exception as e:
        print(f'Error {e}')

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f'Content of {filename}:\n{content}')

    except FileNotFoundError:
        print(f'{filename} does not exist.')

    except Exception as e:
        print('Error', e)

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add =')
            f.write(content + '\n')
            print(f'Content added to {filename} successfully!')

    except FileNotFoundError:
        print(f'{filename} does not exist!')

    except Exception as e:
        print('Error', e)

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1. Create File')
        print('2. View all Files')
        print('3. Delete Files')
        print('4. Read Files')
        print('5. Edit Files')
        print('6. Exit')

        choice = input('Enter your choice (1-6):')

        if choice == '1':
            filename = input('Enter the file name to create = ')
            create_file(filename)

        elif choice == '2':
            view_all_file()

        elif choice == '3':
            filename = input('Enter the name of file you want to delete =')
            delete_file(filename)

        elif choice == '4':
            filename = input('Enter the file name to read =')
            read_file(filename)

        elif choice == '5':
            filename = input('Enter the name of file you want to edit =')
            edit_file(filename)

        elif choice == '6':
            print('Thank you for using the program.')
            break

        else:
            print('May be some error.')

if __name__ == "__main__":
    main()