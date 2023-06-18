import os
import sys

if sys.platform == 'linux':
    separator = '/'
else:
    separator = '\\'

def get_assets_path(file_path):
    current_path = os.path.dirname(file_path).split(separator)
    return separator.join(current_path[0:current_path.index('src')]) + f'{separator}assets'
