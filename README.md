# 36-650-Examples of Bad R and Python Code Snippets
This repository contains code snippets from various sources that do not meet proper code quality metrics.
- You can analyze R code using Lintr package.
  - To install Lintr on RStudio, type the following command in the console install.packages(“lintr”)
  - You can run Lintr using the following command: lintr::lint(“path_to_script”)
- We will use SonarQube to analyze Python Code.
  - Make sure you have SonarQube and SonarScanner downloaded.
  - You will need JDK 11+
    - Check your Java version by typing java -version in your terminal.
    - If you have more than one Java version, update Sonarqube's wrapper.conf file (located in conf folder) and replace java with the exact path to your java version.
    - The steps to configure and run SonarQube server can be found on this URL: https://www.c-sharpcorner.com/article/step-by-step-sonarqube-setup-and-run-sonarqube-scanner/
