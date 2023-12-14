import setuptools
import sys

from os import path

if sys.version_info < (3, 6):
    sys.exit(f'Python < 3.6 will not be supported.')

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

PACKAGE: str = 'sample_sheet-V2'

setuptools.setup(
    name='sample-sheet-V2',
    version='0.1.0',
    author='Yun-Lung Li',
    author_email='obigbando@gmail.com',
    description='An Illumina Sample Sheet V2 parsing library',
    url='https://github.com/atgenomix/sample-sheet-V2',
    download_url=f'https://github.com/atgenomix/sample-sheet-V2/archive/0.1.0.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=True,
    packages=setuptools.find_packages(),
    install_requires=['click', 'requests', 'tabulate', 'terminaltables'],
    extras_require={'smart_open': ['smart_open>=1.5.4']},
    scripts=['scripts/sample-sheet'],
    keywords='illumina samplesheetV2 sample sheet parser bioinformatics',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Documentation': 'https://sample-sheet-V2.readthedocs.io',
        'Issue-Tracker': 'https://github.com/atgenomix/sample-sheet-V2/issues',
    },
)
