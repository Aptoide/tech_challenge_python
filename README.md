# Technical Challenge Python

## INSTRUCTIONS 📃
The purpose of this assessment is to complete a simple programming assignment. If you have any issues, seek help from Aptoide's Recruitment team. You are expected to work on this task on your own, without help or advice from others. You are required to:  

**Before the technical interview:** 👨‍💻
1. Produce a **working, well-structured, extensible and tested** source code to solve the problem, and share it with us via Github.
   
**During the technical interview:** 🫱‍🫲🏾
1. Walk through your code with the assessor, answering questions on the code and programming/design choices
2. Produce a small piece of code, integrated into you previously developed solution

## CODING ASSIGNMENT 💻
Write a program that can process a purchase in apps, like we do on Aptoide store. 

Consider that for **each purchase 25% of the value goes to the Aptoide Store (id: "AptoideStore#1")** and the **remaining 75% goes to the app developer, which depends on the app (e.g. id: "TrivialDriveDeveloper#2")**. Also consider that **Aptoide Store rewards users with promotions**. 

Assume that there are only 2 apps in the Aptoide Store. The items that can be purchased, which are all priced in EUR, are:
1. In the app **TrivialDrive**, in which the developer ID is "TrivialDriveDeveloper#2":
- Oil – €1.00 
- Antifreeze – €1.20 

2. In the app **DiamondLegend**, in which the developer ID is "DiamondLegendDeveloper#3":
- 5x_Diamonds - €2.00

The current promotion rewards the user with the following bonus percentage:
- **5% if the user has already done 1 previous purchases in the app**;
- **10% if the user has already done 10 previous purchases in the app**.

The program should accept via the command line the app, the item to be purchased and the user that is doing the purchase. And it should output the purchase transaction and the updated balance of all of the intervenients (users, developers and store) . If applicable, it should also output the reward transaction and the updated balance of all of the intervenients.

## EXAMPLE 📃
Assuming all intervenients have an initial balance of €10.00. 

Input:
```TrivialDrive Oil User#123```

Output:
```
PURCHASE TRANSACTION => id: 1; app: TrivialDrive; item: Oil; amount: €1.00; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.75; AptoideStore#1: €0.25}  
BALANCE => User#123: €9.00; TrivialDriveDeveloper#2: €10.75 AptoideStore#1: €10.25
```

Input:
```TrivialDrive Antifreeze User#123```

Output:  
```
PURCHASE TRANSACTION => id: 2; app: TrivialDrive; item: Antifreeze; amount: €1.20; sender: User#123; receivers: {TrivialDriveDeveloper#2: €0.90; AptoideStore#1: €0.30}
BALANCE => User#123: €7.80; TrivialDriveDeveloper#2: €11.65 AptoideStore#1: €10.55
#########
REWARD TRANSACTION => id: 3; amount: €0.06; sender: AptoideStore#1; receivers: {User#123: €0.06}
BALANCE => User#123: €7.86; AptoideStore#1: €10.49
```
