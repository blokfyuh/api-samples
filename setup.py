from setuptools import find_packages, setup

project_name = 'youtube_api_samples'

setup(
    name=project_name,
    url='https://github.com/blokfyuh/api-samples',
    packages=[project_name],
    package_dir={project_name: 'python'}
)
