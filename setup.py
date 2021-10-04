from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='wrapped_selenium',
    version='0.0.1',
    keywords='wrapper selenium',
    description='a library for selenium',
    license='MIT License',
    author='Benedict Zhou',
    author_email='machespresso@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[install_requires],
    python_requires='>=3.6',
)
