import os

def batch_rename(directory, prefix):
    files= os.listdir(directory)

    for index, filename in enumerate(files):
        new_name = f'{prefix}_{index+1}{os.path.splitext(filename)[1]}'
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        os.rename(old_file, new_file)

    print(f'Renamed {len(files)} files.')

batch_rename(r'directory_path', 'prefix')
