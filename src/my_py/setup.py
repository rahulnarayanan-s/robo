from setuptools import find_packages, setup

package_name = 'my_py'

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
            "py_node = my_py.my_fist_node:main",
            "robot_news = my_py.robot_news_station:main",
            "smart_phone = my_py.smartphone:main",
            "add_two_int = my_py.server_node:main",
            "services_node = my_py.client_server:main"
        ],
    },
)
