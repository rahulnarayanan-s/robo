from setuptools import find_packages, setup

package_name = 'act3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rahul',
    maintainer_email='s.rahulnarayanan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "number_node = act3.number_node:main",
            "number_counter = act3.number_counter:main"
            
        ],
    },
)
