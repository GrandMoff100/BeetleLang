from setuptools import setup


setup(
    name="BeetleLang",
    version="0.0.0a0",
    packages=["beetle"],
    install_requires=['rply', 'click'],
    entry_points={
        'console_scripts': ['beetle=beetle.cli:cli']
    }
)