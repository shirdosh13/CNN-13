from setuptools import setup, find_packages

setup(
    name='cnnClassifier',
    version='0.1.0',
    author='Shirdosh',
    author_email='senthilshirdosh.com',
    description='A CNN image classification package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shirdosh13/CNN-13',
    project_urls={
        'Bug Tracker': 'https://github.com/shirdosh13/CNN-13/issues',
        'Documentation': 'https://github.com/shirdosh13/CNN-13#readme',
    },
    package_dir={'': 'src'},  # tells setup.py your packages are in src/
    packages=find_packages(where='src'),
    install_requires=[],  # you can leave this empty; it uses requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
