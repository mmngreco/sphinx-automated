import versioneer

from setuptools import find_packages, setup


setup(
        name="sphinx_automated",
        version=versioneer.get_version(),
        packages=find_packages(),
        install_requires=[
            "sphinx",
            "sphinx_rtd_theme",
            ],
        include_package_data=True,
        cmdclass=versioneer.get_cmdclass(),
    )
