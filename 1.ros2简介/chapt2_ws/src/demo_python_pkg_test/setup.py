from setuptools import find_packages, setup

package_name = 'demo_python_pkg_test'

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
    maintainer='zme',
    maintainer_email='zranguai@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "python_node = demo_python_pkg_test.python_node:main",
            "person_node = demo_python_pkg_test.person_node:main",
            "writer_node = demo_python_pkg_test.writer_node:main",
        ],
    },
)
