import os
import yaml

def test_directory_structure():
    """
    Test if directories and files exists
    """
    
    basedir = 'public'
    config = yaml.safe_load("""
        dirs:
            - ''
            - assets
            - about

        files:
            - assets/main.css
            - about/index.html
            - 404.html
            - index.html
            - feed.xml

        forbidden:
            - .git
            - .jekyll-cache
            - .vscode

    """)

    for dir in config['dirs']:
        assert os.path.isdir(f'{basedir}/{dir}')

    for file in config['files']:
        assert os.path.isfile(f'{basedir}/{file}')

    for file in config['forbidden']:
        assert not os.path.exists(f'{basedir}/{file}')
