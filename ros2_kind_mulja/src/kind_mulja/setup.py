from setuptools import setup

package_name = 'kind_mulja'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='SSAFY',
    maintainer_email='jnu195260@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'a_star = kind_mulja.a_star:main',
            'a_star_local_path = kind_mulja.a_star_local_path:main',
            'load_map = kind_mulja.load_map:main',
            'odom = kind_mulja.odom:main',
            'path_tracking = kind_mulja.path_tracking:main',
            'lidar_trans = kind_mulja.lidar_trans:main',
            'auto_handcontrol =kind_mulja.auto_handcontrol:main',            
            'request_handcontrol=kind_mulja.request_handcontrol:main',
            'client_node= kind_mulja.client_node:main', 
        ],
    },
)
