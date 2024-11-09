# User Story 1 – Parent
As a parent, I want to view the baby’s data so I can provide proper care for the baby. I want to enter relevant information into BabyDataApp so I can keep track of my baby’s progress. I want to edit the baby’s data so that I can correct any information erroneously entered in high stress times (i.e. sick baby in the middle of the night, improperly entered a feeding).
## Acceptance Criteria
The Parent User Story has been satisfied when:
-	The parent can view all data relevant to their baby.
-	The parent can add data relevant to their baby.
-	The parent can edit erroneous data relevant to their baby.

# User Story 2 – Medical Professional
As a medical professional, I want to view the baby’s data so that I can provide proper treatment for the baby in the event of an illness or accident.
## Acceptance Criteria
The Medical Professional User Story has been satisfied when:
-	The medical professional can view all data relevant to the baby.

# User Story 3 – Babysitter/Temporary Caregiver
As a babysitter/temporary caregiver, I want to view the baby’s data so I can properly care for the baby. I want to enter relevant events into BabyDataApp so the parents can keep track of the baby’s events while away.
## Acceptance Criteria
The Babysitter/Temporary Caregiver User Story has been satisfied when:
-	The babysitter/temporary caregiver can view all data relevant to the baby.
-	The babysitter/temporary caregiver can add data relevant to the baby.

# Mis-User Story 1 – Malicious Internet User
As a malicious internet user, I want to edit the baby’s data so I can prevent the parents from monitoring the baby’s progress.
## Mitigation Criteria
The Malicious Internet User Mis-User Story has been mitigated when:
-	Proper permissions have been implemented that prevent random users from editing a baby’s data.
-	Data transmitted between the database and the user interface has been encrypted to prevent unauthorized users from viewing a baby’s data.

# Mis-User Story 2 – Angry Neighbor (Reason of Anger Unknown)
As an angry neighbor, I want to view the baby’s data so I can plan loud, chaotic parties when the baby is sick or asleep.
## Mitigation Criteria
The Angry Neighbor Mis-User Story has been mitigated when:
-	Access controls have been implemented to prevent unauthorized data access.


# BabyDataApp Mockup
## BabyDataApp Login Page
![image](https://github.com/user-attachments/assets/d05b76ea-cd4f-429c-bf9c-e46f5f93b422)

## The user can view which babies they have access to.
![image](https://github.com/user-attachments/assets/caad8449-28a2-456f-b613-6d0427b6a136)

## If the user has the proper access, they can add a baby.
![image](https://github.com/user-attachments/assets/fcc52e34-4a0f-4bc7-8d93-f87bedfd8420)

## If the user has the proper access, they can edit and/or delete the baby from the app. If there are many babies, the user can also filter by the baby’s name, age, and any allergies.
![image](https://github.com/user-attachments/assets/2253c723-2717-46b9-8cdb-faef1c53d091)
 
## The parents will be able to add users and control their access levels to ensure only the proper personnel have the minimum access needed to complete their tasks.
![image](https://github.com/user-attachments/assets/30a42bdd-bef3-4db7-a4c0-abe321a52c74)

## If the user has access to add an event, this is the event page they will see.  
![image](https://github.com/user-attachments/assets/2a0fff10-621c-46ea-9d38-321aab1a1e74)

## This is the user page where the baby’s events for a day can be viewed.
![image](https://github.com/user-attachments/assets/113db9c7-0271-4094-a010-3466f1a42a75)


# BabyDataApp C4 Architecture Diagrams
## Context Diagram
![image](https://github.com/user-attachments/assets/10e5c826-730e-4413-9378-5e8d7f5aa2ea)

## Container Diagram
![image](https://github.com/user-attachments/assets/abf252ea-010c-4d33-a930-733e5e098a06)

## Component Diagram
![image](https://github.com/user-attachments/assets/e429d0aa-84b3-4266-98f0-ff53118075e1)




