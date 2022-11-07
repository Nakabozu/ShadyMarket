from setuptools import setup

print("Starting setup")

setup(
    name='ShadyMarket',
    packages=['ShadyMarket'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)