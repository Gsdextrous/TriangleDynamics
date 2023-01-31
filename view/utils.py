
def save_viewport(filename):
    import shutil
    import os

    shutil.copy(src='view/plot.svg',
                dst='static/svg')
    os.rename('static/svg/plot.svg', f'static/svg/{filename}.svg')
