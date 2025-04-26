### **The Factory Pattern**

<br>

**1.	Factory Pattern:**
-	The StorageFactory is responsible for deciding which type of storage to create based on the storage_type string (could be SQL, NoSQL, or InMemory).
- This decouples the repository layer (PaymentRepository) from specific storage details.
<br>

**2.	Repository Layer (PaymentRepository):**
-	The repository depends on an abstraction (Storage interface) and interacts with any concrete storage system.
- The PaymentRepository class uses the Storage abstraction to save and retrieve payments without knowing how or where they are stored.
<br>
  
**3.	Payment Handling:**
-	The Payment class represents the payment model.
-	The repository is used to persist and retrieve Payment objects.
<br>
  
**4.	Decoupling:**
-	The repository doesn't care if the data is stored in a SQL database, NoSQL database, or in memory.
-	You can easily switch the storage mechanism by changing the storage_type in the main function.
<br>

 **Advantages of Using the Factory Pattern Here:**
-	Decoupling: The repository layer doesn’t need to be modified to switch between different types of storage.
-	Flexibility: New storage systems can be added easily (just create a new class that implements the Storage interface).
-	Maintainability: You can change or upgrade storage systems without touching the core business logic in the repository layer.
