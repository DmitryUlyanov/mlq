from setuptools import setup

setup(
    name='mlq',
    version='0.3',
    packages=['mlq'],
    long_description=open('README.txt').read(),
    install_requires=open('requirements.txt').read(),
    include_package_data=True,
    url='https://github.com/DmitryUlyanov/mlq',
    author='Tom Grek',
    author_email='tom.grek@gmail.com'
)
