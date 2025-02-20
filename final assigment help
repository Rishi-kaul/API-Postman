"""Here’s a step-by-step guide to complete all **6 tasks** in Postman:  

---

### **[Task 1] Make the request**  
1. Open **Postman**.  
2. Go to your **API Fundamentals Student Expert collection**.  
3. Click **New Request** → Name it **"skill check"**.  
4. Set the **method** to **POST**.  
5. Set the **endpoint URL** to:  
   ```
   https://postman-echo.com/post
   ```
6. Save the request under your collection **below the "delete a book" request**.  

---

### **[Task 2] Add a query parameter called "movieName"**  
1. In Postman, open the **Params** tab.  
2. Add a **new query parameter**:  
   - **Key**: `movieName`  
   - **Value**: `<Your Favorite Movie>` (e.g., *Inception*)  

---

### **[Task 3] Turn your base URL into a variable**  
1. Go to **Collections** → Select your API Fundamentals collection.  
2. Click **Variables** and add:  
   - **Variable Name**: `skillcheckBaseUrl`  
   - **Initial Value**: `https://postman-echo.com`  
   - **Current Value**: `https://postman-echo.com`  
3. Change your request URL to use this variable:  
   ```
   {{skillcheckBaseUrl}}/post
   ```

---

### **[Task 4] Use API Key Authorization**  
1. Open the **Authorization** tab in your "skill check" request.  
2. Set **Type** to `API Key`.  
3. Configure it as:  
   - **Key**: `student-expert`  
   - **Value**: `skillcheck`  
   - **Add To**: `Query Params`  

---

### **[Task 5] Add a JSON body with the property "actorName"**  
1. Open the **Body** tab.  
2. Select **raw** and set the format to **JSON**.  
3. Add this JSON:  
   ```json
   {
     "actorName": "Leonardo DiCaprio"
   }
   ```  
4. Send the request and check the response.

---

### **[Task 6] Set a variable using a post-response script**  
1. Open the **Tests** tab.  
2. Add the following JavaScript code:  
   ```js
   let responseData = pm.response.json();
   pm.collectionVariables.set("favoriteActor", responseData.json.actorName);
   ```  
3. Send the request again.  
4. Go to **Collections → Variables** and confirm that `favoriteActor` is updated.

---

### **Final Step: Run Collection Tests**  
1. Open the **Runner** in Postman.  
2. Select your **API Fundamentals Student Expert collection**.  
3. Click **Run Collection** and check if all tests pass! ✅  

Good luck! 🚀 Let me know if you need help.




It looks like Postman is expecting the **`favoriteActor`** variable to be set using the **correct syntax** in your test script. Let's fix it!

### **Correct Postman Test Script**
1. Open your **"skill check"** request.  
2. Go to the **Tests** tab.  
3. Replace your existing script with the following:

   ```js
   let responseData = pm.response.json();
   pm.collectionVariables.set("favoriteActor", responseData.actorName);
   ```

### **Explanation of Fix**
- **`pm.response.json();`** → Extracts the JSON response.  
- **`responseData.actorName`** → Correctly accesses the `actorName` from the response body.  
- **`pm.collectionVariables.set("favoriteActor", responseData.actorName);`** → Saves it as a **collection variable** named `favoriteActor`.  

### **Final Steps**
1. **Save** your changes.  
2. **Send the request again.**  
3. Go to **Collections → Variables** and check if `favoriteActor` is correctly updated.  
4. Run your **Postman collection tests** again.  

This should fix the **AssertionError** and allow the test to pass! 🚀 Let me know if you need more help. 😊
"""
