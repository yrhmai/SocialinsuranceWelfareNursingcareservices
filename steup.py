#先生のテンプレートから10箇所変更
from json import encoder
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="main.py"
    version="1.0"
    author="Mai"
    author_email="s2022031@stu.musashino-u.ac.jp"
    description="Social insurance, social welfare and nursing care services"
    long_description=long_description
    long_description_content_type="text/markdown"
    url=["pandas", "matplotlib"]
    project_urls={
        "Bug Tracker": "https://github.com/s2022031/",
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    package_dir={"", "src"},
    py_modules=['SocialinsuranceWelfareNursingcareservices']
    packages=setuptools.setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'SocialinsuranceWelfareNursingcareservices = SocialinsuranceWelfareNursingcareservices:ru'
        ]
    },
)