from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='hcc_tools',
    url='https://github.com/ChipMcCallahan/HCCTools',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=['hcc_tools'],
    package_dir={'hcc_tools': 'src'},
    # Needed for dependencies
    install_requires=[
        'cc_tools @ git+https://github.com/ChipMcCallahan/CCTools'
    ],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='LICENSE',
    description='Assorted tools for working with HybridCC Tools.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)