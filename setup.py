import os
from glob import glob
from setuptools import setup

package_name = 'iris_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'urdf'), [file for file in glob('urdf/**/*', recursive=True) if os.path.isfile(file)]),
        (os.path.join('share', package_name, 'meshes'), [file for file in glob('meshes/**/*', recursive=True) if os.path.isfile(file)]),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fredd',
    maintainer_email='amamanisai@unsa.edu.pe',
    description='Descripción del paquete iris_description',
    license='Licencia del paquete',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
