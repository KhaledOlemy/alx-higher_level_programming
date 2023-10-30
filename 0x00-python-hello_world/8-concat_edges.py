#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str[str.find('object'):str.find('language')-1} {str[str.find('with'):str.find('very')-1]} {str[:str.find(' ')}"
print(str)
