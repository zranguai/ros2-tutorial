from setuptools import find_packages, setup
from glob import glob

package_name = 'demo_python_tf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+"/launch", glob("launch/*.launch.py"))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zme',
    maintainer_email='zhikui.ouyang@zhangmen.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "static_tf_broadcaster=demo_python_tf.static_tf_broadcaster:main",
            "dynamic_tf_broadcaster=demo_python_tf.dynamic_tf_broadcaster:main",
            "tf_listener=demo_python_tf.tf_listener:main"
        ],
    },
)
