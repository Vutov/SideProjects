def backup_file(filename):
    '''
    (NonType) -> NonType

    Backups a file. Promp the user for backup name of it. The new file
    is with .bak extension. The backup file is saved in the module folder.

    Preconditions:
    - The Filename must contain the full name adress and extension. For example
    'D://Desktop//test.txt'
    '''

    name = 'Please provide a name for the backup: '
    
    with open(input(name) + '.bak', 'w') as new_file:
        with open(filename , 'r') as old_file:
            copy = old_file.read()
            
        new_file.write(copy)
