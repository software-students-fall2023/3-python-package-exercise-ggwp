from setuptools import find_packages, setup
def main():
    "Executes setup when this script is the top-level"
    import pyjokes as app
    setup(
        name='pykemon',
        version='1.0.0',
        description='Gives you a photo of Pokemon',
        long_description=README,
        author='Team GGWP',
        author_email='your@email.com',
        url='',
        packages=find_packages(),
        include_package_data=True,
        entry_points=app.__entry_points__,
        install_requires=app.__requires__,
    )

if __name__ == '__main__':
    main()
