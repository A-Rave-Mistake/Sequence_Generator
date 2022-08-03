
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

# About

This program creates a sequence of specified number of results. Each **result** is created from generators. A result can be comination of letters, numbers and symbols.

The program has variety of uses, like random full name generator, password generator or ID creator. It can also create lists (in Python for example), sets, dictionaries or more. This program is pretty modular and it's potential is yet to be explored.
  
  

# Documentation

## Dictionary
**sequence** - a list of results created in a specified way  
**result** - a string created from generator(s)  
**combination** - same as **result**  
**generator** - single input (ascii characters, custom text input or a line from text file),  **generator** is treated like a single character in a **combination** string, there can be multiple generators that commit to creating a single **combination**  
**StartWith** - prefix  
**EndWith** - suffix

## Generators

<img src="https://i.imgur.com/FxGbG4F.jpg" alt="gen1">
  
  
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

Each generator can have it's own input, together they can create combination of any amount of inputs, joining them together.
The results then can be separated with new lines AND/OR seperated with our custom seperator, like `,` `-` or `/`

<img src="https://i.imgur.com/FxGbG4F.jpg" alt="gen2">
<p>(Generator group - has two generators, first one [1] inputs a lowercase letter (a-z), second one [2] inputs a random number (0-9). The letter and the number are then joined together to create a <b>result</b>.)</p>
  
**1.** generator group, contains all generators  
**2.** generator order, select in which order the generators are used:  
  * **Ordered (1 -> n)** - loop through every generator in order from first to last  
  * **Random** - randomly loop through generators, each generator can be used more than once and there's no guarantee that any generator will be used even once  
  * **Random (unique)** - randomly loop through generators, guarantees that every generator will be used exactly once  
  * **Random (sequence)** - randomly select only **one** generator from the group  
  
**3.** generator index  
**4.** select input type:  
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
  
**5.** browse files, select a custom text file from your PC  
**6.** Start With prefix, text entry wil be added at the start of generator input  
**7.** End With suffix, text entry wil be added at the end of every generator input  
**8.** add new generator  
**9.** remove all generators  
  
  
## Start With / End With

The program also allows for creation of sets, lists and dictionaries by using **StartWith** and **EndWith** arguments.
Said arguments add prefix and suffix at the end of every sequence or every combination. 
For example if we want to create a list that is ready to use in **Python** we should add `[` at the beginning of sequence and `]` at the end of sequence and tell the program to separate every result/combination with comma and space `, `, which will then create a list output that we can either copy to clipboard or save to a text file.

The StartWith and EndWith arguments are not limited to sequence and can be used in result or generator scope, allowing for prefixes / suffixes at the start / end of every result and at the start / end of every generator input.

<img src="https://i.imgur.com/30EDGvQ.jpg" alt="startend1">
<img src="https://i.imgur.com/Vke6McG.jpg" alt="startend2">
<img src="https://i.imgur.com/daSn6S5.jpg" alt="startend3">

**RED** - Start prefix / End suffix in sequence scope - `[` and `]` are added at the start and end of whole sequence  
**GREEN** - Start prefix / End suffix in combination scope - `-` is added at the start and end of every combination (a single generator group)  
**RED** - Start prefix / End suffix in generator scope - in this case there's only 1 generator present, if there were more `(` would be added at the beginning of every generator input and `)` at the end of it  
  
  
## Separator  
  
<img src="https://i.imgur.com/28iAOyy.jpg" alt="separator1">
  
Separator allows for separating results with entered input, in this case (and by default) the program separates results with **comma** and **space** `, `  
  
  
## New Line Wrapping  
  
This settings inserts every result into a separate line.
  
(New line wrapping enabled)  
<img src="https://i.imgur.com/3xIOceE.jpg" alt="newline1">  
  
(New line wrapping disabled)  
<img src="https://i.imgur.com/pbujDMd.jpg" alt="newline2">
  
 <!--  
 -->  
  
  
# Example Uses  
  
### **Example #1:** Password Generator  
<img src="https://i.imgur.com/1StSjAS.jpg" alt="passwordgenerator">  
  
### **Example #2:** Indexed Alphabet Letters  
<img src="https://i.imgur.com/IsSIzTq.jpg" alt="alphnum">  
  
### **Example #3:** Random Name Generator  
<img src="https://i.imgur.com/euu04Sm.jpg" alt="namegenerator">  
  
### **Example #4:** Python Dictionary Generator  
<img src="https://i.imgur.com/hSGdkco.jpg" alt="dictionary">

---

## Contact
Adrian Urbaniak - @snacks_fancy - adrian.urbaniak1336@gmail.com

##
**Copyright (C) 2022 Adrian Urbaniak (FancySnacks)**
  
Licensed with GNU GPL v3.0 License
License info can be found in LICENSE.md file
