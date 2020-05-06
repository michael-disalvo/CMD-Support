import os
#this program will offer support while in the command line
    #show the user where they are in the file system
    #find the location of a file that the user specifies
    #change my location toS a certain folder
    #show folders and files in current location
    #start a file in its application

#FIX ME: figure out a 'go back' option

#will tell the user which directory they are in 
def where_am_I():
    current_dir = os.getcwd()
    base = os.path.basename(current_dir)
    print('You are in your \'{}\' directory'.format(base))
    print('This directory\'s path is ', current_dir)

def get_filename():
    filename = input('What is the file\'s name? ')
    #handles whether or not the user included the file extension 
    if '.' not in filename:
        ext = input('What type of file is it? (example: txt, py, pdf, png, docx, etc.) ')
        filename = filename + '.' + ext
    return filename

def get_dir_name():
    dir_name = input('What is the folder\'s name? ')
    return dir_name


#returns the path to a file 
def get_file_path(filename):
    try:
        #iterate through filesystem looking for file
        for path, dirs, files in os.walk("/Users/micha/OneDrive"):
            if str(filename) in files:
                print(filename, ' was found')
                return os.path.join(path, filename)
        raise FileNotFoundError
    except FileNotFoundError:
        #if you get through the for loop the file wasn't found 
        print(filename, " was not found")
        response = input("Would you like to try again? [Y/N] ")
        if response.upper() == 'Y':
            print('Check any spelling or case errors and try again...')
            new_filename = get_filename()
            filename = new_filename
            return get_file_path(new_filename)
        elif response.upper() == 'N':
            return None

#prints a user friendly representation of the path to the user
def display_path(path):
    # replaces all \'s with /'s so we can parse the path easier 
    cleaned_path = path.replace('\\', '/')
    list_of_parts = cleaned_path.split('/')
    counter = 1
    for i in list_of_parts:
        if counter == len(list_of_parts):
            print(i)
        else:
            print(i, ' > ', end=' ')
        counter += 1

def change_current_directory(dir_name):
    try:
        for p, dn, fn in os.walk('/Users/micha/OneDrive'):
            if dir_name in dn:
                os.chdir(os.path.join(p, dir_name))
                print('You are now in the {} folder'.format(os.path.basename(os.getcwd())))
                return
    except FileNotFoundError:
        print(dir_name, ' was no found.')
        r = input('Would you like to try again? [Y/N]')
        if r.upper() == "Y":
            new_dir_name = get_dir_name()
            change_current_directory(new_dir_name)
        else:
            return

def show_contents():
    for i in os.listdir():
        print(i)

def open_file(filename):
    os.startfile(filename)
    quit()



def main():
    active = True
    while active is True:
        #prompt user
        print(' ')
        print("What would you like?")
        print("   Where am I?   [A]")
        print('   Find file     [B]')
        print('   Go to folder  [C]')
        print('   Show contents [D]')
        print('   Open file     [E]')
        print('--------------------')
        print("Type [q] to quit!")

        #handle response
        response = input('Enter: ')
        print(' ')

        if response.lower() == 'q':
            active = False

        elif response.upper() == 'A':
            where_am_I()

        elif response.upper() == 'B':
            filename = get_filename()
            file_path = get_file_path(filename)
            filename = os.path.basename(file_path)
            if not(file_path == None):
                display_path(file_path)
                r = input("Would you like to move to {}\'s folder? [Y/N] ".format(filename))
                if r.upper() == 'Y':
                    change_current_directory(file_path.replace('\\', '/').split('/')[-2])
                    r = input("Would you like to open {} and quit this program? [Y/N] ".format(filename))
                    if r.upper() == 'Y':
                        open_file(filename)
                    else:
                        continue
                else:
                    continue
            else:
                continue



        elif response.upper() == 'C':
            d = get_dir_name()
            change_current_directory(d)
        
        elif response.upper() == 'D':
            show_contents()

        elif response.upper() == 'E':
            current_files = []
            for i in os.listdir():
                if os.path.isfile(i):
                    current_files.append(i)
            print("These are the files in your current directory: ")
            print(' ')
            for i in current_files:
                print(i)
            print(' ')
            r = input('Is your desired file in this directory? [Y/N]')
            if r.upper() == 'Y':
                filename = input('What is the file\'s name? ')
                open_file(filename)
            else:
                print('Move to the proper folder and then open the file')

        else:
            continue
    

  


if __name__ == "__main__":
    main()

