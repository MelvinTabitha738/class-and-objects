# 🐍 Python Classes and Objects

This project demonstrates the use of **Classes** and **Objects** in Python, key concepts in Object-Oriented Programming (OOP). It includes examples to explain the creation and usage of classes and how objects are instantiated from these classes.

## 📌 What I Learned

### ✅ What is a Class?

A **class** is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

### ✅ What is an Object?

An **object** is an instance of a class. It holds the actual data and can call the methods defined in the class.

---

## ✨ Syntax for Defining a Class

```python
class ClassName:
    # Constructor (__init__) to initialize object attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Method to perform some actions
    def display_info(self):
        print(f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}")
