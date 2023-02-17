# Technical Challenge Python

## PRE-REQUISITES 📝
To take this challenge you will quite simply need to have access to a computer, email and software that can create a Python application. We strongly recommend that you have a suitable professional environment in which to work.

## INSTRUCTIONS 📃
The purpose of this assessment is to complete a simple programming assignment. You are required to:  

**Before the live session:** 👨‍💻
1. Produce a working and tested source code to solve the problem

This should be delivered to the supplied github repository. If you have any issues with the programming assignment, please ensure that you inform Aptoide immediately. You are expected to work on this task on your own, without help or advice from others. If you need clarification on any aspect of the assessment, please seek help from Aptoide by emailing the Recruitment team.
   
**During the live session (technical interview with Aptoide developers):** 🫱‍🫲🏾
1. Walk through your code with the assessor, answering questions on the code and programming/design choices as requested by the assessor
2. Produce a small piece of code, integrated into you previously developed solution


## CODING ASSIGNMENT 💻
Write a program and associated unit tests that can process a purchase in apps, like we do on Aptoide store. 

Consider that for **each purchase 25% of the value goes to the Aptoide Store (id: "AptoideStore#1")** and the **remaining 75% goes to the app developer, which depends on the app (e.g. id: "TrivialDriveDeveloper#2")**. Also consider that **Aptoide Store rewards users with promotions**.

Assume that there are only 2 apps in the Aptoide Store. The items that can be purchased, which are all priced in EUR, are:
1. In the app **TrivialDrive**, in which the developer ID is "TrivialDriveDeveloper#2":
- Oil – €1.00 
- Antifreeze – €1.20 

2. In the app **DiamondLegend**, in which the developer ID is "DiamondLegendDeveloper#3":
- 5x_Diamonds - €2.00
- 10x_Diamonds - €3.00

The current promotion rewards the user with the following bonus percentage:
- **5% if the user has already done 1 previous purchase**;
- **10% if the user has already done 10 previous purchase**;

The program should accept the app and item to be purchased and the user that is doing the purchase, which is identified by their id (e.g. "User#123").
The program should output the purchase transaction and the updated balance of all of the intervenients (user, developer and Aptoide Store id). If applicable, it should also output the reward transaction and the updated balance of all of the intervenients. 

All the intervenients have an **initial balance of €10.00.**

Input should be via the command line in the following form:  
```TrivialDrive Oil User#123```

Output should be to the console, for example:  
```
PURCHASE TRANSACTION => id: 1; app: TrivialDrive; item: Oil; amount: €1.00; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.75; AptoideStore#1: €0.25}  
BALANCE => User#123: €9.00; TrivialDriveDeveloper#2: €10.75 AptoideStore#1: €10.25
```

If User#123 does a second purchase with the following input:  
```TrivialDrive Antifreeze User#123```

Output to the console should be:  
```
PURCHASE TRANSACTION => id: 2; app: TrivialDrive; item: Antifreeze; amount: €1.20; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.90; AptoideStore#1: €0.30}
BALANCE => User#123: €7.80; TrivialDriveDeveloper#2: €11.65 AptoideStore#1: €10.55
#########
REWARD TRANSACTION => id: 3; amount: €0.06; sender: AptoideStore#1; receivers: {User#123: €0.06}
BALANCE => User#123: €7.86; AptoideStore#1: €10.49
```

The code and design should meet these requirements but be sufficiently flexible to allow for future extensibility. The code should be well structured, suitably commented, have error handling and be tested.

Deadline: XX/XX/2023 23:59
