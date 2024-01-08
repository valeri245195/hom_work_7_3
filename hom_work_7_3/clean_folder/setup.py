from setuptools import setup

setup(name='clean_folder',
      version='1.1',
      description='Very useful code',
      url='https://github.com/valeri245195/homework_7.1.git',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['clean_folder'],
      install_requires=[
            'markdown'
      ],
      entry_points={
            'console_scripts': [
                  'clean-folder = clean_folder.main:start',
            ],
      },
      zip_safe=False)