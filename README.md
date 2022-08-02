
<!-- GENERAL INFO -->

<div align="center">
  <h3 align="center">SEQUENCE GENERATOR</h3>
  <h4 align="center">Generate sequence of combinations put together from ascii characters or from custom text files</h4>
  <p align="center">
    Made by Adrian Urbaniak
  </p>
  <img src="https://i.imgur.com/aoGcd6t.jpg" alt="Logo">
  <p>(Screenshot representing the program in use)</p>
</div>

<!-- ABOUT -->

## About

This program creates a sequence of specified amount of results. Each **result** is created from generators. A result can be comination of letters, numbers and symbols.
A **generator** is a single input, a result can be made from one of more generators in specified order (ordered, randomized and randomized uniquely).

A single generator can create:
* a lowercase letter (a-z)
* a uppercase letter (A-Z)
* a number (1,2,3,4,5 and so on)
* a random symbol (@./$ etc.)
* a random lowercase letter
* a random uppercase letter
* a random number (0-9)
* a random character (lowercase/uppercase letters, numbers or symbols)
* a line from inserted .txt file (in proper order or randomized order)
* custom text input

Each generator can have it's own input, it can create combination of any amount of inputs we can, joining them together.
The results then can be separated with new lines AND/OR seperated with our custom seperator, like `,` `-` or `/`

The program also allows for creation of sets, lists and dictionaries by using **StartWith** and **EndWith** arguments.
Said arguments add prefix and suffix at the end of every sequence or every combination. 
For example if we want to create a list that is ready to use in **Python** we should add `[` at the beginning of sequence and `]` at the end of sequence and tell the program to separate every result/combination with comma and space `, `, which will then create a list output that we can either copy to clipboard or save to a text file.

The StartWith and EndWith arguments are not limited to sequence and can be used in result or generator scope, allowing for prefixes / suffixes at the start / end of every result and at the start / end of every generator input.

<img src="https://i.imgur.com/Vke6McG.jpg" alt="startend1">
<img src="https://i.imgur.com/daSn6S5.jpg" alt="startend2">

**RED** - Start prefix / End suffix in sequence scope - `[` and `]` are added at the start and end of whole sequence  
**GREEN** - Start prefix / End suffix in combination scope - `-` is added at the start and end of every combination (a single generator group)  
**RED** - Start prefix / End suffix in generator scope - in this case there's only 1 generator present, if there were more `(` would be added at the beginning of every generator input and `)` at the end of it  




## Contact
Adrian Urbaniak - @snacks_fancy - adrian.urbaniak1336@gmail.com

##
**Copyright (C) 2022 Adrian Urbaniak (FancySnacks)**
  
Licensed with GNU GPL v3.0 License
License info can be found in LICENSE.md file
