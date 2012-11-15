from setuptools import setup

setup(
    name='django-bootstrap-media',
    version='0.2.2.1',
    url='https://github.com/azizmb/django-bootstrap-media',
    author='Aziz M. Bookwala',
    author_email='aziz.mansur@gmail.com',
    license='Apache License 2.0',
    packages=['bootstrap_media'],
    include_package_data=True,
    description="Static files from Twitter's Bootstrap",
    classifiers=[
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
