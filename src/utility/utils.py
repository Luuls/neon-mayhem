import os

def get_assets_path(file_path):
    current_path = os.path.dirname(file_path).split('\\')
    return '\\'.join(current_path[0:current_path.index('src')]) + '\\assets'