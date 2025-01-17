# Final_Org_Don_Proj
A code solving the matching delay in an organ transplantation system.

This code essentially involves taking the factors affecting the organ donation system like medical urgency, compatibilty and geographical proximity and running it on a matching algorithm based on ranked recipients who are given a weighted score. Each factor contains a weight factor approximately accurate to the medical standards followed by doctors and surgeons.

For sample, we have used random data and stored it in a database. The matching_algorithm file uses the data from that database to run the code.

(Ignore license file)

To run the program-:
1. Save initialize_db and populate_db as python files in scripts folder in your local machine and run them. (Notice path of organ_matching.db in your system)
2. Edit database path (line 5) in file matching_algorithm.py and save this file under folder app.
3. Save main.py in the file directory as shown in the repo.
4. Now in VSCode terminal open file directory using command - cd "file path" 
5. Create a virtual environment in the folder using command - python -m venv venv
6. Activate the virtual environment using -  .\venv\Scripts\Activate (A virtual environment may already start running in the background. In that case, there is no need to create one.)
7. Run pip install geopy to install used library in the code.
8. Run the main file to see results. (Before running the main file, delete all organ_matching.db which was once created due to the initialization. Those files are already used in main.py)

(try to maintain file directory as shown before running)


Ongoing Developments in code-:
1. The factors are being better calculated with accuracy by referring to certified doctor standards and methods.
2. The database are being converted into an online database (ABDM), and data can be obtained by using APIs.
3. The real-time geo-locations of donor and recipients are being tracked using OpenCage.
4. The backend code can be converted into blockchain technology, after enough experience and knowledge.



Please note the following:
Store all the files in a folder named "OrgDonProj" and open that specific folder in VSCode.

The created database can be viewed in a table format by using an application for sqlite called DB Browser (SQLite).
