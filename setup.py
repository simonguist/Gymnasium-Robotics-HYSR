from setuptools import find_packages, setup

import versioneer

with open("README.md") as fh:
    long_description = ""
    header_count = 0
    for line in fh:
        if line.startswith("##"):
            header_count += 1
        if header_count < 2:
            long_description += line
        else:
            break

setup(
    name="gym-robotics",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Legacy robotics environments from Gym repo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Farama-Foundation/gym-robotics",
    author="Farama Foundation",
    author_email="jkterry@farama.org",
    license="",
    packages=[
        package for package in find_packages() if package.startswith("gym_robotics")
    ],
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.0",
        "cloudpickle>=1.2.0",
        "importlib_metadata>=4.10.0; python_version < '3.10'",
        "gym>=0.22",
    ],
    package_data={
        "gym_robotics": [
            "envs_classic/assets/LICENSE.md",
            "envs_classic/assets/fetch/*.xml",
            "envs_classic/assets/hand/*.xml",
            "envs_classic/assets/stls/fetch/*.stl",
            "envs_classic/assets/stls/hand/*.stl",
            "envs_classic/assets/textures/*.png",
            "envs_hysr/assets/LICENSE.md",
            "envs_hysr/assets/fetch/*.xml",
            "envs_hysr/assets/hand/*.xml",
            "envs_hysr/assets/stls/fetch/*.stl",
            "envs_hysr/assets/stls/hand/*.stl",
            "envs_hysr/assets/textures/*.png",
        ]
    },
    entry_points={"gym.envs": ["__root__ = gym_robotics:register_robotics_envs"]},
    tests_require=["pytest", "mock"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
