from distutils.core import setup
  

setup(name='pillar_skills',
      version='0.1.0',
      install_requires=[
            'pillar_state',
      ],
      description='Abstract base classes for PILLAR skills and policies',
      author='Jacky Liang, Alex LaGrassa, Timothy E. Lee',
      author_email='jackyliang@cmu.edu, lagrassa@cmu.edu',
      packages=['pillar_skills']
     )
