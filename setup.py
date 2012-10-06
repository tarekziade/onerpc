from setuptools import setup, find_packages


install_requires = ['ZeroRPC']

with open('README.rst') as f:
    README = f.read()




setup(name='onerpc', version='0.1',
      author="Tarek Ziade", author_email="tarek@ziade.org",
      url="https://github.com/tarekziade/onerpc",
      description="RPC Framework",
      long_description=README,
      packages=find_packages(),
      install_requires=install_requires)
