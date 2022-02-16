
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/RobertoSaback">
    <img src="images/zelogo.png" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Ze Code Challenge</h3>

  <p align="center">
    Roberto Saback - Quality Assurance 
    <br />
    <a href="https://github.com/RobertoSaback/ZeChallenge/find/master"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#First-part">First part of the Challenge</a>
    ·
    <a href="#Seccond-Part">Seccond part of the Challenge</a>
    ·
    <a href="#Final-Considerations">Final Considerations</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#First-part">First part of the challenge</a>
    <li>
      <a href="#Seccond-Part">Seccond part of the challenge</a>
      <ul>
        <li><a href="#Setting-Up">Setting the environment</a></li>
        <li><a href="#Test-Suit">Test Suit</a></li>
        <li><a href="#Why-Python">Why Python</a></li>
      </ul>
    <li><a href="#Final-Considerations">Final Considerations</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## First Part 

Critical Flows

<br>
  *<strong>Product flow</strong>: This flows refers to the movement of the goods from the supplier to the customer and it would be impossible without a product selection stage to complete the service. The product flow play a key role in moving products through this logistic chain.In fact logistics take the primary onus of an e-commerce entity. Efficiency and service usually reflects this flow as the greatest value for the company since then efficiency  creates a value to the customers , suppliers and stakeholders and it creates visibility into a company.
  <br><br>
  *<strong>Cash flow</strong>: Cash flow: The core idea behind every business is increase profits and value. For this reason a reliable cash flow ensures optimum user experience, consumer safety and fidelity to the future new customers. It ensure that the customer can trust on the company to share sensitive information and the company can trust that all information that comes from the client side are reliable. 
    <br><br>
*<strong>Information Flow</strong>: This flow happens in both the directions and it is necessary for the proper functioning of all the activities in an E-Commerce model. Customers ask for information and likewise the retailer also requires information from the customer. Since, the process is basically online, this flow is important for a smooth transaction and seamless working of the e-commerce.

## Seccond Part

### Setting-Up
For this seccond part I'm assuming that you have an IDE and a pack manager and python installed on your computer. 
With Pip installed you should install selenium modules:<br>
   1. Clone the repo
   ```sh
   git clone https://github.com/RobertoSaback/ZeChallenge.git
   ```
   2. Install PIP packages
   ```sh
   $ pip install selenium
   ```
   <br> 
In that way you will install selenium dependencies in your local machine and then you can use your shell to read the files.

## Test-Suit

| Test Case ID | TC Summary  | Prerequisites | Test Script | Actual Result | Expected Result | Status |  
| --- | --- | --- | --- | --- |  --- |  --- |
| [`TC001`](https://github.com/RobertoSaback/ZeChallenge/blob/master/TC001.py) | Verify if the user can select an item to the cart |<ul> <li>Have a valid account on Zé Delivery</li><li> Stay logged in</li></ul> | <ul> <li>Select an Item and click on it</li><li>Click on Add Button</li><li>Close the bubble</li></ul> | Item is properly selected and the amount of items shows up on the bag icon | Item is properly selected and the amount of items shows up on the bag icon | Passed  |
| [`TC002`](https://github.com/RobertoSaback/ZeChallenge/blob/master/TC002.py) | Verify if bag icon can accept more than 3 characters |<ul> <li>Have a valid account on Zé Delivery</li><li> Stay logged in</li></ul> | <ul> <li>On the product page select a beer</li><li>click 9 times on "adicionar 10 itens" button</li><li>Click on "adicionar na sacola"</li><li>Close the bubble</li></ul> | The total amount of items doesn't matches with the bag number, it has a limit of 99 items | Items and the bag icon matches with the same amount | Failed |
| [`TC003`](https://github.com/RobertoSaback/ZeChallenge/blob/master/TC003.py) | Verify if discount are applied in products of same type |<ul> <li>Have a valid account on Zé Delivery</li><li> Stay logged in</li></ul> | <ul> <li>Select an Item on the product page</li><li>Click 9 times on Add +10 items Button</li><li> Click on add Item to the bag button</li><li>Close the bubble</li></ul> | The total price matches with the total rested the discounts | The total price matches with the total rested the discounts | Passed |
| [`TC004`](https://github.com/RobertoSaback/ZeChallenge/blob/master/TC004.py) | Verify if discount are applied in products of different types |<ul> <li>Have a valid account on Zé Delivery</li><li> Stay logged in</li></ul> |  <ul> <li>On the product page select an Item and click on it</li><li>Click 9 times on Add +10items Button</li><li> Click on add Item to the bag button</li><li>Go back to the product page and repeat the process with another item from same type ( ex: two brands of  different beers) </li><li>Close the bubble</li></ul> | The discount amount matches with the price | The discount amount matches with the price | Passed | 
| [`TC005`](https://github.com/RobertoSaback/ZeChallenge/blob/master/TC005.py) | Verify if the user can select items from different categories |<ul> <li>Have a valid account on Zé Delivery</li><li> Stay logged in</li></ul> | <ul> <li>On the product page select an Item and click on it</li><li>Click 9 times on Add +10items Button</li><li> Click on add Item to the bag button</li><li>Go back to the product page and repeat the process with another item from same type ( ex: two brands of  different beers) </li><li>Close the bubble</li></ul> 

## Why Python

Python is object-oriented and functional. It lets programmers decide if functions or classes are better for the needs at hand. This is awesome for test automation because:<br>
* stateless functions avoid side effects 
* Simple syntax for those functions make them readable. 
* Matches very well with the command line, the entire test automation workflow can be driven from the command line
* Easy to learn (looks like english)
* Have a great active community behind creating libraries and support material everyday <br>

## Final Considerations

A message to ze-engineering-code-challenge team,

Well thank you for your time. I am sure you have lots of candidates to see, but
I wanted to say one last thing: There are no shortages of developers for you to interview. However, there is a shortage of good, talented, egoless, developers with ambition to learn. The best developers aren’t the ones that know the language inside and out at the expense of having blinders. It is not the ones who are unable to admit they are wrong. I may not be the most experienced developer that you will interview, but the one thing that you can guarantee is that there is nobody that you will interview that will work as hard to develop his/her skills every day, play nicely with other developers, and isn’t so narrow minded in problem solving that he/she isn’t willing to try new novel ideas. When you hire me you will rest assured that you won’t have to micromanage me, you don’t have to extinguish fires, and in one year, I will be one of your most valuable employees. I am at a point in my career where I want to be surrounded by a team that I can grow with and I have chosen apply for a Q.A. position in Zé Delivery for this specific reason. You have probably had similar experience in your career when one company allowed you to really have an impact. I am at that stage now, and I look forward to be part of this team. 
<br><br>
Thank you. Sincerely ,<br>
Roberto Saback
