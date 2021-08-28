### Classes and Objects
> **Class**: An abstract blueprint used to create more specific , concrete objects (model) 
Classes contain:
- **Attributes** : category of qualities of an object (name, ID, birthdate)
- **Method** : functions that perform some sort of action for the class
- **Objects** : individual instances instantiated, or created, from the class (blueprint)

### Inheritance and Polymorphism: Overloading and Overriding
> **Inheritance**: Child casses inherit data (attributes) and behaviors (methods) from their parent class.
- Create child classes with **inherited** behaviors of the parent class
> **Polymorphism**: many methods that can do the same task; designing objects to share behaviors
- **Polymorphism** allows the same method to execute different behaviors in two ways: method overriding and method overloading.
  - Method Overriding: A child class can provide a differrent implementation than its parents
    - Used by runtime polymorphism. 
  - Method Overloading: Methods of the same name can have different number of parameters passed into the method call. 
    - Used by compile time polymorphism.

### Abstraction and Encapsulation
> **Encapsulation**: containing information in an object and only exposing selected information; hides the internal software code implementation inside a class, and hides internal data of inside objects
- methods help programmers promote reusability and keep functionality **encapsulated** inside an object
- **Encapsulation** adds security to the program.
*class HerdingDog extends Dog*
- **Private/ Internal Interface**: methods and properties accessible from other methods of the same class
- **Public/ External Interface**: methods and properties accessible also from outisde the class
- **Protected**: Only accessible to child classes
> **Abstraction**: only exosing high level public methds for accessing an object; only displaying selected pieces of data, and only allowing data to be accessed through classes and modified through methods

### Access Modifiers


### Static, Final, This and Super keyworks and interfaces
- _variable, the _ indicates that the variable is protected and it should't be modified directly (use a method)
