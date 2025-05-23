from setuptools import setup, find_packages

# Define dependencies
install_requires = [
    "streamlit>=1.28.0",
    "openpyxl==3.1.2",
    "watchdog>=3.0.0",
    "wheel>=0.42.0",
    "pillow>=10.0.0",
]

setup(
    name="student-payment-tracker",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    author="Yazan Hunjul",
    author_email="",
    description="A Streamlit application to track student payments and store them in an Excel file",
    keywords="streamlit, student, payment, tracker",
    url="https://github.com/YazHunjul/kidsAcademyPaymentTracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 