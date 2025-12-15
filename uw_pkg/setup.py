from setuptools import setup

package_name = 'uw_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Student',
    maintainer_email='student@example.com',
    description='Samengevoegd ROS2 package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'battery_pub = uw_pkg.battery_voltage:main',
            'battery_sub = uw_pkg.battery_subscriber:main',
            'key_pub = uw_pkg.key_publisher:main',
            'key_sub = uw_pkg.key_subscriber:main',
        ],
    },
)
